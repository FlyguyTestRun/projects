"""
==============================================================================
FastAPI Application Entry Point
==============================================================================
Location: src/main.py
Purpose: Main application file with API endpoints
Framework: FastAPI (high-performance async web framework)
==============================================================================
"""

import os
import logging
from datetime import datetime
from typing import Dict, List, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
import asyncpg

# ==============================================================================
# CONFIGURATION
# ==============================================================================

# Environment variables
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/myapp")

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ==============================================================================
# DATABASE CONNECTION POOL
# ==============================================================================

# Global database pool (initialized in lifespan)
db_pool: Optional[asyncpg.Pool] = None


async def get_db_pool() -> asyncpg.Pool:
    """
    Dependency function to get database connection pool.
    
    Returns:
        asyncpg.Pool: Database connection pool
    
    Raises:
        RuntimeError: If database pool is not initialized
    """
    if db_pool is None:
        raise RuntimeError("Database pool not initialized")
    return db_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    
    Startup:
        - Initialize database connection pool
        - Run migrations (if needed)
        - Initialize cache
    
    Shutdown:
        - Close database connections
        - Cleanup resources
    """
    global db_pool
    
    # STARTUP
    logger.info(f"Starting application in {ENVIRONMENT} mode...")
    
    try:
        # Initialize database connection pool
        logger.info("Connecting to database...")
        db_pool = await asyncpg.create_pool(
            DATABASE_URL,
            min_size=2,
            max_size=10,
            command_timeout=60
        )
        logger.info("Database connection pool created successfully")
        
        # Test database connection
        async with db_pool.acquire() as conn:
            version = await conn.fetchval("SELECT version()")
            logger.info(f"Connected to: {version}")
            
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise
    
    yield  # Application runs here
    
    # SHUTDOWN
    logger.info("Shutting down application...")
    
    if db_pool:
        await db_pool.close()
        logger.info("Database connections closed")


# ==============================================================================
# FASTAPI APPLICATION
# ==============================================================================

app = FastAPI(
    title="Professional Microservice API",
    description="Production-grade FastAPI microservice with Docker and WSL2",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

# ==============================================================================
# MIDDLEWARE
# ==============================================================================

# CORS middleware (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom request logging middleware
@app.middleware("http")
async def log_requests(request, call_next):
    """Log all HTTP requests"""
    start_time = datetime.utcnow()
    response = await call_next(request)
    duration = (datetime.utcnow() - start_time).total_seconds()
    
    logger.info(
        f"{request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Duration: {duration:.3f}s"
    )
    
    return response


# ==============================================================================
# PYDANTIC MODELS (Request/Response Schemas)
# ==============================================================================

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Service status")
    environment: str = Field(..., description="Current environment")
    version: str = Field(..., description="Application version")
    timestamp: datetime = Field(..., description="Current server time")
    database: str = Field(..., description="Database connection status")


class UserCreate(BaseModel):
    """User creation request model"""
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "password": "securepassword123",
                "full_name": "John Doe"
            }
        }


class UserResponse(BaseModel):
    """User response model (no password)"""
    id: str = Field(..., description="User UUID")
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email address")
    full_name: Optional[str] = Field(None, description="Full name")
    is_active: bool = Field(..., description="Account active status")
    created_at: datetime = Field(..., description="Account creation timestamp")


class ProjectResponse(BaseModel):
    """Project response model"""
    id: str = Field(..., description="Project UUID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    status: str = Field(..., description="Project status")
    created_at: datetime = Field(..., description="Creation timestamp")


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

@app.get(
    "/",
    summary="Root endpoint",
    description="Welcome message and API information",
    response_model=Dict[str, str]
)
async def root():
    """
    Root endpoint - API welcome message.
    
    Returns:
        dict: Welcome message and documentation links
    """
    return {
        "message": "Welcome to the Professional Microservice API",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
        "version": "0.1.0"
    }


@app.get(
    "/health",
    summary="Health check",
    description="Check API and database health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK
)
async def health_check(pool: asyncpg.Pool = Depends(get_db_pool)):
    """
    Health check endpoint.
    
    Verifies:
        - API is running
        - Database connection is working
        - System resources are available
    
    Returns:
        HealthResponse: Health status information
    
    Raises:
        HTTPException: If health check fails
    """
    try:
        # Test database connection
        async with pool.acquire() as conn:
            await conn.fetchval("SELECT 1")
        db_status = "connected"
        
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        db_status = "disconnected"
    
    return HealthResponse(
        status="healthy",
        environment=ENVIRONMENT,
        version="0.1.0",
        timestamp=datetime.utcnow(),
        database=db_status
    )


@app.get(
    "/users",
    summary="List users",
    description="Get all users (paginated)",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK
)
async def list_users(
    limit: int = 10,
    offset: int = 0,
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """
    List all users with pagination.
    
    Args:
        limit: Maximum number of users to return (default: 10)
        offset: Number of users to skip (default: 0)
        pool: Database connection pool (injected)
    
    Returns:
        List[UserResponse]: List of users
    
    Example:
        GET /users?limit=5&offset=0
    """
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT id, username, email, full_name, is_active, created_at
                FROM users
                WHERE deleted_at IS NULL
                ORDER BY created_at DESC
                LIMIT $1 OFFSET $2
                """,
                limit, offset
            )
            
            users = [
                UserResponse(
                    id=str(row["id"]),
                    username=row["username"],
                    email=row["email"],
                    full_name=row["full_name"],
                    is_active=row["is_active"],
                    created_at=row["created_at"]
                )
                for row in rows
            ]
            
            return users
            
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch users"
        )


@app.get(
    "/users/{user_id}",
    summary="Get user by ID",
    description="Retrieve a specific user by their UUID",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
async def get_user(
    user_id: str,
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """
    Get a specific user by ID.
    
    Args:
        user_id: User UUID
        pool: Database connection pool (injected)
    
    Returns:
        UserResponse: User information
    
    Raises:
        HTTPException: If user not found (404)
    """
    try:
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                """
                SELECT id, username, email, full_name, is_active, created_at
                FROM users
                WHERE id = $1 AND deleted_at IS NULL
                """,
                user_id
            )
            
            if not row:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User {user_id} not found"
                )
            
            return UserResponse(
                id=str(row["id"]),
                username=row["username"],
                email=row["email"],
                full_name=row["full_name"],
                is_active=row["is_active"],
                created_at=row["created_at"]
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch user"
        )


@app.get(
    "/projects",
    summary="List projects",
    description="Get all active projects",
    response_model=List[ProjectResponse],
    status_code=status.HTTP_200_OK
)
async def list_projects(
    limit: int = 10,
    offset: int = 0,
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """
    List all active projects.
    
    Args:
        limit: Maximum number of projects to return
        offset: Number of projects to skip
        pool: Database connection pool (injected)
    
    Returns:
        List[ProjectResponse]: List of projects
    """
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT id, name, description, status, created_at
                FROM projects
                WHERE deleted_at IS NULL AND status = 'active'
                ORDER BY created_at DESC
                LIMIT $1 OFFSET $2
                """,
                limit, offset
            )
            
            projects = [
                ProjectResponse(
                    id=str(row["id"]),
                    name=row["name"],
                    description=row["description"],
                    status=row["status"],
                    created_at=row["created_at"]
                )
                for row in rows
            ]
            
            return projects
            
    except Exception as e:
        logger.error(f"Error fetching projects: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch projects"
        )


# ==============================================================================
# ERROR HANDLERS
# ==============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.utcnow().isoformat()
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Catch-all exception handler"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal server error",
            "status_code": 500,
            "timestamp": datetime.utcnow().isoformat()
        }
    )


# ==============================================================================
# APPLICATION ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes (development only)
        log_level=LOG_LEVEL.lower()
    )


# ==============================================================================
# NOTES FOR STUDENTS
# ==============================================================================
#
# This FastAPI application demonstrates:
# 1. Async database connections with asyncpg
# 2. Dependency injection (Depends)
# 3. Pydantic models for validation
# 4. Proper error handling
# 5. Logging
# 6. CORS configuration
# 7. API documentation (auto-generated)
# 8. Lifespan events (startup/shutdown)
#
# Key Concepts:
# - async/await: Non-blocking I/O for better performance
# - Type hints: Better IDE support and validation
# - Dependency injection: Clean, testable code
# - Middleware: Request/response processing
# - Exception handlers: Centralized error handling
#
# Best Practices:
# - Always validate input with Pydantic
# - Use dependency injection for shared resources
# - Log important events and errors
# - Handle exceptions gracefully
# - Document your endpoints
# - Use async for I/O operations
#
# ==============================================================================

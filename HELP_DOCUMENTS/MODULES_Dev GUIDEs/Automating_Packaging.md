# Professional Development Environment - Week-Long Class Curriculum

**Course Title:** Production-Grade Development with WSL2, Docker, and VS Code  
**Duration:** 5 Days (40 hours total)  
**Target Audience:** Junior developers, students, career switchers  
**Prerequisites:** Basic Python knowledge, Windows 10/11 PC  
**Outcome:** Students will build and deploy a containerized microservice

---

## Course Overview

### Learning Objectives

By the end of this course, students will be able to:

1. **Configure** a professional development environment using WSL2 and Docker
2. **Build** containerized applications following industry best practices
3. **Debug** applications inside containers using VS Code
4. **Test** code with pytest and achieve >80% coverage
5. **Deploy** microservices to production environments
6. **Collaborate** effectively using Git across multiple machines

### Teaching Philosophy

- **Hands-on first:** Students use pre-built containers on Day 1
- **Progressive complexity:** Build from working code to understanding internals
- **Production-ready:** Everything taught is used in real companies
- **No magic:** Every configuration file is explained line-by-line

---

## Week Structure

| Day | Focus | Hours | Student Deliverable |
|-----|-------|-------|-------------------|
| Day 1 | Environment Setup & Docker Basics | 8h | Running containerized app |
| Day 2 | VS Code & Development Workflow | 8h | Debugged and tested feature |
| Day 3 | Database Integration & APIs | 8h | REST API with database |
| Day 4 | Testing & Code Quality | 8h | Test suite with 80%+ coverage |
| Day 5 | Deployment & Best Practices | 8h | Deployed microservice |

---

## Daily Breakdown

---

## DAY 1: Environment Setup & Docker Basics

**Goal:** Students run a working containerized application by end of day

### Session 1: Introduction & Concepts (2 hours)

#### Learning Objectives
- Understand virtualization vs containerization
- Explain WSL2 architecture
- Identify benefits of containerized development

#### Topics
1. **Why Containers?** (30 min)
   - Traditional development problems
   - "Works on my machine" syndrome
   - Dependency hell
   - Environment consistency

2. **WSL2 vs Traditional VMs** (30 min)
   - Resource usage comparison
   - Performance benchmarks
   - Use cases for each

3. **Docker Architecture** (45 min)
   - Images vs Containers
   - Layers and caching
   - Docker Engine architecture
   - Container lifecycle

4. **Course Overview** (15 min)
   - Week roadmap
   - Final project preview
   - Q&A

#### Activities
- **Demo:** Instructor shows final project running
- **Discussion:** Real-world containerization use cases
- **Diagram:** Students draw Docker architecture

#### Resources Provided
- COMPLETE_SETUP_GUIDE.md
- Architecture diagrams
- Glossary of terms

---

### Session 2: WSL2 Installation (2 hours)

#### Learning Objectives
- Install and configure WSL2
- Understand `.wslconfig` settings
- Troubleshoot common installation issues

#### Step-by-Step Guide

**Part 1: Prerequisites Check (15 min)**
```powershell
# Students run these commands
wsl --version
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

**Part 2: .wslconfig Creation (30 min)**
- Instructor explains each setting
- Students create file together
- Class discusses memory/CPU allocation

**Part 3: wsl.conf Setup (30 min)**
- Navigate to WSL Ubuntu
- Create wsl.conf with sudo
- Understand systemd importance

**Part 4: Verification (30 min)**
```bash
# Students verify installation
wsl --status
systemctl --version
free -h  # Check memory limits
```

**Part 5: Troubleshooting Session (15 min)**
- Common errors and fixes
- Peer helping

#### Checkpoints
- [ ] WSL2 version displayed correctly
- [ ] Systemd running
- [ ] Memory limits applied (6GB max)

#### Homework Assignment
- Document your system specifications
- Screenshot working WSL2 terminal
- Write 3 questions about what you don't understand

---

### Session 3: Docker Installation (2 hours)

#### Learning Objectives
- Install Docker in WSL2
- Configure Docker Desktop
- Understand resource limits

#### Hands-On Lab

**Lab 1: Docker Installation (45 min)**
```bash
# Students follow along
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify
docker --version
docker compose version
docker run hello-world
```

**Lab 2: Docker Desktop Configuration (30 min)**
- Settings walkthrough
- Resource allocation discussion
- WSL Integration setup

**Lab 3: First Container (45 min)**
```bash
# Students run together
docker run -d -p 8080:80 nginx
curl localhost:8080
docker ps
docker logs <container_id>
docker stop <container_id>
```

#### Key Concepts Introduced
- Container lifecycle: run, stop, start, rm
- Port mapping (-p flag)
- Detached mode (-d flag)
- Container logs
- Image pulling

#### Exit Ticket
Students must successfully:
1. Run nginx container
2. Access it in browser
3. View logs
4. Stop and remove container

---

### Session 4: Running Pre-Built Application (2 hours)

#### Learning Objectives
- Clone repository
- Understand docker-compose.yml
- Start multi-container application
- Navigate API documentation

#### Hands-On Project

**Part 1: Repository Setup (30 min)**
```bash
# Instructor provides repository
git clone <course-repo-url> ~/projects/class-project
cd ~/projects/class-project
ls -la  # Explore structure
```

**Part 2: docker-compose Explanation (30 min)**
- Instructor walks through docker-compose.yml
- Students annotate their copy
- Discuss each service (web, db, cache)

**Part 3: Start Application (45 min)**
```bash
# Students start services
docker compose up -d

# Verify
docker compose ps
docker compose logs web
curl localhost:8000/health
```

**Part 4: API Exploration (15 min)**
- Open http://localhost:8000/docs
- Students try endpoints
- Create test users via Swagger UI

#### Success Criteria
- [ ] All containers running (green status)
- [ ] Health check returns "healthy"
- [ ] Can create user via API docs
- [ ] Can list users

#### End of Day Review (15 min)
- What we accomplished
- Questions and troubleshooting
- Preview Day 2

---

## DAY 2: VS Code & Development Workflow

**Goal:** Students modify code, debug, and see changes in containers

### Session 1: VS Code Setup (2 hours)

#### Learning Objectives
- Install required extensions
- Connect VS Code to WSL2
- Navigate container filesystem
- Understand dev containers

#### Installation Checklist

**Required Extensions:**
1. Remote - WSL
2. Docker
3. Python
4. Dev Containers
5. GitLens

**Lab: VS Code Connection (60 min)**
```bash
# From WSL terminal
code ~/projects/class-project
```

- Instructor demonstrates:
  - WSL indicator (bottom-left)
  - Integrated terminal
  - File explorer in WSL
  - Running tasks

**Lab: Dev Container Setup (60 min)**
- Open `.devcontainer/devcontainer.json`
- Understand each setting
- Reopen in container: `Ctrl+Shift+P` → "Reopen in Container"
- Verify Python interpreter inside container

#### Checkpoints
- [ ] VS Code connected to WSL
- [ ] Can edit files
- [ ] Terminal shows container prompt
- [ ] Extensions loaded in container

---

### Session 2: Code Navigation & Editing (2 hours)

#### Learning Objectives
- Navigate Python project structure
- Understand FastAPI application
- Make first code modification
- See changes live

#### Code Walkthrough (60 min)

**File-by-File Review:**

1. **`src/main.py`** (20 min)
   - FastAPI imports
   - App initialization
   - Endpoint definitions
   - Students add comments explaining each function

2. **`src/__init__.py`** (5 min)
   - Package initialization
   - Version info

3. **`docker-compose.yml`** (20 min)
   - Service definitions
   - Environment variables
   - Volume mounts
   - Networks

4. **`Dockerfile`** (15 min)
   - Multi-stage build
   - Base image
   - Dependencies
   - Entry point

#### Hands-On Exercise (60 min)

**Task: Add a New Endpoint**

Students add this to `src/main.py`:

```python
@app.get("/hello/{name}")
async def greet_user(name: str):
    """Greet a user by name"""
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.utcnow()
    }
```

**Steps:**
1. Edit `src/main.py`
2. Save file
3. Container auto-reloads (because of --reload flag)
4. Test: `curl localhost:8000/hello/YourName`
5. Check in Swagger docs: http://localhost:8000/docs

#### Success Criteria
- [ ] New endpoint appears in API docs
- [ ] Returns correct JSON response
- [ ] Auto-reload works

---

### Session 3: Debugging with VS Code (2 hours)

#### Learning Objectives
- Set breakpoints
- Step through code
- Inspect variables
- Use debug console

#### Lab: Debugging Setup (45 min)

**Part 1: launch.json Explanation (15 min)**
- Open `.vscode/launch.json`
- Instructor explains each configuration
- Focus on "Python: FastAPI" config

**Part 2: First Debugging Session (30 min)**

Steps for students:
1. Open `src/main.py`
2. Set breakpoint in `greet_user` function (click left margin)
3. Press F5 (Start Debugging)
4. Make request: `curl localhost:8000/hello/Student`
5. VS Code stops at breakpoint
6. Hover over `name` variable
7. Step over (F10)
8. Step into (F11)
9. Continue (F5)

#### Advanced Debugging (45 min)

**Lab: Debug API Request**

Students debug this scenario:
1. Set breakpoint in `list_users` function
2. Start debugger
3. Navigate to http://localhost:8000/users
4. Inspect `pool`, `limit`, `offset` variables
5. Step through database query
6. Examine query results

#### Debugging Best Practices (30 min)

Discussion topics:
- When to use print vs debugger
- Conditional breakpoints
- Log points
- Debug console usage

**Exercise:** Students break the code on purpose, then debug to find the issue

---

### Session 4: Git Workflow (2 hours)

#### Learning Objectives
- Initialize Git repository
- Make commits
- Push to GitHub
- Handle multi-machine workflow

#### Lab: Git Basics (60 min)

**Part 1: Initial Commit (20 min)**
```bash
cd ~/projects/class-project
git init
git add .
git commit -m "Initial commit"
```

**Part 2: GitHub Setup (20 min)**
- Create repository on GitHub
- Add SSH key
- Link remote
```bash
git remote add origin git@github.com:username/class-project.git
git push -u origin main
```

**Part 3: Feature Branch Workflow (20 min)**
```bash
git checkout -b feature/add-greeting
# Make changes
git add src/main.py
git commit -m "feat: Add greeting endpoint"
git push origin feature/add-greeting
```

#### Lab: Multi-Machine Simulation (60 min)

**Scenario:** Student simulates switching computers

1. **On "Machine 1" (WSL):**
   ```bash
   # Make changes
   git add .
   git commit -m "Update greeting message"
   git push origin feature/add-greeting
   ```

2. **On "Machine 2" (Another WSL session):**
   ```bash
   # Simulate different machine
   cd ~/projects/class-project-machine2
   git clone <repo-url> .
   git checkout feature/add-greeting
   docker compose up -d
   # Verify changes work
   ```

3. **Practice Pre-Switch Checklist:**
   - Commit all changes
   - Push to remote
   - Stop containers
   - Document in notes

#### End of Day Project
Students must:
1. Create feature branch
2. Add custom endpoint
3. Commit and push
4. Show instructor on GitHub

---

## DAY 3: Database Integration & APIs

**Goal:** Students build a full CRUD API with database

### Session 1: Database Fundamentals (2 hours)

#### Learning Objectives
- Understand relational databases
- Write SQL queries
- Use PostgreSQL with Python
- Work with asyncpg

#### Database Concepts (45 min)

**Topics:**
1. Tables, rows, columns
2. Primary keys and foreign keys
3. Indexes and performance
4. ACID properties
5. Transactions

**Exercise:** Students design schema on paper for a todo app

#### SQL Crash Course (45 min)

Students practice SQL in pgAdmin or psql:

```sql
-- Connect to database
docker exec -it class-project-db psql -U postgres -d myapp

-- Basic queries
SELECT * FROM users;
SELECT * FROM projects WHERE status = 'active';
SELECT u.username, COUNT(p.id) as project_count
FROM users u
LEFT JOIN projects p ON u.id = p.owner_id
GROUP BY u.username;

-- Insertions
INSERT INTO users (username, email, password_hash)
VALUES ('newuser', 'new@example.com', 'hash123');
```

#### Database Initialization Review (30 min)

**Walkthrough: `docker/init-db/01-init.sql`**
- Line-by-line explanation
- Students annotate copy
- Discuss:
  - UUID vs auto-increment
  - Timestamps (created_at, updated_at)
  - Soft deletes
  - Indexes
  - Triggers

---

### Session 2: Building CRUD Endpoints (2 hours)

#### Learning Objectives
- Create POST endpoint
- Implement validation
- Handle errors properly
- Return appropriate status codes

#### Lab: Create User Endpoint (90 min)

Students implement together:

```python
@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user: UserCreate,
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """Create a new user"""
    try:
        async with pool.acquire() as conn:
            # Check if username exists
            existing = await conn.fetchval(
                "SELECT id FROM users WHERE username = $1",
                user.username
            )
            if existing:
                raise HTTPException(
                    status_code=400,
                    detail="Username already exists"
                )
            
            # Hash password
            password_hash = hash_password(user.password)
            
            # Insert user
            user_id = await conn.fetchval(
                """
                INSERT INTO users (username, email, password_hash, full_name)
                VALUES ($1, $2, $3, $4)
                RETURNING id
                """,
                user.username,
                user.email,
                password_hash,
                user.full_name
            )
            
            # Return created user
            return UserResponse(
                id=str(user_id),
                username=user.username,
                email=user.email,
                full_name=user.full_name,
                is_active=True,
                created_at=datetime.utcnow()
            )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to create user"
        )
```

**Teaching Points:**
- Pydantic validation
- Database transactions
- Error handling
- Status codes (201 for creation)
- Returning created resource

#### Lab: Update and Delete (30 min)

Students implement:
1. `PATCH /users/{id}` - Update user
2. `DELETE /users/{id}` - Soft delete user

---

### Session 3: Advanced API Features (2 hours)

#### Learning Objectives
- Implement pagination
- Add filtering and sorting
- Create complex queries
- Optimize database access

#### Lab: Pagination (45 min)

Enhance `/users` endpoint:

```python
@app.get("/users")
async def list_users(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    sort_by: str = Query("created_at", regex="^(username|email|created_at)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """List users with pagination and sorting"""
    query = f"""
        SELECT id, username, email, full_name, is_active, created_at
        FROM users
        WHERE deleted_at IS NULL
        ORDER BY {sort_by} {order}
        LIMIT $1 OFFSET $2
    """
    # ... implementation
```

**Teaching Points:**
- Query parameters
- Input validation with Query()
- SQL injection prevention
- Sort options

#### Lab: Filtering (45 min)

Add search capability:

```python
@app.get("/users/search")
async def search_users(
    q: str = Query(..., min_length=2),
    pool: asyncpg.Pool = Depends(get_db_pool)
):
    """Search users by username or email"""
    # Use ILIKE for case-insensitive search
    # ... implementation
```

#### Performance Discussion (30 min)

Topics:
- N+1 query problem
- Index usage
- Connection pooling
- Query optimization
- Caching strategies

---

### Session 4: Project Work (2 hours)

#### Independent Lab

**Assignment: Build a Complete Feature**

Students choose one:

**Option A: Tasks API**
- POST /tasks - Create task
- GET /tasks - List tasks (with filters)
- PATCH /tasks/{id} - Update task
- DELETE /tasks/{id} - Delete task

**Option B: Comments System**
- POST /projects/{id}/comments - Add comment
- GET /projects/{id}/comments - List comments
- DELETE /comments/{id} - Delete comment

**Requirements:**
- All CRUD operations
- Input validation
- Error handling
- Database integration
- Tests (at least 3)

#### Instructor Circulates
- One-on-one help
- Code reviews
- Debugging assistance

#### End of Day Demo
- Each student demos their feature (2 min)
- Peer feedback
- Instructor highlights best practices

---

## DAY 4: Testing & Code Quality

**Goal:** Students write comprehensive tests and improve code quality

### Session 1: Introduction to Testing (2 hours)

#### Learning Objectives
- Understand testing pyramid
- Write unit tests with pytest
- Mock external dependencies
- Achieve code coverage

#### Testing Concepts (45 min)

**Discussion Topics:**
1. Why test?
2. Types of tests (unit, integration, e2e)
3. Test-driven development (TDD)
4. When to write tests

**Exercise:** Students identify what to test in their code

#### pytest Basics (45 min)

**Live Coding Session:**

```python
# tests/test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string_methods():
    text = "hello"
    assert text.upper() == "HELLO"
    assert "ell" in text

# Run tests
# pytest tests/test_example.py -v
```

**Key Concepts:**
- Test functions start with `test_`
- Assertions
- Test discovery
- Verbose output (-v)

#### Test Structure (30 min)

**AAA Pattern:**
- Arrange (setup)
- Act (execute)
- Assert (verify)

Example:
```python
def test_create_user():
    # Arrange
    user_data = {"username": "test", "email": "test@example.com"}
    
    # Act
    response = client.post("/users", json=user_data)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["username"] == "test"
```

---

### Session 2: Testing FastAPI Endpoints (2 hours)

#### Learning Objectives
- Use TestClient
- Mock database calls
- Test different scenarios
- Handle fixtures

#### Lab: Test GET Endpoints (60 min)

Students write tests for `/users` endpoint:

```python
def test_list_users_returns_200(client):
    """Test successful user listing"""
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_users_pagination(client):
    """Test pagination parameters"""
    response = client.get("/users?limit=5&offset=10")
    assert response.status_code == 200
    # Additional assertions

def test_list_users_empty_database(client, mock_db):
    """Test when no users exist"""
    # Mock empty result
    response = client.get("/users")
    assert response.json() == []
```

#### Lab: Test POST Endpoints (60 min)

Students write tests for user creation:

```python
def test_create_user_success(client):
    """Test successful user creation"""
    user_data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "securepass123",
        "full_name": "New User"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"

def test_create_user_duplicate_username(client):
    """Test creating user with existing username"""
    # First creation
    user_data = {"username": "duplicate", "email": "test@example.com", "password": "pass123"}
    client.post("/users", json=user_data)
    
    # Second creation (should fail)
    response = client.post("/users", json=user_data)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_create_user_invalid_email(client):
    """Test validation for invalid email"""
    user_data = {"username": "test", "email": "notanemail", "password": "pass123"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 422  # Validation error
```

---

### Session 3: Mocking & Fixtures (2 hours)

#### Learning Objectives
- Create reusable fixtures
- Mock database connections
- Use pytest-mock
- Test async code

#### Lab: pytest Fixtures (60 min)

**Create test fixtures:**

```python
@pytest.fixture
def sample_user():
    """Provide sample user data"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "username": "testuser",
        "email": "test@example.com",
        "is_active": True,
        "created_at": datetime.utcnow()
    }

@pytest.fixture
def auth_headers():
    """Provide authentication headers"""
    token = create_test_token()
    return {"Authorization": f"Bearer {token}"}

# Use in tests
def test_with_fixture(client, sample_user):
    # Use sample_user data
    pass
```

#### Lab: Mocking Database (60 min)

**Mock database calls:**

```python
@pytest.fixture
def mock_db_pool():
    """Mock database pool"""
    pool = MagicMock()
    mock_conn = MagicMock()
    mock_conn.fetch = AsyncMock(return_value=[])
    pool.acquire.return_value.__aenter__.return_value = mock_conn
    return pool

def test_with_mocked_db(client, mock_db_pool):
    """Test using mocked database"""
    app.dependency_overrides[get_db_pool] = lambda: mock_db_pool
    
    response = client.get("/users")
    assert response.status_code == 200
    
    app.dependency_overrides.clear()
```

---

### Session 4: Code Coverage & Quality (2 hours)

#### Learning Objectives
- Generate coverage reports
- Identify untested code
- Use linters
- Format code automatically

#### Lab: Coverage Analysis (60 min)

**Run coverage:**
```bash
pytest --cov=src --cov-report=html --cov-report=term-missing
```

**Students:**
1. Run coverage
2. Review HTML report
3. Identify gaps
4. Write tests for uncovered code
5. Re-run until >80% coverage

#### Lab: Code Quality Tools (60 min)

**Black (formatter):**
```bash
black src/ tests/
```

**isort (import sorter):**
```bash
isort src/ tests/
```

**pylint (linter):**
```bash
pylint src/
```

**mypy (type checker):**
```bash
mypy src/
```

**Students:**
1. Run each tool
2. Fix issues
3. Commit formatted code

#### VS Code Integration

Configure auto-format on save:
```json
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

---

## DAY 5: Deployment & Best Practices

**Goal:** Students deploy their application and learn production practices

### Session 1: Production Configuration (2 hours)

#### Learning Objectives
- Understand dev vs production
- Manage environment variables
- Configure for security
- Use proper logging

#### Production vs Development (45 min)

**Key Differences:**

| Aspect | Development | Production |
|--------|------------|------------|
| Debug mode | ON | OFF |
| Auto-reload | ON | OFF |
| Logging | DEBUG | INFO/WARNING |
| Error details | Full stack traces | Generic messages |
| CORS | Allow all | Specific origins |
| Database | Local | Cloud/RDS |

#### Environment Variables (45 min)

**Lab: Create production .env:**

```bash
# .env.production
ENVIRONMENT=production
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://user:pass@prod-db:5432/myapp
SECRET_KEY=<strong-random-key>
CORS_ORIGINS=https://myapp.com,https://api.myapp.com
DEBUG=false
```

**Security Best Practices:**
- Never commit .env files
- Use secrets managers (AWS Secrets Manager, etc.)
- Rotate secrets regularly
- Use different credentials per environment

#### Logging Configuration (30 min)

**Production logging:**

```python
import logging
from python_json_logger import jsonlogger

# JSON logging for production
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)
```

---

### Session 2: Docker Production Build (2 hours)

#### Learning Objectives
- Build optimized images
- Use multi-stage builds
- Implement health checks
- Configure resource limits

#### Lab: Optimize Dockerfile (60 min)

**Review multi-stage build:**

```dockerfile
# Build stage
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim
COPY --from=builder /opt/venv /opt/venv
COPY src/ /app/src/
```

**Students measure:**
- Image size before optimization
- Build time
- Image size after optimization

#### Lab: Health Checks (30 min)

**Add to Dockerfile:**

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
```

**Test:**
```bash
docker ps  # Shows health status
docker inspect <container> | grep Health
```

#### Production docker-compose (30 min)

**Create docker-compose.prod.yml:**

```yaml
version: '3.8'

services:
  web:
    build: .
    restart: always
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
        reservations:
          cpus: '1.0'
          memory: 1G
    environment:
      - ENVIRONMENT=production
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

---

### Session 3: CI/CD Basics (2 hours)

#### Learning Objectives
- Understand CI/CD concepts
- Set up GitHub Actions
- Automate testing
- Deploy automatically

#### CI/CD Concepts (30 min)

**Discussion:**
- Continuous Integration
- Continuous Deployment
- Benefits and challenges
- Industry practices

#### Lab: GitHub Actions (90 min)

**Create `.github/workflows/test.yml`:**

```yaml
name: Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest --cov=src --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

**Students:**
1. Create workflow file
2. Commit and push
3. Watch action run on GitHub
4. Fix any failing tests

---

### Session 4: Final Project Presentations (2 hours)

#### Project Requirements

Each student presents:
1. **Application overview** (2 min)
   - What it does
   - Key features

2. **Code walkthrough** (3 min)
   - Show main.py
   - Explain one endpoint in detail
   - Demonstrate tests

3. **Live demo** (2 min)
   - Start containers
   - Show API docs
   - Make requests
   - Show database data

4. **Deployment** (2 min)
   - Production configuration
   - CI/CD pipeline
   - Future improvements

5. **Q&A** (1 min)

#### Evaluation Criteria

Students are evaluated on:
- [ ] Application runs successfully
- [ ] Has working CRUD endpoints
- [ ] Database integration working
- [ ] Tests achieve >80% coverage
- [ ] Code follows style guide
- [ ] Git history shows regular commits
- [ ] Can explain their code
- [ ] Proper error handling
- [ ] Documentation (README)

#### Peer Feedback

Each student provides:
- One thing done well
- One suggestion for improvement

---

## Course Materials Provided

### Pre-Course Checklist (Sent 1 Week Before)

Students receive:
- [ ] Hardware requirements document
- [ ] Pre-installation instructions
- [ ] Slack/Discord invite
- [ ] Syllabus
- [ ] Reading list

### Day 1 Materials

- [ ] COMPLETE_SETUP_GUIDE.md
- [ ] QUICK_START_CHECKLIST.md
- [ ] System architecture diagrams
- [ ] Glossary of terms
- [ ] Troubleshooting guide

### Day 2-5 Materials

- [ ] All code templates (Dockerfile, docker-compose.yml, etc.)
- [ ] Database init scripts
- [ ] Test examples
- [ ] Style guides
- [ ] Best practices document

### Post-Course Materials

- [ ] Certificate of completion
- [ ] LinkedIn endorsement
- [ ] Career resources
- [ ] Advanced topics roadmap
- [ ] Alumni network access

---

## Assessment Strategy

### Continuous Assessment (50%)

- **Daily check-ins** (10%): Students complete end-of-day checklist
- **Code commits** (15%): Regular, meaningful commits with good messages
- **Lab participation** (15%): Active engagement during hands-on sessions
- **Peer collaboration** (10%): Helping others, asking questions

### Final Project (50%)

- **Functionality** (20%): Application works as specified
- **Code quality** (15%): Clean, readable, well-structured
- **Tests** (10%): Comprehensive test coverage
- **Documentation** (5%): Clear README and code comments

---

## Teaching Resources

### Instructor Materials

**Daily Slide Decks:**
- Day 1: Introduction & Setup
- Day 2: VS Code & Development
- Day 3: Database & APIs
- Day 4: Testing & Quality
- Day 5: Deployment & Best Practices

**Live Coding Scripts:**
- Step-by-step instructions for each demo
- Expected student questions and answers
- Common pitfalls and how to address them

**Solution Repositories:**
- `day1-complete` branch
- `day2-complete` branch
- `day3-complete` branch
- `day4-complete` branch
- `day5-complete` branch

### Student Resources

**Reference Documentation:**
- WSL2 commands cheat sheet
- Docker commands cheat sheet
- Git workflow diagram
- PostgreSQL query reference
- pytest best practices

**Video Tutorials (Optional Homework):**
- Docker fundamentals (20 min)
- FastAPI crash course (30 min)
- pytest tutorial (25 min)
- Git branching strategies (15 min)

---

## Success Metrics

### Student Success Indicators

By end of course, 90% of students should:
- [ ] Successfully run containerized applications
- [ ] Write and debug Python code in containers
- [ ] Create RESTful APIs with database integration
- [ ] Write tests achieving >70% coverage
- [ ] Use Git for version control
- [ ] Understand Docker fundamentals

### Course Quality Metrics

- **Completion rate:** >85%
- **Student satisfaction:** >4.5/5
- **Job placement** (3 months): >60%
- **Skills retention** (6 months): >75%

---

## Troubleshooting Guide for Instructors

### Common Student Issues

#### Issue 1: WSL2 Won't Install
**Symptoms:** Error during WSL installation
**Solutions:**
1. Check Windows version (need 19041+)
2. Enable virtualization in BIOS
3. Run as administrator
4. Check Windows features: Virtual Machine Platform, WSL2

#### Issue 2: Docker Won't Start
**Symptoms:** "Cannot connect to Docker daemon"
**Solutions:**
1. Check systemd is running
2. Verify docker service: `sudo systemctl status docker`
3. Add user to docker group
4. Restart WSL

#### Issue 3: Out of Memory
**Symptoms:** System freezes, containers crash
**Solutions:**
1. Reduce WSL2 memory limit in .wslconfig
2. Reduce Docker memory limit
3. Stop unused containers
4. Close other applications

#### Issue 4: Port Already in Use
**Symptoms:** "Address already in use"
**Solutions:**
1. Check running containers: `docker ps`
2. Stop conflicting service
3. Change port mapping
4. Use `docker-compose down` first

---

## Alternative Delivery Options

### Self-Paced Online Course

**Structure:**
- 5 modules (corresponding to 5 days)
- Video lectures (15-20 min each)
- Interactive labs (30-45 min each)
- Quizzes after each module
- Final project submission

**Platform:** Udemy, Coursera, or custom LMS

**Timeline:** 4-6 weeks at student's pace

### Weekend Bootcamp

**Structure:**
- Saturday 9am-5pm: Days 1-2
- Sunday 9am-5pm: Days 3-5
- Compressed content
- More instructor-led demos
- Less independent work

**Best for:** Working professionals

### University Semester Course

**Structure:**
- 15 weeks (3 hours/week)
- Week 1-3: Environment setup
- Week 4-6: Development workflow
- Week 7-9: Database & APIs
- Week 10-12: Testing
- Week 13-15: Deployment & Projects

**Grading:**
- Homework assignments (40%)
- Midterm project (20%)
- Final project (30%)
- Participation (10%)

---

## Extension Topics (Advanced Course)

For students who complete the basic course:

### Week 2: Advanced Topics

**Day 6: Microservices Architecture**
- Service decomposition
- Inter-service communication
- API gateways
- Service discovery

**Day 7: Authentication & Authorization**
- JWT tokens
- OAuth2
- Role-based access control
- Security best practices

**Day 8: Performance Optimization**
- Database query optimization
- Caching strategies (Redis)
- Load balancing
- Horizontal scaling

**Day 9: Monitoring & Logging**
- Prometheus metrics
- Grafana dashboards
- Centralized logging (ELK stack)
- Error tracking (Sentry)

**Day 10: Cloud Deployment**
- AWS ECS/Fargate
- Google Cloud Run
- Kubernetes basics
- Infrastructure as Code (Terraform)

---

## Frequently Asked Questions

### For Students

**Q: Do I need a powerful computer?**
A: Minimum 8GB RAM, but 12GB+ recommended. Any modern processor works.

**Q: Can I use macOS or Linux?**
A: Yes! The course focuses on Docker, which works on all platforms. WSL2 is Windows-specific, but concepts apply everywhere.

**Q: What if I fall behind?**
A: Office hours daily, recorded sessions, peer study groups available.

**Q: Will this help me get a job?**
A: Yes! Containerization is used in 80%+ of tech companies. This is a highly marketable skill.

**Q: Do I get a certificate?**
A: Yes, certificate of completion provided after successful final project.

### For Instructors

**Q: How many students per class?**
A: Recommended 15-20 for hands-on support. Maximum 30 with teaching assistant.

**Q: What if students have different OS versions?**
A: Provide separate guides for Windows 10, 11, macOS, Linux. Focus on Docker as common ground.

**Q: How to handle slow learners?**
A: Pair programming, extra office hours, simplified track option, TA support.

**Q: Can this be taught remotely?**
A: Yes! Use Zoom, screen sharing, breakout rooms. Actually easier for troubleshooting (can see their screens).

---

## Conclusion

This curriculum provides a comprehensive, production-ready education in modern development practices. Students emerge with practical skills used daily by professional developers worldwide.

**Key Takeaways:**
- ✅ Hands-on from day 1
- ✅ Production-grade practices
- ✅ Real-world applications
- ✅ Portfolio-ready projects
- ✅ Industry-standard tools

**Next Steps:**
1. Customize for your audience
2. Set up instructor environment
3. Test all labs
4. Prepare support materials
5. Market course

**Success Formula:**
```
Practical Labs + Expert Instruction + Real Tools + Student Projects = Career-Ready Developers
```

---

## Appendix: Daily Time Breakdown

### Typical Day Schedule

```
09:00 - 09:15  Day Start / Q&A from previous day
09:15 - 10:45  Session 1 (Lecture + Demo)
10:45 - 11:00  Break
11:00 - 12:30  Session 2 (Hands-on Lab)
12:30 - 13:30  Lunch
13:30 - 15:00  Session 3 (Advanced Topics)
15:00 - 15:15  Break
15:15 - 16:45  Session 4 (Project Work)
16:45 - 17:00  Day Wrap-up / Exit Ticket
```

### Homework Expectations

- **Time:** 1-2 hours/evening
- **Purpose:** Reinforce daily learning
- **Format:** Complete unfinished labs, watch videos, reading
- **Submission:** Push code to GitHub, answer reflection questions

---

**Course Version:** 1.0  
**Last Updated:** January 2026  
**Maintained By:** Development Education Team  
**License:** Educational Use Only
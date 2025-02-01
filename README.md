# Web App Template

## Quick setup

Only quick setup will get you the fully correct template.
- `git clone` this repo.
- `rm -rf .git/`
- `git init`
- run `./setup.sh`
- `yarn dev` to run frontend
- `task dev:api` to run backend app (activate venv first)
- `task db:up` to run database
- `pre-commit install` to install pre-commit

## Git and VSCode

### Create git repo

```
$ mkdir my_project
$ cd my_project
$ git init
```

### VSCode Extensions

#### Frontend

- Javascript and Typescript Nightly - get the latest version of JS/TS intellisense
- Headwind - Sort Tailwind classes
- Tailwind CSS IntelliSense - IntelliSense plugin for Tailwind
- ESLint - JS/TS linter
- Stylelint - CSS linter
- Prettier - Code formatter for JS/TS/CSS/YAML

#### Backend

- Python / Pylance - Language support and language server
- Ruff - linter and formatter
- Docker - manage docker containers in vscode
- ES7+ - React/Redux/React-Native snippets
- Mypy - Type Checker
- YAML - YAML Language support

#### Misc

- Jupyter - support for jupyter notebooks

#### VSCode Settings

- Copy .vscode/settings.json
- This will turn on auto format on save
- This will set the default Python interpreter to the one in the venv
- This will add ./backend to the PYTHONPATH for Python tools like linters.

## Frontend

- Typescript: language
- ESLint: linting
- yarn: package manager
- Turbopack: bundler
- React + NextJS: frontend framework
- TailwindCSS: CSS framework

### Initialize next app

`$ yarn create next-app frontend --typescript`

```
✔ Would you like to use ESLint? Yes
✔ Would you like to use Tailwind CSS? Yes
✔ Would you like your code inside a `src/` directory? No
✔ Would you like to use App Router? (recommended) No
✔ Would you like to use Turbopack for `next dev`? Yes
✔ Would you like to customize the import alias (`@/*` by default)? No
```

### Run next app

```
$ yarn dev
```

## Backend

- Python: language
- pip/venv: virtual env, package manager
- ruff: linting
- pre-commit: pre-commit hooks
- loguru: logging
- FastAPI: web framework
- Pydantic V2: data validation
- SQLAlchemy 2.0: ORM
- PostgreSQL: relational database
- Alembic: database migrations
- Docker/Docker Compose: containerization
- pytest: unit testing

### Virtual Environment

```
$ mkdir backend
$ cd backend
$ pyenv local 3.12.8
$ pyenv exec python -m venv venv
$ source venv/bin/activate
```

- Copy `requirements.txt`
- Use `pip install -r requirements.txt`
- Copy `backend/.gitignore`
- Copy `backend/venv/lib/python3.12/site-packages/app.pth`. This adds backend/ to sys.path for all scripts using virtualenv.

### pre-commit/linting/formatting/type checking

- Copy `.pre-commit-config.yaml` (in root dir) (configures pre-commit to use ruff and mypy)
- Copy `pyproject.toml` (in backend/) (configures ruff)
- `pre-commit install` to install pre-commit
- Test by committing to git.

### Task

- Copy Taskfile.yml

### FastAPI

```
$ pip install fastapi uvicorn
```

- Copy app/
- Rough structure
```
  .
  └── app/
  ├── backend/ # Backend functionality and configs
  | ├── config.py # Configuration settings
  │ └── session.py # Database session manager
  ├── models/ # SQLAlchemy models
  │ ├── auth.py # Authentication models
  | ├── base.py # Base classes, mixins
  | └── ... # Other service models
  ├── routers/ # API routes
  | ├── auth.py # Authentication routers
  │ └── ... # Other service routers
  ├── schemas/ # Pydantic models
  | ├── auth.py  
  │ └── ...
  ├── services/ # Business logic
  | ├── auth.py # Create user, generate and verify tokens
  | ├── base.py # Base classes, mixins
  │ └── ...
  ├── cli.py # Command-line utilities
  ├── const.py # Constants
  ├── exc.py # Exception handlers
  └── main.py # Application runner
```

An API request will go through main.py -> routers/ -> schemas/ -> services/ -> models/ -> backend/

- .env file
  Copy .env file and populate with your own env var info. This can be used to store facts about the backend app as well as any API/DB secrets.

### PostgreSQL/Docker

```
$ docker compose up -d postgres
```

This will:

- Start a PostgreSQL container
- Create a volume for persistent data
- Expose port for the database
- Set up the database with credentials from .env
- If you need to choose a different port, you can change the port in the .env file. Make sure to also update the port in the Taskfile.yml file.

You can manage the database using these commands:

```
$ task db:up    # Start the database
$ task db:down  # Stop the database
$ task db:logs  # View database logs
```

### Alembic

- Use alembic to create your tables for the first time.

```
$ alembic init alembic --template async
$ modify alembic/env.py to have target_metadata = SQLModel.metadata
$ modify alembic.ini to not set sqlalchemy.url and set instead in alembic/env.py
$ alembic revision -m "create initial tables" # create migration script to create initial tables.
$ alembic upgrade head # do migration.
```

### Testing

- Copy tests/
- Run `pytest` to do testing.


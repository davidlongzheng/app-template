# How to create a web app

## Initial setup

### Create git repo
```
$ mkdir my_project
$ git init
```


## Frontend

- Typescript: language
- ESLint: linting
- yarn: package managemer
- Turbopack: bundler
- React + NextJS: frontend framework
- TailwindCSS: CSS framework

### Initialize next app
$ yarn create next-app frontend --typescript

✔ Would you like to use ESLint? … No / Yes
✔ Would you like to use Tailwind CSS? … No / Yes
✔ Would you like your code inside a `src/` directory? … No / Yes
✔ Would you like to use App Router? (recommended) … No / Yes
✔ Would you like to use Turbopack for `next dev`? … No / Yes
✔ Would you like to customize the import alias (`@/*` by default)? … No / Yes

### Run next app
$ yarn dev

## Backend

- Python: language
- pip/venv: virtual env, package manager
- flake8/bandit/isort/ruff: linting
- pre-commit: pre-commit hooks
- FastAPI: web framework
- Pydantic V2: data validation
- SQLAlchemy 2.0: ORM
- PostgreSQL: relational database
- Alembic: database migrations
- Docker: containerization
- Pytest: unit testing

### Virtual Environment

$ mkdir backend
$ cd backend
$ python -m venv .env
$ source .env/bin/activate

### Add pre-commit/linting

$ pip install pre-commit ruff bandit isort flake8
$ Copy .pre-commit-config.yml, pyproject.toml, .isort.cfg
$ pre-commit install


# How to create a web app

## Initial setup

### Create git repo

$ mkdir my_project
$ git init

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

- Code Spell Checker - spell checking
- Jupyter - support for jupyter notebooks


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
- ruff: linting
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
$ python -m venv venv
$ source venv/bin/activate
$ pip freeze > requirements.txt
- Use `pip install -r requirements.txt`

### Add pre-commit/linting

- Copy .pre-commit-config.yaml (configures pre-commit to use ruff) (in top-level dir)
- Copy pyproject.toml (configures ruff)
$ pip install pre-commit ruff
$ pre-commit install # to install pre-commit dependencies
Test by committing to git.

### Add FastAPI



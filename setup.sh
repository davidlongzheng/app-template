#!/bin/bash

set -euxo pipefail

cd frontend
yarn install
cd ..

cd backend
pyenv local 3.12.8
if [ ! -d "venv" ]; then
  pyenv exec python -m venv venv
fi
cp app.pth venv/lib/python3.12/site-packages/
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
alembic upgrade head
task db:seed

#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install -r backend/requirements.txt
fi
if [ ! -d frontend/dist ]; then
  npm --prefix frontend ci
  npm --prefix frontend run build
fi
export PYTHONPATH="$PWD/backend"
exec .venv/bin/python -m uvicorn recalllab.app:app --host 127.0.0.1 --port 8000

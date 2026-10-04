#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Run ./run.sh once first, or create .venv and install requirements.txt."
  exit 1
fi
exec .venv/bin/python scripts/train.py

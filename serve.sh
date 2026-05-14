#!/usr/bin/env bash
# macOS / Linux convenience wrapper for serve.py.
# Run with:  bash serve.sh
# or:        ./serve.sh   (after chmod +x serve.sh)

set -e
cd "$(dirname "$0")"
exec python3 serve.py

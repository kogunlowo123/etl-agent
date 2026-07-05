#!/bin/bash
set -euo pipefail
echo "Setting up ETL Agent..."
pip install -e ".[dev]"
echo "Setup complete!"

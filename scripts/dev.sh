#!/usr/bin/env bash
set -e

echo "🚀 Starting dev environment"

make doctor
make up
make wait

echo ""
echo "API ready:"
echo "  http://localhost:8000/docs"
echo ""
echo "Run tests:"
echo "  make test"

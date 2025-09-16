#!/bin/bash

set -e

echo "=== Current Directory ==="
pwd

echo "=== Directory Contents ==="
ls -l

echo "=== OS Information ==="
uname -a

echo "=== CPU Information ==="
cat /proc/cpuinfo | head -n 10

echo "=== Memory Information ==="
cat /proc/meminfo | head -n 10

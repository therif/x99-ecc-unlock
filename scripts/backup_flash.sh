#!/usr/bin/env bash
set -euo pipefail
FLASHROM=${FLASHROM:-flashrom}
OUT=${1:-spi-backup}
$FLASHROM -p internal -r "${OUT}-1.bin"
$FLASHROM -p internal -r "${OUT}-2.bin"
sha256sum "${OUT}-1.bin" "${OUT}-2.bin"
cmp "${OUT}-1.bin" "${OUT}-2.bin" && echo 'SPI READ STABLE'

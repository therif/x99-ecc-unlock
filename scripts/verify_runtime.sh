#!/usr/bin/env bash
set -u
echo '=== MCMTR ==='
setpci -d 8086:2fa8 7c.L
setpci -d 8086:2f68 7c.L
echo '=== EDAC ==='
journalctl -k -b | grep -iE 'EDAC|ECC|sbridge|machine check|hardware error' || true
echo '=== EDAC SYSFS ==='
find /sys/devices/system/edac/mc -maxdepth 3 -type f \( -name mc_name -o -name ce_count -o -name ue_count \) -print -exec cat {} \; 2>/dev/null
echo '=== SMBIOS ==='
dmidecode -t 16

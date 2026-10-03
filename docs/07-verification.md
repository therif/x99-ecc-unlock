# Verification
## MCMTR
```bash
setpci -d 8086:2fa8 7c.L
setpci -d 8086:2f68 7c.L
```
Before: `00050f00 / 00010f00`; after: `00050f04 / 00010f04`.

## EDAC
```bash
journalctl -k -b | grep -iE 'EDAC|ECC|sbridge|machine check|hardware error'
```
Success registered `Haswell SrcID#0_Ha#0` and `Haswell SrcID#0_Ha#1`.

## sysfs
```bash
find /sys/devices/system/edac/mc -maxdepth 3 -type f \
  \( -name mc_name -o -name ce_count -o -name ue_count \) \
  -print -exec cat {} \;
```
Immediately after successful boot CE=0 and UE=0 on both MCs.

## SMBIOS
`dmidecode -t 16` changed from `None` to `Multi-bit ECC`. EDAC/MCMTR are stronger evidence than SMBIOS alone.

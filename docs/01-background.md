# Background
The tested X99/C610 system has an ECC-capable Xeon and ECC DIMMs, but Linux originally reported:
```text
EDAC sbridge: CPU SrcID #0, Ha #0, Channel #1 has DIMMs, but ECC is disabled
EDAC sbridge: Failed to register device with error -19.
```
SMBIOS reported `Error Correction Type: None`. The goal was actual memory-controller ECC operation confirmed by Linux EDAC, not merely exposing a BIOS menu.

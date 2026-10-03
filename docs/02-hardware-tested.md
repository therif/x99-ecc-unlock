# Tested Hardware and Software
| Component | Verified value |
|---|---|
| Chipset | Intel C610/X99 (Wellsburg) |
| CPU | Intel Xeon E5-2698B v3 @ 2.00 GHz |
| CPUID | family 6, model 63/0x3F, stepping 2 |
| SPI | XMC XM25QH128C/XM25QH128D, 16 MiB |
| OS | Proxmox VE / Debian |
| Kernel | 7.0.14-20-pve during final verification |
| EDAC | `sb_edac` / sbridge |

Target PEIM: `UncoreInitPeim`, GUID `D71C8BA4-4AF2-4D0D-B1BA-F2409F0C20D3`.
Shared platform-info GUID: `1E2ACC41-E26A-483D-AFC7-A056C34E087B`.
This is not a generic all-X99 patch.

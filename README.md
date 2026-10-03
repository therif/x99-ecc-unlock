# X99 ECC Unlock

Experimental documentation and tooling for enabling functional ECC on a tested Intel X99/C610 firmware where firmware disabled ECC during memory initialization.

## Verified system
- Intel C610/X99 (Wellsburg)
- Intel Xeon E5-2698B v3, family 6, model 63 (0x3F), stepping 2
- XMC XM25QH128C/XM25QH128D, 16 MiB SPI
- Proxmox VE / Debian; kernel `7.0.14-20-pve` during final verification
- Target PEIM: `UncoreInitPeim`, GUID `D71C8BA4-4AF2-4D0D-B1BA-F2409F0C20D3`

## Verified result
Before: MCMTR `00050f00 / 00010f00`, EDAC reported `has DIMMs, but ECC is disabled`, SMBIOS reported `None`.

After the final patch and cold boot: MCMTR `00050f04 / 00010f04`; Linux `sb_edac` registered `Haswell SrcID#0_Ha#0` and `Haswell SrcID#0_Ha#1`; CE/UE counters appeared at 0; SMBIOS reported `Multi-bit ECC`.

## Root cause
IFR exposed `ECC Support` at `IntelSetup + 0x11FF` (`0=Disable, 1=Enable, 2=Auto`). Auto and Enable both initially set internal bit `0x00020000`, so changing Auto to Enable alone was insufficient.

Shared PEI platform-info GUID `1E2ACC41-E26A-483D-AFC7-A056C34E087B` contains platform class `0x13` at payload `+0x5E` on the tested firmware. `UncoreInitPeim` explicitly clears the ECC bit for platform classes `0x13/0x14`.

## Final patch set
1. ECC_MIX: tested full-SPI offset `0xE403F0`, `12 -> 16`.
2. Platform ECC gate: exact context change `74 04 -> EB 07`; see `reference/patch-map.md`.

The earlier `+0x2336C` forced-branch experiment is NOT part of the final solution; its `74 07` form must remain/restored.

No complete proprietary BIOS/SPI, ME dump, or board-specific NVRAM is included. Read `DISCLAIMER.md` and the full `docs/` before use.

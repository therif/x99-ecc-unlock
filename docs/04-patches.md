# Patch Details
## Patch A — ECC_MIX
Exact tested full-SPI image: offset `0xE403F0`, byte `12 -> 16`. Absolute offset is documentation only.

## Patch B — platform ECC gate
Match exactly inside `UncoreInitPeim`:
```text
8A 86 F2 46 04 00 3C 13 74 04 3C 14 75 03 21 56 58 8A 87 EF 11 00 00
```
Replace `74 04 -> EB 07`.

## Do NOT apply old +0x2336C experiment
Final firmware must contain:
```text
A9 00 04 00 00 74 07 C6 87 6C 33 02 00 00 F7 47 58 00 00 02 00
```
The temporary `74 07 -> EB 07` was not sufficient and was restored.

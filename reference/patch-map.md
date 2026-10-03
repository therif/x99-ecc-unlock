# Patch Map
ECC_MIX tested offset `0xE403F0`: `12 -> 16` (verify context first).

Platform gate original:
```text
8A 86 F2 46 04 00 3C 13 74 04 3C 14 75 03 21 56 58 8A 87 EF 11 00 00
```
Patched:
```text
8A 86 F2 46 04 00 3C 13 EB 07 3C 14 75 03 21 56 58 8A 87 EF 11 00 00
```
+2336C gate must remain original:
```text
A9 00 04 00 00 74 07 C6 87 6C 33 02 00 00 F7 47 58 00 00 02 00
```

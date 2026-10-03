# Reverse Engineering
## ECC Support
IFR exposed `ECC Support`, VarOffset `0x11FF`: Disable=0, Enable=1, Auto=2.
```asm
mov al,[edi+0x11ff]
mov edx,0xfffdffff
mov ecx,0x00020000
cmp al,2
je SET_ECC
cmp al,1
jne CLEAR_ECC
SET_ECC: or [esi+0x58],ecx
```
Auto and Enable both set `0x00020000`.

## Platform-specific clear
```asm
mov al,[esi+0x446f2]
cmp al,0x13
je CLEAR
cmp al,0x14
jne CONTINUE
CLEAR: and [esi+0x58],edx
```
`EDX=0xFFFDFFFF`, so classes `0x13/0x14` clear ECC.

## Platform record
GUID `1E2ACC41-E26A-483D-AFC7-A056C34E087B`; observed layout: record+0x08 GUID, record+0x18 payload. `PlatformInfo` builds payload, sets payload+0x5E=0x13 on the tested platform, and copies 0xCF bytes. `PlatformEarlyInit` and `UncoreInitPeim` consume it.

Changing the global class was rejected; the final patch bypasses only the ECC-specific clear.

## Abandoned +0x2336C experiment
A downstream forced branch did not enable ECC because the upstream ECC policy bit had already been cleared. It was restored in the final firmware.

## Runtime proof
MCMTR changed from `00050f00/00010f00` to `00050f04/00010f04`; EDAC then registered MC0/MC1 and SMBIOS reported Multi-bit ECC.

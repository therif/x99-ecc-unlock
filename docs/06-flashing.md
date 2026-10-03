# Flashing
Successful testing used flashrom v1.8.0.

Stable reads:
```bash
flashrom -p internal -r read1.bin
flashrom -p internal -r read2.bin
cmp read1.bin read2.bin && echo SPI_READ_STABLE
```
Prefer a fresh live SPI read as merge base to preserve current NVRAM/state.

Tested write:
```bash
flashrom -V -p internal --ifd -i bios -w candidate.bin
```
Require `VERIFIED.`. Then:
```bash
flashrom -p internal -r post-write.bin
sha256sum candidate.bin post-write.bin
cmp candidate.bin post-write.bin && echo FLASH_READBACK_IDENTICAL
```
Do not reboot after failed verification. Use a cold boot after successful readback.

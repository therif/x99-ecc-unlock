# flashrom Example
```bash
flashrom -p internal -r pre.bin
flashrom -V -p internal --ifd -i bios -w candidate.bin 2>&1 | tee flashrom-write.log
flashrom -p internal -r post.bin
sha256sum candidate.bin post.bin
cmp candidate.bin post.bin && echo FLASH_READBACK_IDENTICAL
```
Cold boot only after successful verification/readback.

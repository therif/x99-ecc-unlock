# Build Guide
1. Dump SPI twice and confirm identical reads.
2. Keep an untouched offline backup.
3. Extract `UncoreInitPeim`.
4. Verify signatures in your exact firmware.
5. Apply context-checked changes.
6. Replace only the PE32 body.
7. Re-extract and verify the embedded PE32 hash.
8. Compare the full image and understand every changed byte.

Use `python3 scripts/patch_uncore.py input-pe32.bin output-pe32.bin` for the platform-gate patch. ECC_MIX is deliberately not blindly applied by absolute offset.

# Technical Notes
- UncoreInitPeim GUID: `D71C8BA4-4AF2-4D0D-B1BA-F2409F0C20D3`
- Platform-info GUID: `1E2ACC41-E26A-483D-AFC7-A056C34E087B`
- ECC_MIX tested offset: `0xE403F0`
- old +2336C gate: around `0xE6D7A4`
- platform ECC gate: around `0xE8215A`

Final state: ECC_MIX enabled; +0x2336C hack restored; platform ECC clear bypassed.
Final verified live candidate/readback SHA256: `0fe467a36f8162208653095517107e84148268546f30b01d67841623b7c71aee` (historical reference only; binary not distributed).

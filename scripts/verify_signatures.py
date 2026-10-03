#!/usr/bin/env python3
from pathlib import Path
import sys
if len(sys.argv)!=2: raise SystemExit(f'usage: {sys.argv[0]} IMAGE')
b=Path(sys.argv[1]).read_bytes()
sigs={
 'platform-original':'8A 86 F2 46 04 00 3C 13 74 04 3C 14 75 03 21 56 58 8A 87 EF 11 00 00',
 'platform-patched':'8A 86 F2 46 04 00 3C 13 EB 07 3C 14 75 03 21 56 58 8A 87 EF 11 00 00',
 '2336c-original':'A9 00 04 00 00 74 07 C6 87 6C 33 02 00 00 F7 47 58 00 00 02 00',
 '2336c-experimental':'A9 00 04 00 00 EB 07 C6 87 6C 33 02 00 00 F7 47 58 00 00 02 00'}
for n,h in sigs.items():
 s=bytes.fromhex(h); hits=[]; p=0
 while True:
  p=b.find(s,p)
  if p<0: break
  hits.append(hex(p)); p+=1
 print(f'{n}: {hits}')

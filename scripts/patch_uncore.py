#!/usr/bin/env python3
from pathlib import Path
import sys
if len(sys.argv)!=3: raise SystemExit(f'usage: {sys.argv[0]} INPUT_PE32 OUTPUT_PE32')
src,dst=map(Path,sys.argv[1:]); b=bytearray(src.read_bytes())
old=bytes.fromhex('8A 86 F2 46 04 00 3C 13 74 04 3C 14 75 03 21 56 58 8A 87 EF 11 00 00')
new=bytes.fromhex('8A 86 F2 46 04 00 3C 13 EB 07 3C 14 75 03 21 56 58 8A 87 EF 11 00 00')
h=[]; p=0
while True:
 p=b.find(old,p)
 if p<0: break
 h.append(p); p+=1
print('hits:',[hex(x) for x in h])
if len(h)!=1: raise SystemExit('ABORT: expected exactly one signature')
o=h[0]; b[o:o+len(old)]=new; dst.write_bytes(b)
print('patched',dst,'at',hex(o+8))

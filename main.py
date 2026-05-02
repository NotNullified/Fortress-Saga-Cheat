import sys
import re
import json
import pymem
import pymem.process

PROCESS_NAME = 'Ld9boxHeadless.exe'
try:
    pm = pymem.Pymem(PROCESS_NAME)
    print(f'Attached to {PROCESS_NAME}')
except Exception as e:
    print(f'Error attaching to ldbox: {e}')
    sys.exit(1)

with open("all_sigs.json", "r") as f:
    SIGNATURES = json.load(f)

def aob_to_regex(pattern: str) -> bytes:
    parts = pattern.split()
    regex = b''

    for byte in parts:

        if byte == '??':
            regex += b'.'
        else:
            try:
                regex += re.escape(bytes([int(byte, 16)]))
            except:
                return regex
    return regex

def main():
    print("Script is running, be patient please ts written in python")
    for sig in SIGNATURES:
        AOB = aob_to_regex(sig[0])
        addr = pymem.pattern.pattern_scan_all(pm.process_handle, AOB)
        
        if addr:
            print(addr)
            print(f'AOB found at {hex(addr)}')
            
            
            lvl = pm.read_int(addr+4) # Add 4 to get 2nd byte in AOB (lvl)
            print(f'Current lvl: {lvl}, setting to {sig[1]}')
            pm.write_int(addr+4, sig[1])
        else:
            print('AOB not found, perhaps update broke script.')

    print("Script appears to have ran properly")
            

if __name__ == '__main__':
    main()
    sys.exit(0)
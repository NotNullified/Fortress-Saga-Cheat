# Convert a list of ints to a sig/AOB

sig_ints = [566226432, 30264, 0, 0, '??', '??', '??', '??', '??', '??', 1, 96]
AOB = ''

for byte in sig_ints:
    if byte == '??':
        AOB += '????????'
        continue
    little_byte = byte.to_bytes(4, byteorder='little') # convert to 4 byte little endian
    hex_str = little_byte.hex().upper()
    AOB += hex_str

AOB = ' '.join(AOB[i : i + 2] for i in range(0, len(AOB), 2)) #Insert space after every 2nd char

print(AOB)
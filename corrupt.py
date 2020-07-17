import sys
import magic
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} file.webm")
    exit()
file = sys.argv[1]
if magic.from_file(file) != 'WebM':
    print("File is not a WebM")
    exit()
f = open(file, 'rb+')
d = f.read()
o = d.find(b'\x2a\xd7\xb1') + 3
o = d.find(b'\x44\x89', o) + 2
f.seek(o + 2)
f.write(b'\x00')
f.close()
print("Done!")

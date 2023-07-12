# source: https://stackoverflow.com/a/48613256
import sys, hashlib

text = input('Enter something: ')
mode = input('Enter algorithm: ')
#assert list == __builtins__.list
#algs = list(hashlib.algorithms_available())
#if (mode in algs):
#    print(hashlib.mode(text.encode('utf-8')).hexdigest())
#else:
#    sys.exit(1)
#none of this code worked so only sha256 and md5. cry about it
if (mode == "sha256"):
    print(hashlib.sha256(text.encode('utf-8')).hexdigest())
    sys.exit(1)
if (mode == "md5"):
    print(hashlib.md5(text.encode('utf-8')).hexdigest())
    sys.exit(1)
else:
    sys.exit(2)

import os

# walk dir
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

# list file under
print(os.listdir('.'))

# get basename
print(os.path.basename('a/bb.ccc'))

# wildcard
import glob
for f in glob.glob("*.f"):
    print(f)

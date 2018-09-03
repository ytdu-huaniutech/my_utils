import os
import glob

# walk dir
print('walk dir:')
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

# list file under
print('list dir:', os.listdir('.'))

# get basename
print('basename of a/bb.ccc:', os.path.basename('a/bb.ccc'))

# wildcard
import glob
for f in glob.glob("*.*"):
    print('wildcard match *.*: ', f)

# test existence
print('f exists?', os.path.exists('f'))


# get best match files (files under dir | globbing | single file)
def best_match_files(file_name):
    if os.path.isdir(file_name):
        file_name = os.path(file_name, '*')
    return glob.glob(file_name)

from pathlib import Path

# absolute path
# c:\Program Files\Microsoft
# /usr/local/bin
# relative path

path = Path("ecommerce")
#  exists returns a boolean
print(path.exists())
# to make a directory
#print(path.mkdir())
# remove a directory by using rmdir
#print(path.rmdir())
# gets the files in the current directories, but not the directories
path = Path()
for file in path.glob('*.py'):
    print(file)

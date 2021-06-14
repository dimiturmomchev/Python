from pathlib import Path

# path = Path("emails")
# print(path.exists())           # check if this path exists
# print(path.mkdir())            # makes directory
# print(path.rmdir())            # delete directory

path = Path()
# print(path.glob("*.py"))  # search for directories "*.*" for all files "*.py" all py files "*.xml" all xml files # IN THE CURRENT DIRECTORY

for file in path.glob("*"):
    print(file)
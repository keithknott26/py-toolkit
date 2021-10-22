from pathlib import Path

print("Building a path to the README.md for pathlib sample")
p = Path(__file__)
# building a path is very intuitive
readme = p.cwd() / "samples/pathlib/README.md"
print(f"type: {type(readme)}")
print(f"string: {readme}")
print(f"is a file: {readme.is_file()}")
print(f"parts: {readme.parts}")
print(f"absolute: {readme.absolute}")
print(f"name, steam, suffix: {readme.name}, {readme.stem}, {readme.suffix}")
print(f"parent: {readme.parent}")

# create a directory and write a file there
# chaing the command to create directory
# you can use the path open method to open a file
directory_path = readme.parent.joinpath('hello')
directory_path.mkdir(exist_ok=True)
print(f"created directory {directory_path}")
file_to_write = directory_path / 'demo.out'
with open(file_to_write, 'w+') as f:
    f.write("Hello from python samples run\n")


# use glob to find only certain files
for p in directory_path.glob('*.out'):
    print(p)


def relative_to_absolute(relative_path, filename):
    """
    Example:
    relative_path = '../data'
    filename = 'filename.txt'
    relative_to_absolute('01_own_apps', '07_relative_to_absolute_path.py')
    Result:
    C:\LagunovProjects\Playground\01_own_apps\01_own_apps\07_relative_to_absolute_path.py
    """
    work_dir = Path(__file__).parent
    return (work_dir / relative_path / filename).resolve()

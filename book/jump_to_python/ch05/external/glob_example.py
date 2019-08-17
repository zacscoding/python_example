import glob

path_pattern = "./*.py"
files = glob.glob(path_pattern)
print(files)

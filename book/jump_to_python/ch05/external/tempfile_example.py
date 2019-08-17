import tempfile
import os

temp_file = tempfile.TemporaryFile()

print(">> temp file path : ", temp_file.name)
print(">> exist temp file : ", os.path.exists(temp_file.name))
temp_file.close()
print(">> exist temp file after close() : ", os.path.exists(temp_file.name))

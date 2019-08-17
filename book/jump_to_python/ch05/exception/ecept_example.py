f = open("not_exist_file", "r")
"""
Output :

Traceback (most recent call last):
  File "C:/git/zaccoding/python_example/book/jump_to_python/ch05/exception/ecept_example.py", line 1, in <module>
    f = open("not_exist_file", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'not_exist_file'
"""

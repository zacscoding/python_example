import os

print("---------------------------------------------")
print(">> display os.environ")
print(os.environ)

print("---------------------------------------------")
print(">> display os.environ['path']")
print(os.environ['path'])

print("---------------------------------------------")
print(">> display os.getcwd()")
print(os.getcwd())

print("---------------------------------------------")
print(">> display os.getcwg() after os.chdir('../')")
os.chdir('../')
print(os.getcwd())

print("---------------------------------------------")
print(">> display os.system('dir')")
os.system('dir')

print("---------------------------------------------")
print(">> display os.popen('dir') and upper()")
f = os.popen('dir')
print(str(f.read()).upper())

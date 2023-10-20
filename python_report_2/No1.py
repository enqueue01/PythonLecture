import os

dir = os.listdir('.')
for name in dir:
    if os.path.isdir(name):
        print(f"폴더 : {name}")
    else:
        print(f"파일 : {name}")
import os

for name in os.listdir('.'):
    if os.path.isdir(name):
        print(f"폴더 : {name}")
    else:
        print(f"파일 : {name}")
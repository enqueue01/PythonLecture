import os

for name in os.listdir('.'):
    print(f"폴더 : {name}" if os.path.isdir(name) else f"파일 : {name}")

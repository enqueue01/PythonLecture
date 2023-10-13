employee = {"홍길동", "이수지", "박상민", "강민우", "하누리"}
late = {"홍길동", "이수지", "박상민"}
absent = {"박상민", "하누리"}

print(*employee-late-absent)
print(*late&absent)
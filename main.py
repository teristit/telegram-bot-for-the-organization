def file_open(name):
    f = open(name, encoding="utf-8")
    f = f.read()
    return f

print(file_open('test.txt'))
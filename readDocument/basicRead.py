"""f = open("check.txt", "r")
print(f.read())

print()
f = open("check.txt", "w")
print("write")
f.write("hello how are you?")
f.close()

print("read update")
f = open("check.txt", "r")
print(f.read())"""

print()

f = open("check.txt", "a")
print("append")
f.write("what are you doing?")
f.close()

print("read update")
f = open("check.txt", "r")
# print(f.read())
print(f.readlines())

try:
    f = open("newFile.txt", "x")
    f.write("hello")
except FileExistsError:
    print("file already exist")
finally:
    f.close()

"""f = open("newFile.txt", "x")
f.write("hello")
f.close()"""
f = open('reading_file_example.txt')

print(f)

txt = f.read()
print(type(txt))
print(txt)
f.close()

f = open('reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

f = open('reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
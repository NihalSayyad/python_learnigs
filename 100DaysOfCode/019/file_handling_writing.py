with open('reading_file_example.txt', 'a') as f:
    f.write("\nThis text to be appended at the end")

with open('reading_file_example.txt')  as f:
    lines = f.read().splitlines()
    print(lines)

#This will create a new file and add the content to it
with open('writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

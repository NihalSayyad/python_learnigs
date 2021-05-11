with open('reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


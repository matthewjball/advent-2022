from dataclasses import dataclass

with open ('input.txt', 'r') as file:
    inputs = [str(i.replace('\n','')) for i in file.readlines()][1:]


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.directories = {}

    def total_size(self):
        size = 0
        for s in self.files.values():
            size += s
        for directory in self.directories.values():
            size += directory.total_size()
        return size

    def top(self):
        if self.parent is not None:
            return self.parent.top()
        else:
            return self

    def add_size_to_list(self, dictionary):
        dictionary[self.name] = self.total_size()
        for directory in self.directories.values():
            directory.add_size_to_list(dictionary)


curr_dir = Directory("root", None)

for line in inputs:
    if line == "$ cd ..":
        curr_dir = curr_dir.parent
    elif line[:4] == "$ cd":
        dir_name = line.split(" ")[2]
        curr_dir = curr_dir.directories[dir_name]
    elif line[:3] == "dir":
        dirname = line[4:]
        curr_dir.directories[dirname] = Directory(curr_dir.name + "/" + dirname, curr_dir)
    elif line == "$ ls":
        #ignore
        continue
    else:
        file_size = int(line.split(" ")[0])
        file_name = line.split(" ")[1]
        curr_dir.files[file_name] = file_size

top_level = curr_dir.top()


dirs = {}
top_level.add_size_to_list(dirs)

total = 0

for dirname, size in dirs.items():
    if size <= 100000:
        total += size

print(f"Part 1 answer: {total}")

space_to_free = 30000000 - (70000000 - top_level.total_size())
sorted_sizes = sorted(dirs.values())

for size in sorted_sizes:
    if size >= space_to_free:
        print(f"Part 2 answer: {size}")
        break

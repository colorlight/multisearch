import os

path = "./"
files = os.listdir(path)
right_files = [ ]
for file in files:
        if not os.path.isdir(file):
            f = open(path + '/' + file)
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str = str + line
            if (str.find('key1') != -1) and (str.find('key2') != -1):
                right_files.append(f)

for file in right_files:
    print(file.name)
print 'hello world'



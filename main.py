
import random
import os
# random.choice selects random element
# os.listdir lists in current directory
# filename=""
# # filter out directories
# while not os.path.isfile(filename):
#     filename=random.choice(os.listdir(directory_path))
# # with open(filename,'r') as file_obj:
# #     # do stuff with file

_files = os.listdir('.')
# print(_files)


_files.remove('README.md')
files=[file for file in _files if file.endswith(".md")]

number = random.randint(0, len(files) - 1)
file_ = files[number]

# with open(file_, 'w') as f:
#     f.write("foobar")

# print(os.getcwd())
print(file_)
os.system("rm  Today_Challenge.md")
os.system("cp {}  Today_Challenge.md".format(file_))
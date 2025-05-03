import os

# os.mkdir(r'first')
# os.mkdir(r'second')

for i in range(1, 3):
    with open(f'first\\test{i}.txt', 'w'):
        pass
    with open(f'second\\test{i}.txt', 'w'):
        pass


for root, directories, files in os.walk(r'./'):
    # print(root)
    # for directory in directories:
    #     print(directory)
    for file in files:
        print(file)
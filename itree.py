import os
import sys

file_tree = []
file_tree.append("📦" + " " + sys.argv[1])


for i, (root, dirs, files) in enumerate(os.walk(sys.argv[1])):
    if i == 0:
        for directory in dirs:
            file_tree.append("┣ 📂" + " " + directory)
        
        for file in files:
            file_tree.append("┣ 📄" + " " + file)

        file_tree[-1] = file_tree[-1].replace('┣', '┗')
    
    else:
        index_flag = 0
        root_partial = ''
        levels = len(root.split('\\'))
        for level in range(levels - 2):
            root_partial += "┃ "
        root_partial += '┣ 📂 '
        if root_partial + root.split('\\')[-1] in file_tree:
            index = file_tree.index(root_partial + root.split('\\')[-1])
        else:
            index = file_tree.index(root_partial.replace("┣ 📂", "┗ 📂") + root.split('\\')[-1])

        for directory in dirs:
            file_tree.insert(index + 1 ,root_partial.replace("┣ 📂", "┃") + "┣ 📂" + " " + directory)
            index += 1
            index_flag = 1
        
        for file in files:
            file_tree.insert(index + 1 ,root_partial.replace("┣ 📂", "┃") + "┣ 📄" + " " + file)
            index += 1
            index_flag = 1
        
        if index_flag == 1:
            file_tree[index] = file_tree[index].replace('┣ 📂', '┗ 📂')
            file_tree[index] = file_tree[index].replace('┣ 📄', '┗ 📄')

    
        # print(index)
        # print(root_partial)

for file in file_tree:
    print(file)
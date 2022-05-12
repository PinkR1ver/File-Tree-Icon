import os
import sys

base_path = sys.argv[-1]

file_tree = []
file_tree.append("📦" + " " + base_path)


# Command detection
if '-h' in sys.argv:
    skip_hidden = False
else:
    skip_hidden = True

if '-v' in sys.argv or '--version' in sys.argv:
    print('version 1.0')
    exit()

if '--help' in sys.argv:
    print("usage: python itree.py [argv] [root]")
    print("")
    print("itree is a tool to generate file tress with different stlyes very simply")
    print("")
    print("optional arguments:")
    print("")
    print("  -v, --version         Show the itree version number and exit")
    print("  --help                Show this help message and exit.")
    print("  -h                    Output hidden files and dirs")
    print("  -d, --depth [number]  set the depth we will show, default is 5")
    exit()

if '-d' in sys.argv or '--depth' in sys.argv:

    # check -d command

    if '-d' in sys.argv and '--depth' in sys.argv:
        print("You just need use \'-d\' or \'--depth\', don't need use both of them")
        exit()
    if '-d' in sys.argv:
        index = sys.argv.index('-d')
    else:
        index = sys.argv.index('--depth')
    
    # Get depth number

    if sys.argv[index + 1].isdigit():
        depth_bound = int(sys.argv[index + 1])
    else:
        print("-d or -depth should be follwed with number depth, use itree --help to check useage")
        exit()

else:
    depth_bound = 5
        

# Build File tree
for i, (root, dirs, files) in enumerate(os.walk(base_path)):

    ## Init Build in file tree depth 0
    if i == 0:
        for directory in dirs:
            if not skip_hidden or '.' not in directory[0]:
                file_tree.append("┣ 📂" + " " + directory)
            else:
                pass
        
        for file in files:
            if not skip_hidden or '.' not in file[0]:
                file_tree.append("┣ 📄" + " " + file)
            else:
                pass

        file_tree[-1] = file_tree[-1].replace('┣', '┗')

    else:

        ## index_flag is to check if the index is increasing, 
        ## if index increase,
        ## it means that the dir have sub dirs or files, 
        ## so need to replace the '┣' with '┗'

        index_flag = 0

        root_partial = ''

        depths = len(root.replace(base_path + '\\', '').replace(base_path, '').split('\\'))
        
        if depths >= depth_bound:
            continue
            
        for depth in range(depths - 1):
            root_partial += "┃ "
        root_partial += '┣ 📂 '

        if root_partial + root.split('\\')[-1] in file_tree:
            index = file_tree.index(root_partial + root.split('\\')[-1])
        elif root_partial.replace("┣ 📂", "┗ 📂") + root.split('\\')[-1] in file_tree:
            index = file_tree.index(root_partial.replace("┣ 📂", "┗ 📂") + root.split('\\')[-1])
        else:
            continue

        for directory in dirs:
            if not skip_hidden or '.' not in directory[0]:
                file_tree.insert(index + 1 ,root_partial.replace("┣ 📂", "┃") + "┣ 📂" + " " + directory)
                index += 1
                index_flag = 1
            else:
                pass
        
        for file in files:
            if not skip_hidden or '.' not in file[0]:
                file_tree.insert(index + 1 ,root_partial.replace("┣ 📂", "┃") + "┣ 📄" + " " + file)
                index += 1
                index_flag = 1
            else:
                pass
        
        if index_flag == 1:
            file_tree[index] = file_tree[index].replace('┣ 📂', '┗ 📂')
            file_tree[index] = file_tree[index].replace('┣ 📄', '┗ 📄')

    
        # print(index)
        # print(root_partial)

for file in file_tree:
    print(file)
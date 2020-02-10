def searching(string):
    l = len(string)
    with open('./a-z/%s.txt' %string[0], 'r', encoding = 'utf-8') as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            elif line[0] == string:
                break

        if not line:
            print("There is no such a word. Would you like to add one?")
            add = input('y/n ')
            if add == 'y':
                adding(string)
        else:
            print(' '.join(line))
    return

def adding(string):
    check = ''
    while check != 'y':
        print('Description of the vocabulary:')
        des = input()
        print('..........')
        print('Please double check!')
        print('Vocabulary: %s' %string)
        print('Description: %s' %des)
        print('..........')
        check = input("Correct?(y/~). If you don't want to add, please type 'q'\n")
        if check == 'q':
             break

    if check == 'y':
        with open('./a-z/%s.txt' %string[0], 'a', encoding = 'utf-8') as f:
            f.write('%s %s\n' %(string, des))
        print('New vocabulary is added!')
    
    return

def modifying(string):
    with open('./a-z/%s.txt' %string[0], 'r', encoding = 'utf-8') as f:
        # search the location
        counter = 0
        while True:
            line = f.readline().split()
            if not line:
                break
            elif line[0] == string:
                break
            counter += 1

        if not line:
            print("There is no such a word. Would you like to add one?")
            add = input('y/n ')
            if add == 'y':
                adding(string)
                return
        else:
            # modify the description
            print('Now:', end = ' ')
            print(' '.join(line))
            check = ''
            while check != 'y':
                print('Please type the new description.')
                mod = input()
                check = input("Correct?(y/~). If you don't want to modify, please type 'q'\n")
                if check == 'q':
                    break
        
    if check == 'y':
        with open('./a-z/%s.txt' %string[0], 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
            lines[counter] = '%s %s\n' %(string, mod)

        with open('./a-z/%s.txt' %string[0], 'w', encoding = 'utf-8') as f:
            f.writelines(lines)
                
        print('New: %s %s' %(string, mod))
    return

for i in range(97, 123):
    with open('./a-z/%s.txt' %chr(i), 'w', encoding = 'utf-8') as f:
        print(i)

print('done')

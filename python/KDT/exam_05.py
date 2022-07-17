with open({students.txt}, 'r', encoding = 'utf-8') as f :

    text = f.read()

    print(text, type(text))

    names = text.split()
    cnt = 0

    for name in names:
        if name[0] == '김':
            cnt += 1

    print(cnt)
for a in range(1,9):
    f = open(f"{a}차시.txt", 'w', encoding='UTF-8')
    f.close

    f = open(f"{a}차시.txt", 'a', encoding='UTF-8')
    for i in range(1,100):
        text = str(input(f'{a}차시 text 작성 :'))
        if text == 'e':
            break
        f.write(text + '\n')
    f.close

print('done')
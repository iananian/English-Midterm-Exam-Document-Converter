for i in range(1,26):
    f = open(f"{i}차시.txt", 'r', encoding='UTF-8')
    data = f.read()
    data = data.replace('\n\n', '\n')
    data = data.replace('\n', ' ')
    data = data.replace('.', '. \n\n')
    data = data.replace('\n ', '\n')
    data = data.replace('\n\n” ', '” \n\n')
    script = data
    f.close

    f = open(f"{i}차시.txt", 'w', encoding='UTF-8')
    f.write(script)
    f.close

print('done')
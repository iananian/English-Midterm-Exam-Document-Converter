f = open(f"총합.txt", 'w', encoding='UTF-8')
f.write('영어 학습지 총정리\n\n\n')
f.close

for i in range(1,26):
    f = open(f"{i}차시.txt", 'r', encoding='UTF-8')
    data = f.read()
    script = data
    f.close

    f = open(f"총합.txt", 'a', encoding='UTF-8')
    f.write(f"{i}차시\n\n\n")
    f.write(script)
    f.close

print('done')
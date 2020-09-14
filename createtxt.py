'''
按照数字生成文件名
'''
with open("main.txt", 'w') as f:
    for i in range(1, 43):
        f.write(str(i).zfill(5) + '\n')
f.close()

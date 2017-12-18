def count(obj):
    obj = obj.replace(" ", "")
    if len(obj) < 3:
        return False
    else:
        b = {}
        for i in obj:
            if i in b:
                b[i] = b[i] + 1
                # 判断是否长度为3且是数字或字母
                if b[i] == 3 and i.isalpha():
                    print(i)
                    return False
            else:
                b[i] = 1
    return False
# 输入需要处理的字符串
a = input()
# 进行处理 首次出现三次的英文字符
count(a)

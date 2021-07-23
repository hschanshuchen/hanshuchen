
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
def getChrNum(str):
    alph=0
    space=0
    digit=0
    others=0
    for i in str:
        if i.isalpha():
            alph+=1
        elif i.isspace():
            space+=1
        elif i.isdigit():
            digit+=1
        else:
            others+=1
    print("英文字符有%s个，空格有%s个，数字有%s个，其他字符有%s个"%(alph,space,digit,others))




if __name__=="__main__":
    getChrNum("das  451908__")
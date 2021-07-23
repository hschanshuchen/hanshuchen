



with open("test01.txt",encoding="UTF-8") as f1,open("test02.txt",encoding="UTF-8") as f2,open("test03.txt",'w',encoding="UTF-8") as f3:


    text01 = f1.read()
    f1.close()

    text02 = f2.read()
    f2.close()


    f3.write(text01+text02)
    f3.close()


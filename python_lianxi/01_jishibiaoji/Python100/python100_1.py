
## 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

'''
获取两个数之间的数字组成的不相等的三位数的个数
'''

class py01:
    def getNumber(self,n,m):
        count=0
        for i in range(n,m):
            for j in range(n, m):
                for k in range(n, m):
                    if (i!=j) and (k!=j) and (i!=k):
                        count=count+1
        return count



if __name__=='__main__':
        py=py01()
        num=py.getNumber(1,5)
        print(num)











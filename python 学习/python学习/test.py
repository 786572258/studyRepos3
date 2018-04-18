class Person:
    def __init__(self):
        print("这是构造方法")

    def show(self):
        print("这是show方法")
        return 1

    def testWhile(self, num):
        count = 0
        while(count < int(num)):
            print(count)
            count = count + 1

class stack:
    def __init__(self, max, ):
        self.__max=max
        self.__element=[0]*self.__max
        self.__top=-1

    def is_Full(self):
        return self.__max-1==self.__top

    def is_Empty(self):
        return self.__top==-1

    def push(self,num):
        if self.is_Full():
            print("stack is full")
        else:
            self.__top += 1
            self.__element[self.__top] = num


    def pop(self):
        if(self.is_Empty()):
            print("stack is empty")

        else:
            a=self.__element[self.__top]
            self.__top-=1
            return a

    def display(self):
        for i in range(self.__top, -1, -1):
            print(self.__element[i], end=' \n')
        print()

stack1=stack(5)
stack1.push(1)
stack1.push(2)
stack1.display()
a=stack1.pop()
print("pop element ",+a)
stack1.display()




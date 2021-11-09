class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linklist():
    def __init__(self ,head):
        self.head=None

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count


    def insert_at(self,data,index):
        if index <= 0 or index >= self.get_length():
            print("inalid inndex")

        elif index==0:
            new_node=Node(data)
            self.head=new_node
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    new_node=Node(data,itr.next)
                    itr.next=new_node

if __name__=='__main__':
    l=linklist()
    l.get_length()
    l.insert_at(1,0)

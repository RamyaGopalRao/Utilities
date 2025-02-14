class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):

        if not self.head:
            self.head=Node(data)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data)

    def insertat(self,index,data):
        if(index==0):
            if(self.head is None):
                self.head=Node(data)
                return
            else:
                new_node=Node(data)
                new_node.next=self.head
                self.head=new_node
                return
        else:
            itr=self.head
            cnt=0
            while(itr and cnt<=index):
                if(cnt==index-1):
                    print(cnt,index)
                    new_node=Node(data)
                    prev=itr.next
                    itr.next=new_node
                    new_node.next=prev
                cnt=cnt+1
                itr=itr.next
    def remove(self,index):
        if(index==0):
            if(self.head is None):
                return
            else:
                self.head=self.head.next
                return
        else:
            cnt=0
            itr=self.head
            while(itr and cnt<=index):
                if(cnt==index-1):
                    itr.next=itr.next.next
                cnt+=1
    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            popped_value = self.head.data
            self.head = None
            return popped_value
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        popped_value = second_last.next.data
        second_last.next = None
        return popped_value
    def sort(self):
        if(self.head ==None):
            return
        else:
            current=self.head
            nextnode=current.next
            while(nextnode):
                if(current.data>nextnode.data):
                    current.data,nextnode.data=nextnode.data,current.data
                    current=nextnode
                    nextnode=nextnode.next
                    continue




    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll=Linkedlist()
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(1)
ll.append(7)
ll.append(27)
ll.append(17)
ll.append(57)
ll.append(67)
ll.append(78)
print(ll.print_list())
ll.sort()
print(ll.print_list())



ll.insertat(2,9)
ll.print_list()

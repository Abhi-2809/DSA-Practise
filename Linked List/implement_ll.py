class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            #print(itr.val)
            llstr += str(itr.val)+' --> ' if itr.next else str(itr.val)
            itr = itr.next
        print(llstr)



    def get(self, index: int) -> int:

        if index<0:
          return -1

        count=0
        itr = self.head

        while count>=0:
          if count==index:
            return itr.val
            break
          count+=1
          itr = itr.next
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        
        if self.head is None:
          new_node = Node(val,None)
          self.head = new_node
        
        itr = self.head

        while itr.next:
          itr = itr.next
        new_node = Node(val,None)
        itr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        if index<0 :
          return -1

        if index==0:
          self.addAtHead(val)

        itr = self.head
        count = 0

        while itr:
          if count==index-1:
            new_node = Node(val,itr.next)
            itr.next = new_node
            break

          count+=1
          itr = itr.next
        

    def deleteAtIndex(self, index: int) -> None:

      if self.head is None or index<0:
        return -1

      if index==0:
        self.head = self.head.next
        return
  
      
      itr = self.head
      count = 0

      while itr:
        if count==index-1:
          itr.next = itr.next.next
          break
        count+=1
        itr = itr.next

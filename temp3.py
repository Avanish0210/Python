class Stack:
    def __init__(self):
        self.maxsize = 5
        self.size = 0
        self.st = []

    def isfull(self):
        if self.size==self.maxsize:
            return True
        return False
    
    def isempty(self):
        if self.size==[]:
            return True
        return False
    
    def push(self):
        if self.isfull()==False:
            self.size+=1
            self.st.append(item)

    def push(self):
        if self.isempty()==False:
            self.size-=1
            return self.st.pop()
        
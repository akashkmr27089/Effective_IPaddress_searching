class dfa_node:
    def __init__(self):
        self.trans = [[]]
        self.accept = False
    def insert_node(self,data):
        self.trans[0].append(data)
        self.trans.append(dfa_node())
    def insert(self,data):
        print(data)
        if len(data) == 0:
            self.accept = True
            return
        if data[0] in self.trans[0]:
            if len(data) > 0:
                self.trans[self.trans[0].index(data[0])+1].insert(data[1:])
            else:
                self.accept = True
        else:
            self.insert_node(data[0])
            if len(data[1:])!=0:
                self.trans[-1].insert(data[1:])
            else:
                self.accept = True
    def verify(self,data):
        # print(self.trans)
        # print(data)
        # print(self.accept)
        if len(data) == 1:
            print("dotmat", self.accept)
            return self.accept
        else:
            return self.trans[self.trans[0].index(data[0])+1].verify(data[1:])
    
a = dfa_node()
print(" Objects :")
a.insert([1,2,3,4,5])
print(a.trans)
print("verifing :")
print(a.verify([1,2,3,4,5]))
a.insert([2,3,4])
print(a.verify([2,3,4,5]))

        
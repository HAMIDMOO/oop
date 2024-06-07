# its bether to not use ("_")  & begin class name with capital word

class Hamid:

    def __init__(self, x) -> None:
        self.x= x
        n= []
        self.n=[]
        for i in range(x):
            n.append(input("Ener the {}th number : ".format(i+1)))
        self.n = n    

    def max(self):
        max_lst=[]
        max= self.n[0]
        for i in (self.n):

            if len(i)>= len(max) and i not in max_lst:
                max_lst= max_lst+[i]        
        return max_lst
    

    def min(self):
        min_lst=[]
        min= self.n[0]
        for i in (self.n):
            if len(i)== len(min):
                min_lst= min_lst + [i]
            elif len(i)< len(min):
                min_lst = [i]
                min = i

        return min_lst



    



p1= Hamid(4)
print(p1.min())

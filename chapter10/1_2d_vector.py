class D2vector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'

class D3vector(D2vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'

v2d = D2vector(1,2)
v3d = D3vector(2,3,4)
print(v2d)
print(v3d)
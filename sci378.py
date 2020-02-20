print("Version 0.0.1")

from matplotlib import rcParams
from numpy import array

fontsize=20

rcParams['font.size']=fontsize
rcParams['font.family']='sans-serif'

rcParams['axes.labelsize']=fontsize
rcParams['axes.titlesize']=fontsize
rcParams['xtick.labelsize']=fontsize
rcParams['ytick.labelsize']=fontsize
rcParams['legend.fontsize']=fontsize

rcParams['figure.figsize']=(12,8)

rcParams['axes.grid']=True

class Storage(object):
    def __init__(self):
        self.data=[]
    
    def __add__(self,other):
        s=Storage()
        s+=other
        return s
        
    def __iadd__(self,other):
        self.append(*other)
        return self
        
    def append(self,*args):
        if not self.data:
            for arg in args:
                self.data.append([arg])

        else:
            for d,a in zip(self.data,args):
                d.append(a)
       
    def arrays(self):
        for i in range(len(self.data)):
            self.data[i]=array(self.data[i])

        ret=tuple(self.data)
        if len(ret)==1:
            return ret[0]
        else:
            return ret

    def __array__(self):
        from numpy import vstack
        return vstack(self.arrays())

    
    

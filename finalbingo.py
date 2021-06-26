from BINGO import *

class bingo1:
    
    def __init__(self):
        
        self.q=bingo()
        self.r=bingo()
    
    
    def intelligence(self):
        self.q.count()
        self.r.count()
        z=max(self.r.c)
        if(z==5):
            for i in range(12):
                if(self.r.c[i]==5):
                    self.r.c[i]=0
                
    
        i=self.r.c.index(max(self.r.c))
        
        if(i<=4):
            for i in range(5):
                
                for j in range(5):
                    if(self.r.a[i][j]!='x'):
                        return(self.r.a[i][j])
        if(i+5<=9):
            for i in range(5):
                for j in range(5):
                    if(self.r.a[j][i]!='x'):
                    
                        return(self.r.a[j][i])
        if(i==10):
            
            for j in range(5):
                if(self.r.a[j][j]!='x'):
                    return(self.r.a[j][j])
        if(i==11):
            for j in range(5):
                if(self.r.a[j][4-j]!='x'):
                    return(self.r.a[j][4-j])
        
        for i in range(5):
            
            if(self.r.a[i][i]!='x'):
                return(self.r.a[i][i])
            elif(self.r.a[i][4-i]!='x'):
                return(self.r.a[i][4-i])
        
        for i in range(5):
            
            for j in range(5):
                if(self.r.a[i][j]!='x'):
                    return(self.r.a[i][j])
    def judge(self):
        p=0
        k=0
        for i in range(12):
            if(self.r.c[i]==5):
                p+=1
        for i in range(12):
            
            if(self.q.c[i]==5):
                
                k+=1
        
        '''print("p: ",p)
        print("k: ",k)'''
        if(p==5):
            return(1)
        if(k==5):
            return(2)
        
        if(p==5 and k==5):
            return(0)
    def play(self):
        
        n=0
        self.q.grid()#player1
        self.r.grid()#computer
        
        while(1):
            
            if(n%2==0):
                
            
                p1=int(input("hey enter your number"))
                for i in range(5):
                    for j in range(5):
                        if(self.q.a[i][j]==p1):
                            self.q.a[i][j]='x'
                        elif(self.r.a[i][j]==p1):
                            self.r.a[i][j]='x'
                self.q.display()
                self.q.count()
                self.r.count()
            
            
            
            
            else:
                
                
                
                v=self.intelligence()
                print("computer choose",v)
            
                for i in range(5):
                    for j in range(5):
                        if(self.q.a[i][j]==v):
                            self.q.a[i][j]='x'
                        elif(self.r.a[i][j]==v):
                            self.r.a[i][j]='x'
                self.q.display()
            self.q.count()
            self.r.count()
            if(1):
                g=self.judge()
                
                if(g==1):
                    print("hey computer you won hurrah")
                    self.r.display()
                    break
                elif(g==2):
                    print("hey player you won wow")
                    self.r.display()
                    break
                elif(g==0):
                    print("ki labh holo khele dujonei mor")
                    break
            n+=1
        
        
w=bingo1()
   
w.play()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
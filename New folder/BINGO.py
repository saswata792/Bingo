import random as rdm

class bingo:
    def grid(self):
        a=[]
        self.a=a
        e=[]
        
        
        
        for i in range(5):
            j=0
            b=[]
            while(j<5):
                p=rdm.randint(1,25)
                
                if p not in e:
                    e.append(p)
                    b.append(p)
                    j+=1
            self.a.append(b)
        
    def display(self):
        
        for i in range(5):
            for j in range(5):
                print(self.a[i][j],end="\t")
            print()
    def count(self):
        #row
        c=[0,0,0,0,0,0,0,0,0,0,0,0]
        self.c=c
        for i in range(5):
            for j in range(5):
                if(self.a[i][j]=='x'):
                    
                    self.c[i]+=1
                
        #coloumns
        for i in range(5):
            for j in range(5):
                if(self.a[j][i]=='x'):
                    self.c[i+5]+=1
                
        #diagonal
        for i in range(5):
            if(self.a[i][i]=='x'):
                self.c[10]+=1
            
        #off diagonal
        for i in range(5):
            if(self.a[i][4-i]=='x'):
                self.c[11]+=1
    '''def replace(self):
        for i in range(5):
            for j in range(5):
                if(self.a[i][j]==p and self.a[i][j]!='x'):
                    self.a[i][j]='x'
                else:
                    print("number is already marked")'''
                    


    

        
def kovanci(sez):
    
    slovar={}
    
    def F(sez,i=0,j=0):
        n=len(sez)
        if i>=n:
            return 0   
        else:
            if (i,j) not in slovar:
                slovar[(i,j)]=max(F(sez,i+1,j),F(sez,i+1,j+1))+sez[i][j]
            return slovar[(i,j)]
        
    return F(sez)

def kovanci_nad(sez):
    
    slovar={}
    
    def F(sez,i=0,j=0):
        n=len(sez)
        if i>=n:
            return (0,"" )  
        
        if i==n-1:
            return(sez[i][j],"")
        
        else:
            if (i,j) not in slovar:
                v1=F(sez,i+1,j)
                v2=F(sez,i+1,j+1)
                if v1>v2:
                    slovar[(i,j)]=(v1[0]+sez[i][j],"L"+v1[1])
                else:
                    slovar[(i,j)]=(v2[0]+sez[i][j],"D"+v2[1])
                
            return slovar[(i,j)]
        
    return F(sez)

print(kovanci_nad([[10], [5, 8], [12, 6, 5],[4,7,10,12]]))
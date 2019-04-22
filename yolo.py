def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
  
def table(u):
        u1=[]
        f=[]
        k=1
        for i in range(len(u)):
            j3=[0]*(max(all_minterm)+1)
            k=0
            if(len(u)>0):
                while(k!=len(u[i][0])):
                    j3[u[i][0][k]]=+1
                    k=k+1
                u1.append([u[i][0],j3])
                #print(u1)
                f=[]
                for j in range(len(j3)):
                    sum1=0
                    for i in range(len(u1)):
                        sum1=sum1+u1[i][1][j]
                    f.append(sum1)
        return(f)
def remove(duplicate):
    final_list=[]
    for i in range(len(duplicate)):
        if duplicate[i] not in final_list :
            final_list.append(duplicate[i])
    return final_list

g3=[]
def pairs(ge,r2):
        r=0
        
        g3=[]
        for i in range(len(ge)):
            k=i+1
        
            g2=[]
            while (k!=len(ge)):
                if(ge[k][2] - ge[i][2]==1):
                    for bv in range(len(ge[i][1])):
                        if((ge[i][1][bv]) != (ge[k][1][bv])):
                            g2.append(bv)
                            
                    if(len(g2)==1):
                        str3=ge[i][1][:(g2[0])]+'x'+ge[i][1][(g2[0]+1):]
                        g3.append([[ge[i][0],ge[k][0]],str3,ge[i][2]])
                        r=r+1
                g2=[]
                k=k+1
        d=[]
        if(r2>1):
            for i in range(len(g3)):
                for j in range(len(g3[i][0])):
                    d=d+g3[i][0][j]
                g3[i][0]=d
                d=[]
            for i in range(len(g3)):
                 g3[i][0].sort() 
                 
            g3=(remove(g3))
     
                
        return(g3,r)


def count(a): 
     a=bin(a)[2:]
     return (a.count('1'))


def insertionSort(arr,aux, n): 
    for i in range(1,n,1): 
        key1 = aux[i] 
        key2 = arr[i] 
        j = i-1
        while (j >= 0 and aux[j] < key1): 
            aux[j+1] = aux[j] 
            arr[j+1] = arr[j] 
            j = j-1
        aux[j+1] = key1 
        arr[j+1] = key2 

def sort(arr, n): 
    aux = [0 for i in range(n)] 
    for i in range(0,n,1): 
        aux[i] = count(arr[i]) 
    insertionSort(arr, aux, n) 

g=0
def binar(arr,len_all):
  
    for i in range(len_all):
        x=g-len(l[i][1])
        str1='0'*x
        w.append([arr[i],str1+l[i][1],])
        
        
def  countsetbits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count     
    

#*************input********

all_minterm=[0,1,2]
len_all=len(all_minterm)
if(len(all_minterm)!=0):
    sort(all_minterm,len_all) 
    all_minterm=all_minterm[::-1]
    l=[]
    r=[]
    w=[]
    for i in range(len_all):
        l.append([all_minterm[i],bin(all_minterm[i])[2:]])
        r.append(len(l[i][1]))
    g=max(r)
    binar(all_minterm,len_all)
    #print(w)
    q=[]
    for i in range(len(w)):
        q.append([w[i][0],w[i][1],countsetbits(w[i][0])])
        
    #print(q)
    x1=[]
    x1.append(q)
    x,y= pairs(q,1) 
    if(len(x)>0):
        x1.append(x)
    #print(x) 
    
    while True :
        u=x
        r=1
        
        x,y=pairs(x,2)
        if(len(x)>0):
            x1.append(x)
           
        #print(u)
        
        if (y==0):
            break
    print(x1)
    f=table(u)
    if(len(u)==0):
        f=[0]*(max(all_minterm)+1)
        for i in range(len(all_minterm)):
            f[all_minterm[i]]=1
    
    
   
    
    
    
    
    p=[]
    ans=[]
    s=[]
    for d in range(len(f)):
            if(f[d]==1):
                    p.append(d)
    if(len(u)!=0):
        while True:
           
            p=[]
            for d in range(len(f)):
                    if(f[d]==1):
                        p.append(d)
            #print(p)
            s=[]
            for i in range(len(u)):
                    s.append(len(intersection(p,u[i][0])))
            #print(s)
            k=0
            if(sum(s)!=0):
                for  i in range(len(s)):
                                
                    if(max(s)==s[i]):
                        
                        if(k==0):
                            k=k+1
                            ans.append(u[i])
                            for j in range(len(u[i][0])):
                                f[u[i][0][j]]=0
            if  (sum(p)==0):
                 break
    print(ans)  
    f=[0]*(max(all_minterm)+1)
    for i in range(len(all_minterm)):
        f[all_minterm[i]]=1
    for i in range(len(all_minterm)):
        for j in range(len(ans)):
            for k in range(len(ans[j][0])):
                if(all_minterm[i]==ans[j][0][k]):
                    f[all_minterm[i]]=0
    print(f)
    
       
    
    r=0
    
    e=len(x1)-1
    print(e)
    if(e!=0):
        while True:
                print(f)
                p=[]
                for d in range(len(f)):
                        if(f[d]==1):
                            p.append(d)
                print(p)
                s=[]
                for i in range(len(x1[e])):
                        s.append(len(intersection(p,[x1[e][i][0]])))
                print(s)
                k=0
                if(sum(s)!=0):
                    for  i in range(len(s)):
                        if(max(s)==s[i]):
                            if(k==0):
                                k=k+1
                                ans.append(x1[e][i])
                                if(e!=0):
                                    for j in range(len([x1[e][i][0]])):
                                        f[x1[e][i][0][j]]=0
                                if(e==0):
                                    f[x1[e][i][0]]=0
                            
                if((sum(s)==0)and(sum(f)!=0)):
                     e=e-1
                if(sum(f)==0):
                     break
        
            
    print(ans)
    print(f)
    if(sum(f)!=0):
        p=[]
        for d in range(len(f)):
                    if(f[d]==1):
                        p.append(d) 
        for i in range(len(p)):
        
            str1='0'*(g-len(bin(p[i])[2:]))
            str1=str1+(bin(p[i])[2:])
            ans.append([p[i],str1,0])
    print(ans)
    m=[]
    for k in range(len(ans)):  
        str2=' '
        for i in range(len(ans[k][1])):
           
                if(ans[k][1][i]=='1'):
                    str1=str(i)+'a'
                    str2=str1+str2
                    
                    
                elif(ans[k][1][i]=='0'):
                    str1="'"+str(i)+'a'
                    str2=str1+str2
        str2=" "+str2          
        str2 = "".join(reversed(str2)) 
        m.append(str2)
    
    print("\n") 
    print(all_minterm)
    print("\n")
    print("the output is:")
    print(ans)
    print("\n")
    print(m)
else:
    
    print("------*****$$$*****-----")       
    
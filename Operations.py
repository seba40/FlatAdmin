from datetime import datetime as dt
import datetime
import copy
ch = {'apartament':[],'apa':[],'canal':[],
              'incalzire':[],'gaz':[],'altele':[]}
ch1=[]
ch2=[]
ch3=[]
chrap=[]
backup=[]
def sortare(list,opt):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if (ch[opt][i][0]>ch[opt][j][0]):
                aux=list[i]
                list[i]=list[j]
                list[j]=aux
class Ops:

    def reg(self):
        global ch
        global backup
        backup.append(copy.deepcopy(ch))
        if len(backup) > 10:
            backup.pop(0)

    def optiune1(self,n):
            #setare numar apartamente
            global ch
            
            

            
            for i in range(0,n):
                ch['apartament'].append(i+1)
                ch['apa'].append([0,0])
                ch['canal'].append([0,0])
                ch['incalzire'].append([0,0])
                ch['gaz'].append([0,0])
                ch['altele'].append([0,0])
                
                
            
    def optiune2(self,ap,opt,val,datastr):
        #adaugare
        global ch
        zi,luna,an=map(int,datastr.split('.'))
        data =datetime.date(an,luna,zi)
        ch[opt][ap-1] = [val,data]
            
    def optiune3(self,index,ap,i,j,opt):
        #stergere
        global ch
        if (index ==1):
            ch['apa'][ap-1] = [0,0]
            ch['canal'][ap-1] = [0,0]
            ch['incalzire'][ap-1] = [0,0]
            ch['gaz'][ap-1] = [0,0]
            ch['altele'][ap-1] = [0,0]
            
        if (index ==2):
            
            for x in range(i,j+1):
                ch['apa'][x-1] = [0,0]
                ch['canal'][x] = [0,0]
                ch['incalzire'][x-1] = [0,0]
                ch['gaz'][x-1] = [0,0]
                ch['altele'][x-1] = [0,0]
    
        if (index==3):
            ch[opt][ap-1] = [0,0]
    def optiune4(self,index,n,datastr):
        #afisare "cautare"
        global ch
        global ch1
        global ch2
        global ch3
        
        if (index ==1):
            
            for i in range (0,len(ch['apartament'])):
                if (ch['apa'][i][0] > n or ch['canal'][i][0] > n or ch['incalzire'][i][0] > n or ch['gaz'][i][0] > n or ch['altele'][i][0] > n):
                    s=str("Apartamentul "+str(ch['apartament'][i])+" are cheltuieli mai mari decat "+str(n))
                    ch1.append(s)
        if (index ==2):
            s="Pentru "+str(n)+" cheltuielile sunt urmatoarele : "
            ch2.append(s)
            for i in range(0,len(ch[n])):
                s="Apartament "+str(i+1)+" ==> "+str(ch[n][i][0])+" "+str(ch[n][i][1])
                ch2.append(s)
        if (index ==3):
            
            
            zi,luna,an=map(int,datastr.split('.'))
            data =datetime.date(an,luna,zi)
            
            chstr=['apa','canal','incalzire','gaz','altele']       
            for i in range (0,len(ch['apartament'])):
                for j in chstr:
                    if (ch[j][i][1]!=0):
                        if (data >ch[j][i][1] and ch[j][i][0] > n):
                            s="Apartament "+str(i+1)+" : "+str(j)+" "+str(ch[j][i][0])+" "+str(ch[j][i][1])
                            ch3.append(s)
    
    def optiune5(self,index,opt):
        #Rapoarte          
        global ch
        global chrap
        s=0
        if (index ==1):
            chrap=[]
            for i in range (0,len(ch['apartament'])):
                s=s+ch[opt][i][0]
            chrap.append("Suma totala pentru "+str(opt)+" ==> "+str(s))
        if (index ==2):
            chrap=[]           
            copy=ch['apartament']
            sortare(copy,opt)
            chrap.append("Ordinea apartamentelor este : "+str(copy))
        if (index ==3):
            chrap=[]
            s=0 
            chstr=['apa','canal','incalzire','gaz','altele']
            for i in chstr:
                s=s+ch[i][opt-1][0]
            chrap.append ("Totalul de cheltuieli este  "+str(s))
    
    def optiune6(self,index,opt):
        #filtre
        global ch
        if (index==1):
            for i in range(0,len(ch['apartament'])):
                ch[opt][i]=[0,0]
        if (index==2):      
            chstr=['apa','canal','incalzire','gaz','altele']       
            for i in range (0,len(ch['apartament'])):
                for j in chstr:
                    if (ch[j][i][0]<opt):
                        ch[j][i]=[0,0]
    def und(self):
        global ch
        global backup
        
        if (len(backup)>1):
            poz=len(backup)-2
            ch=0
            ch=copy.deepcopy(backup[poz])
            backup.pop(poz+1)
            
        
                            
                        
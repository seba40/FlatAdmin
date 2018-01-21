import Back.Operations as bk
import io
import os



class stream():
    def save(self):
        path=os.path.abspath("file.ap")   
        f=open(path, 'w')
        chstr=['apa','canal','incalzire','gaz','altele']
        
        for i in range(0,len(bk.ch['apartament'])):
            for j in chstr:
                
                s=str(str(bk.ch[j][i][0])+" " +str(bk.ch[j][i][1]))
                f.write(s+"  ")
            f.write("\n")
            f.flush()
            
            
        
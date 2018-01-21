from tkinter import *
from tkinter import ttk
from Back.Operations import Ops
import Back.Operations as bk
from Back.File import stream
from tkinter.tix import ComboBox

op=Ops()
main=Tk()
f=stream()
ct=bk.ch1
def delete():
    filtrusuma.pack_forget()
    filtrutip.pack_forget()
    raptotap.pack_forget()
    rapsort.pack_forget()
    raptotal.pack_forget()
    cautdata.pack_forget()
    cauttip.pack_forget()
    cautsum.pack_forget()
    delch.pack_forget()
    delaps.pack_forget()
    delap.pack_forget()
    addframe.grid_forget()
    doneap.pack_forget()
    inputap.delete(0,'end')
    inputcautdata1.delete(0,'end')
    inputcautdata2.delete(0,'end')
    newframe.pack_forget()
    addframe.grid_forget()
    doneadd.grid_forget()


    
def printap():
    box.delete(0, last='end')
    for i in range(0,len(bk.ch['apartament'])):
            s=bk.ch['apartament'][i],bk.ch['apa'][i],bk.ch['canal'][i],bk.ch['incalzire'][i],bk.ch['gaz'][i],bk.ch['altele'][i]
            box.insert(i,s)
    scrolly.config( command = box.yview )
    scrollx.config( command = box.xview )
    
    
    
    box.pack() 
def printcaut(x):
    ct=x
    box.delete(0, last='end')
    for i in range(0,len(ct)):
        box.insert(i,ct[i])
                
    scrolly.config( command = box.yview )
    scrollx.config( command = box.xview )

    box.pack()


def new():
    delete()
    textap.pack()
    inputap.pack()
    butap.pack()
    newframe.pack()
def add():
    delete()
    inputadd_ap.delete(0,'end')
    inputadd_ch.delete(0,'end')
    inputadd_vl.delete(0,'end')
    inputadd_dt.delete(0,'end')
    textadd_ap.grid(row=1,column=1)
    textadd_ch.grid(row=2,column=1)
    textadd_dt.grid(row=4,column=1)
    textadd_vl.grid(row=3,column=1)
    
    
    inputadd_ap.grid(row=1,column=3)
    inputadd_ch.grid(row=2,column=3)
    inputadd_vl.grid(row=3,column=3)
    inputadd_dt.grid(row=4,column=3)
    buttonadd.grid(row=5,column=2)
    addframe.grid()
def delap1():
    delete()
    textdelap.pack()
    inputdelap.pack()
    buttondelap.pack()
    delap.pack()
def delaps1():
    delete()
    textdelaps1.pack()
    inputdelaps1.pack()
    textdelaps2.pack()
    inputdelaps2.pack()
    buttondelaps.pack()
    delaps.pack()
def delch1():
    delete()
    textdelch1.pack()
    inputdelch1.pack()
    textdelch2.pack()
    inputdelch2.pack()
    buttondelch.pack()
    delch.pack()
    
def cautsum1():
    delete()
    textcautsum.pack()
    inputcautsum.pack()
    buttoncautsum.pack()
    cautsum.pack()
def cauttip1():
    delete()
    textcauttip.pack()
    inputcauttip.pack()
    buttoncauttip.pack()
    cauttip.pack()
def cautdata1():
    delete()
    textcautdata1.pack()
    inputcautdata1.pack()
    textcautdata2.pack()
    inputcautdata2.pack()
    buttoncautdata.pack()
    cautdata.pack()
def raptotal1():
    delete()
    textraptotal.pack()
    inputraptotal.pack()
    buttonraptotal.pack()
    raptotal.pack()
def rapsort1():
    delete()
    textrapsort.pack()
    inputrapsort.pack()
    buttonrapsort.pack()
    rapsort.pack()
def raptotap1():
    delete()
    textraptotap.pack()
    inputraptotap.pack()
    buttonraptotap.pack()
    raptotap.pack()
def filtrutip1():
    delete()
    textfiltrutip.pack()
    inputfiltrutip.pack()
    buttonfiltrutip.pack()
    filtrutip.pack()
def filtrusuma1():
    delete()
    textfiltrusuma.pack()
    inputfiltrusuma.pack()
    buttonfiltrusuma.pack()
    filtrusuma.pack()     
def inputnr():
    bk.ch = {'apartament':[],'apa':[],'canal':[],
              'incalzire':[],'gaz':[],'altele':[]}
    n=int(inputap.get())
    op.optiune1(n)
    doneap.pack()
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.pack(side=BOTTOM,fill=X)
    option.entryconfig(0,state=NORMAL)
    option.entryconfig(1,state=NORMAL)
    option.entryconfig(2,state=NORMAL)
    option.entryconfig(3,state=NORMAL)
    option.entryconfig(4,state=NORMAL)
    inputadd_ap.config(from_=1, to=len(bk.ch['apartament']))
    inputdelap.config(from_=1, to=len(bk.ch['apartament']))
    inputdelaps1.config(from_=1, to=len(bk.ch['apartament']))
    inputdelaps2.config(from_=1, to=len(bk.ch['apartament']))
    inputdelch1.config(from_=1, to=len(bk.ch['apartament']))
    inputraptotap.config(from_=1, to=len(bk.ch['apartament']))
    op.reg()
    printap()
    

    
def inputadd():
    doneadd.grid_forget()
    ap=int(inputadd_ap.get())
    opt=inputadd_ch.get()
    val=int(inputadd_vl.get())
    datestr=inputadd_dt.get()
    op.optiune2(ap, opt, val, datestr)
    doneadd.grid(row=6,column=2)
    op.reg()
    printap()
    
def inputdelap1():
    ap=int(inputdelap.get())
    op.optiune3(1,ap,0,0,0)
    op.reg()
    printap()
    
def inputdelaps():
    ap1=int(inputdelaps1.get())
    ap2=int(inputdelaps2.get())
    op.optiune3(2,0,ap1,ap2,0)
    op.reg()
    printap()
    
def inputdelch():
    ap=int(inputdelch1.get())
    opt=inputdelch2.get()
    op.optiune3(3,ap,0,0,opt)
    op.reg()
    printap()
    


def inputcautsum1():
    n=int(inputcautsum.get())
    op.optiune4(1,n,0)
    printcaut(bk.ch1)
    
def inputcauttip1():
    n=inputcauttip.get()
    op.optiune4(2,n,0)
    printcaut(bk.ch2)
def inputcautdata():
    n=int(inputcautdata1.get())
    datastr=inputcautdata2.get()
    op.optiune4(3,n,datastr)
    printcaut(bk.ch3)
def inputraptotal1():
    n=inputraptotal.get()
    op.optiune5(1,n)
    printcaut(bk.chrap)
def inputrapsort1():
    n=inputrapsort.get()
    op.optiune5(2,n)
    printcaut(bk.chrap)
def inputraptotap1():
    n=int(inputraptotap.get())
    op.optiune5(3,n)
    printcaut(bk.chrap)
def inputfiltrutip1():
    n=inputfiltrutip.get()
    op.optiune6(1,n)
    op.reg()
    printap()
    
def inputfiltrusuma1():
    n=int(inputfiltrusuma.get())
    op.optiune6(2,n)
    op.reg()
    printap()
    
def undo():
    op.und()
    printap()
def sv():
    f.save()
def ld():
    f.load()
    printap()
#INITIALIZATION

main.geometry('330x200')
main.title('Program de Administrare')

#NEW FRAME
newframe = Frame(main)
textap=Label(newframe,text='Numar de apartamente')
doneap=Label(newframe,text='Registrul a fost creat !')
inputap=Entry(newframe)
butap=Button(newframe,text='SET',command=inputnr)

#ADD FRAME
addframe=Frame(main)
textadd_ap =Label(addframe,text='Numarul apartamentului')
textadd_ch=Label(addframe,text='Numele cheltuielii')
textadd_vl=Label(addframe,text='Valoarea cheltuielii')
textadd_dt=Label(addframe,text='Data cheltuielii')
inputadd_ap=Spinbox(addframe)
inputadd_ch=ttk.Combobox(addframe)
inputadd_vl=Entry(addframe)
inputadd_dt=Entry(addframe)
                  
chstr=['apa','canal','incalzire','gaz','altele'] 
inputadd_ch['values']=chstr



buttonadd=Button(addframe,text='OK',command=inputadd)
doneadd=Label(addframe,text='✓')
# DEL AP FRAME

delap=Frame(main)
textdelap = Label(delap,text='Numarul Apartamentului')
inputdelap = Spinbox(delap)
buttondelap= Button(delap,text='STERGE',command=inputdelap1)
#  DEL APS FRAME
delaps=Frame(main)
textdelaps1= Label(delaps,text='Numarul primului apartament')
inputdelaps1 = Spinbox(delaps)
textdelaps2= Label(delaps,text='Numarul celui de-al doilea apartament')
inputdelaps2 = Spinbox(delaps)
buttondelaps= Button(delaps,text='STERGE',command=inputdelaps)
#DEL AP CH FRAME
delch=Frame(main)
textdelch1 = Label(delch,text='Numarul Apartamentului')
textdelch2=  Label(delch,text='Tipul Cheltuielii')
inputdelch1 = Spinbox(delch)
inputdelch2=ttk.Combobox(delch)
inputdelch2['values']=chstr
buttondelch= Button(delch,text='STERGE',command=inputdelch)
# Cautare > Suma FRAME

cautsum=Frame(main)
textcautsum=Label(cautsum,text='Suma')
inputcautsum=Entry(cautsum)
buttoncautsum=Button(cautsum,text='CAUTA',command=inputcautsum1)
# Cautare Tip
cauttip=Frame(main)
textcauttip=Label(cauttip,text='Tipul Cheltuielii')
inputcauttip=ttk.Combobox(cauttip)
inputcauttip['values']=chstr
buttoncauttip=Button(cauttip,text='CAUTA',command=inputcauttip1)
# Cautare data
cautdata=Frame(main)
textcautdata1=Label(cautdata,text='Suma')
textcautdata2=Label(cautdata,text='Data Cheltuielii')
inputcautdata1=Entry(cautdata)
inputcautdata2=Entry(cautdata)
buttoncautdata=Button(cautdata,text='CAUTA',command=inputcautdata)
# Raport total
raptotal=Frame(main)
textraptotal=Label(raptotal,text='Tipul Cheltuielii')
inputraptotal=ttk.Combobox(raptotal)
inputraptotal['values']=chstr
buttonraptotal=Button(raptotal,text='OK',command=inputraptotal1)
# Raport sortare
rapsort=Frame(main)
textrapsort=Label(rapsort,text='Tipul Cheltuielii')
inputrapsort=ttk.Combobox(rapsort)
inputrapsort['values']=chstr
buttonrapsort=Button(rapsort,text='OK',command=inputrapsort1)
#Raport total ap
raptotap=Frame(main)
textraptotap=Label(raptotap,text='Numarul Apartamentului')
inputraptotap=Spinbox(raptotap)
buttonraptotap=Button(raptotap,text='OK',command=inputraptotap1)
# Filtru tip
filtrutip=Frame(main)
textfiltrutip=Label(filtrutip,text= 'Tipul Cheltuielii')
inputfiltrutip=ttk.Combobox(filtrutip)
inputfiltrutip['values']=chstr
buttonfiltrutip=Button(filtrutip,text='OK',command=inputfiltrutip1)
#Filtru suma
filtrusuma=Frame(main)
textfiltrusuma=Label(filtrusuma,text= 'Suma')
inputfiltrusuma=Entry(filtrusuma)
buttonfiltrusuma=Button(filtrusuma,text='OK',command=inputfiltrusuma1)
#MENU CONSTR

meniu=Menu(main)

file=Menu(meniu,tearoff=0)
file.add_command(label='New',command=new)
file.add_command(label='Save',command=sv)
file.add_command(label='Load',command=ld)
file.add_command(label='Exit',command=exit)

option=Menu(main,tearoff=0)

sterg=Menu(option,tearoff=0)
sterg.add_command(label='Cheltuieli apartament',command=delap1)
sterg.add_command(label='Cheltuieli serie de ap.',command=delaps1)
sterg.add_command(label='Anumita cheltuiala',command=delch1)

caut=Menu(main,tearoff=0)
caut.add_command(label='Cheltuieli > Suma',command=cautsum1)
caut.add_command(label='Anumit tip',command=cauttip1)
caut.add_command(label='Cheltuieli inainte de data',command=cautdata1)

raport=Menu(main,tearoff=0)
raport.add_command(label='Suma totala : Cheltuiala',command=raptotal1)
raport.add_command(label='Sortare ap. dupa cheltuiala',command=rapsort1)
raport.add_command(label='Totalul pentru apartament',command=raptotap1)

filtru=Menu(main,tearoff=0)
filtru.add_command(label='Tip cheltuiala',command=filtrutip1)
filtru.add_command(label='Cheltuieli < Suma',command=filtrusuma1)


option.add_command(label='Adaugare/Schimbare',command=add,state=DISABLED)

meniu.add_cascade(label='File',menu=file)
meniu.add_cascade(label='Options',menu=option)
option.add_cascade(label='Stergere',menu=sterg,state=DISABLED)
option.add_cascade(label='Cautare',menu=caut,state=DISABLED)
option.add_cascade(label='Raport',menu=raport,state=DISABLED)
option.add_cascade(label='Filtru',menu=filtru,state=DISABLED)
meniu.add_command(label='Undo',command=undo)
main.config(menu=meniu)


# OUTPUT WINDOW
output=Toplevel()
scrollx=Scrollbar(output,orient=HORIZONTAL)
scrolly=Scrollbar(output)
box=Listbox(output,width=50,height=10,yscrollcommand = scrolly.set,xscrollcommand = scrollx.set)

#MAIN LOOP
output.mainloop()
main.mainloop()




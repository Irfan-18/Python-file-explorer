from tkinter import *
import tkinter as tk
import os, glob

root=Tk()
root.title("File explorer")
root.wm_geometry("%dx%d+%d+%d" % ( 600, 600 , 40 , 20 ))

tk.Label(root,text="File Explorer",font=('times',25)).place(x=220,y=20)
tk.Label(root,text="Selected File: ",).place(x=30,y=90)

cmd = tk.Entry(root, width=20)
cmd.place(x=110,y=90)

tk.Label(root,text="Filter: ",).place(x=150,y=135)
cmdsearch = tk.Entry(root, width=20)
cmdsearch.place(x=200,y=135)

path = "."


def createbuttons():
    print("created widgets")

    button1=tk.Button(root,text="NEW DIR",height=1,width=10,command=newdir,font=(5)).place(x=20,y=210)
 
    button2=tk.Button(root,text="NEW FILE",height=1,width=10,command=newfile,font=(5)).place(x=20,y=260)

    button3=tk.Button(root,text="DELETE",height=1,width=8,command=delete).place(x=310,y=85)

    button4=tk.Button(root,text="OPEN",height=1,width=8,command=fopen).place(x=240,y=85)

    button5=tk.Button(root,text="BACK DIR",height=1,width=10,command=retrn,font=(5)).place(x=20,y=160)

    button6=tk.Button(root,text="CLEAR",height=1,width=8,command=clr).place(x=380,y=85)
 
    button7=tk.Button(root,text="EXIT",height=1,width=5,command=root.destroy,font=(16)).place(x=450,y=470)

    button8=tk.Button(root,text="Search",height=1,width=8,command=getfiles).place(x=330,y=130)

    button9=tk.Button(root,text="Clear Search",height=1,width=10,command=clrsearch).place(x=400,y=130)

    
def newdir():    
    os.mkdir(os.getcwd() + "\\" + cmd.get())
    print("created folder")
    getfiles()
    clr()
    
def newfile():
    f = open(os.getcwd() + "\\" + cmd.get() , "w")
    print("writing")
    f.close()
    os.startfile(os.getcwd() + "\\" + cmd.get())
    print("opened file ")
    getfiles()
    clr()
    
def delete():
    full_path = os.path.join(os.getcwd(), cmd.get())
    if os.path.isdir(full_path):
        os.rmdir(full_path)
        print("deleted directory ")
    elif os.path.isfile(full_path):
        os.remove(full_path)
        print("deleted file ")
    getfiles()
    clr()    

def fopen():
    full_path = os.path.join(os.getcwd(), cmd.get())
    if os.path.isdir(full_path):
        os.chdir(full_path)
        print("opened directory ")
        getfiles()
    elif os.path.isfile(full_path):
        os.startfile(full_path)
        print("opened file ")
        getfiles()

def curselect(event):
    #clr()    
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    strpicked = picked.split(".....")
    #print ("selected: " + strpicked[0] + " " + cmd.get())
    
    if strpicked[0] == "..":
        retrn()
        clr()
    elif cmd.get() == strpicked[0]:
        fopen()
        clr()
    else:
        clr()
        cmd.insert(0, strpicked[0])

def getfiles():
    mylistbox.delete(0, END)
    sPath = os.getcwd()
    #files = os.listdir(sPath)
    if cmdsearch.get() == "":
        files = glob.glob("*")
    else:
        files = glob.glob("*" + cmdsearch.get() + "*")    
    mylistbox.insert(END, "..")
    for name in files:
        full_path = os.path.join(sPath, name)
        size = str(os.path.getsize(full_path))
        if os.path.isdir(full_path):
            mylistbox.insert(END, name + ".....<Dir>")
        else:
            mylistbox.insert(END, name + "....." + size)

def retrn():
    os.chdir('..')
    print("back")
    getfiles()

def clr():
    cmd.delete(0, END) 

def clrsearch():
    cmdsearch.delete(0, END)
    getfiles()
    
mylistbox=Listbox(root,width=40,height=15,font=('arial',13))
mylistbox.bind('<<ListboxSelect>>',curselect)
mylistbox.place(x=150,y=160)

if len(sys.argv) == 2:
    path = sys.argv[1]

os.chdir(path)
getfiles()
createbuttons()

root.mainloop()

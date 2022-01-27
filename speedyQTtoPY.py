import sintassi
import os
from os import listdir
from os.path import isfile, join

mypath=sintassi.path 
mainwin=sintassi.mainwin 

def main_program_start(fr0m,file_class,button_name,menu_name,mainwin):
    f=open("main.py","w")
    f.write(sintassi.A)
    for i in range(len(fr0m)):
        f.write(fr0m[i])
    for i in range(len(file_class)):
        if file_class[i][0]==mainwin:
            f.write("class Window(QMainWindow, "+file_class[i][1]+"):\n\n")
            f.write(sintassi.INIT)
            for c in range(len(button_name)):
                if button_name[c][0]==mainwin:
                    f.write("\t\tself."+button_name[c][1]+".clicked.connect()\n")
            for c in range(len(menu_name)):
                if menu_name[c][0]==mainwin:
                    f.write("\t\tself."+menu_name[c][1]+".triggered.connect()\n")
            f.write("\n")
        else:
            wn=file_class[i][0]
            win_name=wn.split(".")
            f.write("class "+win_name[0]+"(QDialog,"+file_class[i][1]+"):\n\n")
            f.write(sintassi.INIT)
            for c in range(len(button_name)):
                if button_name[c][0]==wn:
                    f.write("\t\tself."+button_name[c][1]+"clicked.connect()\n")
            for c in range(len(menu_name)):
                if menu_name[c][0]==wn:
                    f.write("\t\tself."+menu_name[c][1]+".triggered.connect()\n")
            f.write("\n")
    f.write(sintassi.START)
    f.close()
                   
def window_class(elenco_pyfile):
    fr0m=[]
    file_and_class=[]
    b_name=[]
    m_name=[]
    for i in range(len(elenco_pyfile)):
        f=open(elenco_pyfile[i],"r")
        for line in f.readlines():
            splitline=line.split(" ")
            if splitline[0]=="class":
                parname=splitline[1]
                cname=parname.split("(")
                class_name=cname[0]
            if (line.find("QPushButton"))!=-1:
                splitline=line.split("=")
                sl=splitline[0]
                parButton=sl.split(".")
                pB=parButton[1].split(" ")
                puls=elenco_pyfile[i]+","+pB[0]
                pulssplit=puls.split(",")
                b_name.append(pulssplit)
            if (line.find("QtWidgets.QAction(MainWindow)"))!=-1:
                splitline=line.split("=")
                sl=splitline[0]
                parMenu=sl.split(".")
                pM=parMenu[1].split(" ")
                menu=elenco_pyfile[i]+","+pM[0]
                menusplit=menu.split(",")
                m_name.append(menusplit)                  
        f.close()
        riga=elenco_pyfile[i]+","+class_name
        rigasplit=riga.split(",")
        file_and_class.append(rigasplit)
        pyfile=elenco_pyfile[i].split(".")
        fr0m.append("from "+pyfile[0]+" import "+class_name+"\n")
    return fr0m,file_and_class,b_name,m_name

elenco = [f for f in listdir(mypath) if isfile(join(mypath, f))]
os.makedirs("py_scripts")
os.chdir("py_scripts")
elenco_pyfile=[]
for i in range(len(elenco)):
    file=elenco[i]
    splitfile=file.split(".")
    pyfile=splitfile[0]+".py"
    elenco_pyfile.append(pyfile)
    os.system("pyuic5 -o "+pyfile+" "+mypath+"\\"+file)

lista,fc,bn,mm=window_class(elenco_pyfile)
main_program_start(lista,fc,bn,mm,mainwin)
 

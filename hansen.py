import math

from guizero import App, Box, PushButton, Text, TextBox
import tkinter.filedialog as filedialog
def grad2rad(g):
    return math.pi*g/200.0
def rad2grad(a):
    return 200.0*a/math.pi
def cot(a):
    return 1/math.tan(a)

global xA,yA,xB,yB,g1,g2,d1,d2
def hansen(xA,yA,xB,yB,g1,g2,d1,d2):
    print(g1,g2,d1,d2)
    d=d1+d2
    g=g1+g2
    lnom=cot(grad2rad(d))-cot(grad2rad(g))+cot(grad2rad(g1))-cot(grad2rad(d2))
    ldenom=cot(grad2rad(g1))*cot(grad2rad(d2))-cot(grad2rad(g))*cot(grad2rad(d))
    l=math.atan(lnom/ldenom)*200.0/math.pi
    alpha=200-d-g1
    beta=200-(g+d2)
    theta=200-(alpha+d-l)
    omega=200-(beta+g+l)
    A=theta
    B=beta+omega
    print("{0:.4f} {1:.4f} {2:.4f} {3:.4f} {5:.4f} {6:.4f} {7:.4f} {8:.4f} {9:.4f}  {10:.4f} {11:.4f}".format(alpha,beta,l,omega,theta,g,d,g1,g2,d1,d2,A,B))
    xm=(yB-yA+xA*cot(grad2rad(B))+xB*cot(grad2rad(A)))/(cot(grad2rad(A))+cot(grad2rad(B)))
    ym=(xA-xB+yA*cot(grad2rad(B))+yB*cot(grad2rad(A)))/(cot(grad2rad(A))+cot(grad2rad(B)))
    return xm,ym

global xA_text,yA_text,xB_text,yB_textd2_text,g1_text,g2_text,d1_text,xm_text,ym_text
    
def select_pointsfile():
    global xA,yA,xB,yB,xA_text,yA_text,xB_text,yB_text
    filename = filedialog.askopenfilename(title='Select File for points',initialdir='c:/temp/forward/')
    print("Selected file: " + filename)
    pointsfile=open(filename,'r')
    lines=pointsfile.readlines()
    print(lines)
    p1=lines[0].split()
    p2=lines[1].split()
    xA=float(p1[0])
    yA=float(p1[1])
    xB=float(p2[0])
    yB=float(p2[1])
    xA_text.value=p1[0]
    yA_text.value=p1[1]
    xB_text.value=p1[0]
    yB_text.value=p1[1]
    pointsfile.close()
    return

def select_anglesfile():
    global g1,g2,d1,d2,d2_text,g1_text,g2_text,d1_text
    filename = filedialog.askopenfilename(title='Select File for angles',initialdir='c:/temp/forward/')
    print("Selected file: " + filename)
    anglesfile=open(filename,'r')
    line1=anglesfile.readline()
    line=line1.split()
    g1=float(line[0])
    g2=float(line[1])
    d1=float(line[2])
    d2=float(line[3])
    d1_text.value=line[2]
    d2_text.value=line[3]
    g1_text.value=line[0]
    g2_text.value=line[1]
    print(g1,g2,d1,d2)
    anglesfile.close()
    return

def close_app():
    global app
    app.destroy()

def write_file():
    filename = filedialog.asksaveasfilename(
                filetypes=(
                    ("Text files", "*.txt"),
                    ("All files", "*.*"),
                ),initialdir='./')
    print("Selected file: " + filename)

def calculate():
    global app,xA,yA,xB,yB,g1,g2,d1,d2,xm_text,ym_text
    xm,ym=hansen(xA,yA,xB,yB,g1,g2,d1,d2)
    print(xA,yA,xB,yB,xm,ym)
    xm_text.value="{0:.3f}".format(xm)
    ym_text.value="{0:.3f}".format(ym)
    return
global app

def main():
    global xm_text,ym_text,app,xA,yA,xB,yB,g1,g2,d1,d2,xA_text,yA_text,xB_text,yB_text,d1_text,d2_text,g1_text,g2_text
    app = App(title="File Writer", width=400, height=400,layout="grid")

    select_button1 = PushButton(app,grid=[0,0],text="Select File for points", command=select_pointsfile)
    xA_label = Text(app,grid=[1,0],text="xA")
    xA_text = TextBox(app,grid=[2,0])
    yA_label = Text(app,grid=[3,0],text="yA")
    yA_text = TextBox(app,grid=[4,0])
    xB_label = Text(app,grid=[5,0],text="xB")
    xB_text = TextBox(app,grid=[6,0])
    yB_label = Text(app,grid=[7,0],text="yB")
    yB_text = TextBox(app,grid=[8,0])

    g1_label = Text(app,grid=[1,1],text="γ1")
    g1_text = TextBox(app,grid=[2,1])
    g2_label = Text(app,grid=[3,1],text="γ1")
    g2_text = TextBox(app,grid=[4,1])
    d1_label = Text(app,grid=[5,1],text="δ1")
    d1_text = TextBox(app,grid=[6,1])
    d2_label = Text(app,grid=[7,1],text="δ2")
    d2_text = TextBox(app,grid=[8,1])

    xm_label = Text(app,grid=[1,2],text="xm")
    xm_text = TextBox(app,grid=[2,2])
    ym_label = Text(app,grid=[3,2],text="ym")
    ym_text = TextBox(app,grid=[4,2])
    
    select_button1 = PushButton(app,grid=[0,0],text="Select File for points", command=select_pointsfile)
    select_button1 = PushButton(app,grid=[0,0],text="Select File for points", command=select_pointsfile)
    select_button2 = PushButton(app, grid=[0,1],text="Select File for angles", command=select_anglesfile)
    calc_button = PushButton(app, grid=[0,2],text="Press to calculate values", command=calculate)
        
    write_button = PushButton(app, grid=[0,3], text="Write to File", command=write_file)
    exit_button = PushButton(app, grid=[0,4], text="Press me to exit!", command=close_app)
    
    app.display()

if __name__=="__main__":
    main()
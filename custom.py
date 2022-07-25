from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Vehicle service management")
root.geometry("1920x1080")

path = "logo.jpg"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)

global canvas 
canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = ImageTk.PhotoImage(Image.open("imagetwo.jpg"))
image_1 = canvas.create_image(300.0,280.0,image=image_image_1)

image_image_2 = ImageTk.PhotoImage(Image.open("admin.jpg"))
image_2 = canvas.create_image(924.0,382.0,image=image_image_2)
   
def clickcustsign():
    global custfname
    global custlname
    global custphone
    global custemail
    global custpass
    top2=Toplevel()
    top2.geometry("1920x1080")
    
    canvas.place(x = 0, y = 0)
    image_image_3 = ImageTk.PhotoImage(Image.open("background.jpg"))
    xyz = canvas.create_image(924.0,382.0,image=image_image_3)
    
    image=Image.open("mahadev.jpg")
    img=image.resize((450, 350))
    my_img = ImageTk.PhotoImage(img) 

    

    custfname=Entry(top2)
    label1=Label(top2,text="First name")
    label1.pack()
    custfname.pack()
    custlname=Entry(top2)
    label2=Label(top2,text="Last name")
    label2.pack()
    custlname.pack()
    custemail=Entry(top2)
    label3=Label(top2,text="Email")
    label3.pack()
    custemail.pack()
    custphone=Entry(top2)
    label4=Label(top2,text="Mobile number")
    label4.pack()
    custphone.pack()
    custpass=Entry(top2)
    label5=Label(top2,text="Set password")
    label5.pack()
    custpass.pack()
    custsubmit=Button(top2,text="sign up",command=clicksignup)
    custsubmit.pack()
    label5=Label(top2,text="already a customer?")
    label5.pack()
    custlog=Button(top2,text="customer login",command=clickcustlog)
    custlog.pack()
    
    

def jobcard():
    global services
    top3=Toplevel()
    top3.geometry("1920x1080")
    if var1.get()==1:
        services+=" genaral services,"
    if var2.get()==1:
        services+=" oil service,"
    if var3.get()==1:
        services+=" break system maintanance,"
    if var4.get()==1:
        services+=" engine maintanance,"
    if var5.get()==1:
        services+=" oil service,"

    label1=Label(top3,text=services[:-1])
    label1.pack()
global clicksubmit


def clicksignup():
    global var1
    global var2
    global var3
    global var4
    global var5

    global services
    services="The services are"
    top1=Toplevel()
    top1.geometry("1920x1080")
    label1=Label(top1,text="welcome"+" "+custfname.get()+" "+"enter your vehicle details and pick the services you want")
    label1.pack()
    label2=Label(top1,text="Vehicle Brand and Model")
    label2.pack() 
    vbrand=Entry(top1)
    vbrand.pack()
    label3=Label(top1,text="Vehicle Reg no.")
    label3.pack() 
    vreg=Entry(top1)
    vreg.pack()
    var1=IntVar()
    gen=Checkbutton(top1,text="general service",variable=var1)
    gen.pack()
    var2=IntVar()
    oils=Checkbutton(top1,text="oil service",variable=var2)
    oils.pack()
    var3=IntVar()
    br=Checkbutton(top1,text="break system maintanance",variable=var3)
    br.pack()
    var4=IntVar()
    eng=Checkbutton(top1,text="engine maintanance",variable=var4)
    eng.pack()
    var5=IntVar()
    cl=Checkbutton(top1,text="oil service",variable=var5)
    cl.pack()
    
    subbut=Button(top1,text="submit",command=jobcard)
    subbut.pack()
    

    
#general checkup oil maintenace break system maintanance engine maintanance clutch repair battery
    
global clickcustlog

def clickcustlog():
    custemail=Entry(root)
    label1=Label(root,text="Email/Mobile number")
    label1.pack()
    custemail.pack()
    custpass=Entry(root)
    label2=Label(root,text="password")
    label2.pack()
    custpass.pack()
    
    canvas.place(x = 0, y = 0)
    image_image_3 = ImageTk.PhotoImage(Image.open("background.jpg"))
    global xyz
    xyz = canvas.create_image(924.0,382.0,image=image_image_3)


#custsign=Button(root,text="customer sign in",command=clickcustsign,fg="white",bg="blue")
#button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_1 = ImageTk.PhotoImage(Image.open("button_3.png"))

custsign = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    text="customer sign in",command=clickcustsign
)
custsign.place(
    x=880.0,
    y=315.0,
    width=114.0,
    height=41.0
)


adlog=Button(root,text="admin login")
adlog.place(
    x=880.0,
    y=375.0,
    
)
mechlog=Button(root,text="mechanic login")
mechlog.place(
    x=880.0,
    y=430.0,
    
)
#custsign.pack()
#adlog.pack()
#mechlog.pack()
#root.resizable(False, False)

mainloop()
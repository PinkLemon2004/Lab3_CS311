from tkinter import*
from tkinter import messagebox

#การแสดงผลหน้าตาการทำงาน
def mainwindow():
    root = Tk()
    root.title("Sales Dashborad")
    root.geometry("950x600")
    root.configure(bg='lightgreen')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    root.iconbitmap('img/icon.ico')
    return(root)
#ฟังก์ชันคำสั่งที่จะทำงานตอนคลิก
def click1():
    messagebox.showinfo("Rujira said", "Click Me 1 clicked")
def click2():
    messagebox.showinfo("Rujira said", "Click Me 2 clicked")
def click3():
    messagebox.showinfo("Rujira said", "Click Me 3 clicked")

#สร้างเฟรมแบ่งเฟรมเพื่อเอาไว้ใส่วิทเจ็ต
def createframe(root) :
    #บนสุด
    top = Frame(root,bg='#B9C8F9') 
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    #ทางซ้าย
    left = Frame(root,bg='#ffffff')
    left.rowconfigure((0,1,2),weight=1) 
    left.columnconfigure((0,1,2,3),weight=1)
    left.grid(row=1,column=0,sticky='news')
    #ล่าง
    bottom = Frame(root,bg='#277D84')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1,2,3),weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')

    #ขวา
    right = Frame(root,bg='red')
    right.rowconfigure((0,1),weight=1) 
    right.columnconfigure(0,weight=2)
    right.grid(row=1,column=1,sticky='news')

    return(root,top,left,right,bottom)

#ใส่ข้อความที่หัวข้อด้านบย
def widgettop(top):
    #ใส่labelในเฟรมtop
    headingLabel = Label(top,text='Sales Dashboard By Rujira Navaen',font=('Arial',30,'bold'),bg='#B6F4FF',padx=900,pady=20)
    headingLabel.grid(row=0,columnspan=2)


def widgetleft(left):

    #menu 4 อัน
    profile_Revenue = Text(left, width=20, height=8, padx=1,bg='#4CB60F')
    profile_Revenue.tag_config("tag-center-bold", justify='center', font=('Verdana', 11, 'bold'))
    profile_Revenue.tag_config("tag-center", justify='center', font=('Verdana', 10))

    profile_Revenue.insert(INSERT, '\nRevenue\n', 'tag-center-bold')
    profile_Revenue.insert(INSERT, '\n917,000\n', 'tag-center')

    profile_Revenue.grid(row=0, column=0,sticky='w')
    profile_Revenue.config(state="disabled")

    profile_Order = Text(left, width=20, height=8, padx=1,bg='#DFB913')
    profile_Order.tag_config("tag-center-bold", justify='center', font=('Verdana', 11, 'bold'))
    profile_Order.tag_config("tag-center", justify='center', font=('Verdana', 10))

    profile_Order.insert(INSERT, '\nOrder\n', 'tag-center-bold')
    profile_Order.insert(INSERT, '\n898\n', 'tag-center')

    profile_Order.grid(row=0, column=1,sticky='w')
    profile_Order.config(state="disabled")

    profile_AOV = Text(left, width=20, height=8, padx=1,bg='#17C1C7')
    profile_AOV.tag_config("tag-center-bold", justify='center', font=('Verdana', 11, 'bold'))
    profile_AOV.tag_config("tag-center", justify='center', font=('Verdana', 10))

    profile_AOV.insert(INSERT, '\nAvg. Order Value\n', 'tag-center-bold')
    profile_AOV.insert(INSERT, '\n1021\n', 'tag-center')

    profile_AOV.grid(row=0, column=2,sticky='w')
    profile_AOV.config(state="disabled")

    profile_Customers = Text(left, width=20, height=8, padx=1,bg='#B42D2D')
    profile_Customers.tag_config("tag-center-bold", justify='center', font=('Verdana', 11, 'bold'))
    profile_Customers.tag_config("tag-center", justify='center', font=('Verdana', 10))

    profile_Customers.insert(INSERT, '\nCustomers\n', 'tag-center-bold')
    profile_Customers.insert(INSERT, '\n819\n', 'tag-center')

    profile_Customers.grid(row=0, column=3,sticky='w')
    profile_Customers.config(state="disabled")

    #Topchannels
    title1 = Label(left,text='Top Channels',font=('Arial',18,'bold'),bg='#FFFFFF')
    title1.grid(row=1,columnspan=2,sticky='nw')

    img = Label(left,image=img2,bg='#FFFFFF')
    img.grid(row=2,columnspan=2,sticky='nwes')
    
    #Bestsellers
    title2 = Label(left,text='Bestseller',font=('Arial',18,'bold'),bg='#FFFFFF')
    title2.grid(row=1,column=2,columnspan=2,sticky='nw')
    
    #สร้างพื้นที่1อันแล้วใส่เข้าไป5อัน จะได้ไม่ต้องนั่งแยกแถว ไม่ต้องทำตามนี้ก็ได้ เพราะมักง่าย
    cv = Label(left,bg='#FFFFFF')
    cv.grid(row=2,column=2,columnspan=2,sticky='wn')

    con1 = Label(cv,text='1.Le Chiquito Bag',font=('Arial',12),bg='#FFFFFF')
    con1.grid(column=1,row=0,sticky='w',pady=10)

    con2 = Label(cv,text='2. Fendi FF Mask',font=('Arial',12),bg='#FFFFFF')
    con2.grid(column=1,row=1,sticky='w')

    con3 = Label(cv,text='3.Raito Racer Sneakers',font=('Arial',12),bg='#FFFFFF')
    con3.grid(column=1,row=2,sticky='w',pady=10)

    con4 = Label(cv,text='4.Carly Mini Bag',font=('Arial',12),bg='#FFFFFF')
    con4.grid(column=1,row=3,sticky='w')

    con5 = Label(cv,text='5.Eva Shoulder Bag - Ivory Croc',font=('Arial',12),bg='#FFFFFF')
    con5.grid(column=1,row=4,sticky='w',pady=10)

def widgetright(right):
    title = LabelFrame(right,text='Device',bg='#FFFFFF') #ใช้LabelFrame จะมีเส้นต้องขอบ
    title.grid(column=0, rowspan=2,sticky="nsew")

    imgdv = Label(right,image=img3,bg='#FFFFFF')
    imgdv.grid(row=0)

#ปุ่ม
def widgetbottom(bottom):
    btn1 = Button(bottom,image=img1,text='Click Me 1',compound='center',bg='#277D84',border=0,command=click1)
    btn1.grid(row=0,column=0)
    btn2 = Button(bottom,image=img1,text='Click Me 2',compound='center',bg='#277D84',border=0,command=click2)
    btn2.grid(row=0,column=1)
    btn3 = Button(bottom,image=img1,text='Click Me 3',compound='center',bg='#277D84',border=0,command=click3)
    btn3.grid(row=0,column=2)
    btn4 = Button(bottom,image=img1,text='Exit Program',compound='center',bg='#277D84',border=0,command=quit)
    btn4.grid(row=0,column=3)

root = mainwindow()
img1 = PhotoImage(file="img/button.png")
img2 = PhotoImage(file="img/chanels.png")
img3 = PhotoImage(file="img/device.png")
root,top,left,right,bottom = createframe(root)
widgettop(top)
widgetleft(left)
widgetright(right)
widgetbottom(bottom)
root.mainloop()
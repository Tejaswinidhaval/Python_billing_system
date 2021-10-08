
from tkinter import *
import time
import datetime
import random

root =Tk()
root.geometry("1350x750+0+0")
root.title("COSMETIC PRODUCTS SHOPPING")
root.configure(background='light pink')
Tops = Frame(root,bg='magenta',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=('arial',60,'bold'),text='SHIMMER BEAUTY PRODUCTS',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)
ReceiptCal_F = Frame(root,bg='purple',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F,bg='purple',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F,bg='pink',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F,bg='purple',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)
##############################################################
MenuFrame = Frame(root,bg='purple',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='violet',bd=4,relief=RIDGE)
Cost_F.pack(side=BOTTOM)
Makeup_F=Frame(MenuFrame,bg='pink',bd=4,relief=RIDGE)
Makeup_F.pack(side=LEFT)
SelfCare_F=Frame(MenuFrame,bg='pink',bd=4,relief=RIDGE)
SelfCare_F.pack(side=RIGHT)
###########################variables############################
var1=IntVar()
var2=IntVar()
var3=IntVar()

var9=IntVar()
var10=IntVar()
var11=IntVar()

b=StringVar()
DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofMakeup = StringVar()
CostofSelfCare = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""
text_Input1 = StringVar()

E_brush = StringVar()
E_eye = StringVar()
E_lip = StringVar()

E_kit = StringVar()
E_mask = StringVar()
E_perfume = StringVar()

text_Input.set("")
text_Input1.set("")

E_brush.set("0")
E_eye.set("0")
E_lip.set("0")
E_kit.set("0")
E_mask.set("0")
E_perfume.set("0")
DateofOrder.set(time.strftime("%d/%m/%y"))
#####################FunctionDeclaration########################
def iExit():
    root.destroy()
       
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofMakeup.set("")
    CostofSelfCare.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    text_Input.set("")
    text_Input1.set("")
    E_brush.set("0")
    E_eye.set("0")
    E_lip.set("0")
    
    E_kit.set("0")
    E_mask.set("0")
    E_perfume.set("0")
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    
    var9.set(0)
    var10.set(0)
    var11.set(0)

    txtDisplay.configure(state=DISABLED)
    txtDisplay1.configure(state=DISABLED)
    txtbrush.configure(state=DISABLED)
    txteye.configure(state=DISABLED)
    txtlip.configure(state=DISABLED)
    
    txtkit.configure(state=DISABLED)
    txtmask.configure(state=DISABLED)
    txtperfume.configure(state=DISABLED)
    
def CostofItem():
    Item1=float(E_brush.get())
    Item2=float(E_eye.get())
    Item3=float(E_lip.get())
    
    Item9=float(E_kit.get())
    Item10=float(E_mask.get())
    Item11=float(E_perfume.get())
    
    PriceofMakeup =(Item1 * 350) + (Item2 * 630) + (Item3 * 1020) 
    PriceofSelfCare =(Item9 * 1500) + (Item10 * 750) + (Item11 * 250) 
    MakeupPrice = "Rs",str('%.2f'%(PriceofMakeup))
    SelfCarePrice =  "Rs",str('%.2f'%(PriceofSelfCare))
    CostofMakeup.set(SelfCarePrice)
    CostofSelfCare.set(MakeupPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofMakeup + PriceofSelfCare + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofMakeup + PriceofSelfCare + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofMakeup + PriceofSelfCare + 1.59) * 0.15)
    TC="Rs",str('%.2f'%(PriceofMakeup + PriceofSelfCare + 1.59 + TT))
    TotalCost.set(TC)
    txtDisplay.configure(state=NORMAL)
    txtDisplay1.configure(state=NORMAL)

    totmain=TotalCost.get()
    
def chkbrush():
    if(var1.get() == 1):
        txtbrush.configure(state = NORMAL)
        txtbrush.focus()
        txtbrush.delete('0',END)
        E_brush.set("")
    elif(var1.get() == 0):
        txtbrush.configure(state = DISABLED)
        E_brush.set("0")
       
def chkeye():
    if(var2.get() == 1):
        txteye.configure(state = NORMAL)
        txteye.focus()
        txteye.delete('0',END)
        E_eye.set("")
    elif(var2.get() == 0):
        txteye.configure(state = DISABLED)
        E_eye.set("0")

def chk_lip():
    if(var3.get() == 1):
        txtlip.configure(state = NORMAL)
        txtlip.delete('0',END)
        txtlip.focus()
    elif(var3.get() == 0):
        txtlip.configure(state = DISABLED)
        E_lip.set("0")

def chk_kit():
    if(var9.get() == 1):
        txtkit.configure(state = NORMAL)
        txtkit.delete('0',END)
        txtkit.focus()
    elif(var9.get() == 0):
        txtkit.configure(state = DISABLED)
        E_kit.set("0")

def chk_mask():
    if(var10.get() == 1):
        txtmask.configure(state = NORMAL)
        txtmask.delete('0',END)
        txtmask.focus()
    elif(var10.get() == 0):
        txtmask.configure(state = DISABLED)
        E_mask.set("0")

def chk_perfume():
    if(var11.get() == 1):
        txtperfume.configure(state = NORMAL)
        txtperfume.delete('0',END)
        txtperfume.focus()
    elif(var11.get() == 0):
        txtperfume.configure(state = DISABLED)
        E_perfume.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Brush:\t\t\t\t\t' + E_brush.get() +'\n')
    txtReceipt.insert(END,'Eyeshadow:\t\t\t\t\t'+ E_eye.get()+'\n')
    txtReceipt.insert(END,'Lipstick:\t\t\t\t\t'+ E_lip.get()+'\n')
    txtReceipt.insert(END,'Kit:\t\t\t\t\t'+ E_kit.get()+'\n')
    txtReceipt.insert(END,'Mask:\t\t\t\t\t'+ E_mask.get()+'\n')
    txtReceipt.insert(END,'Perfumre:\t\t\t\t\t'+ E_perfume.get()+'\n')
    txtReceipt.insert(END,'Cost of Make-Up:\t\t\t\t'+ CostofSelfCare.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Skin Care:\t\t\t\t'+ CostofMakeup.get()+'\nS0ubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")
###########################Makeup############################

    
brush=Checkbutton(Makeup_F,variable=var1,onvalue=1,offvalue=0,
                    bg='pink',command=chkbrush).grid(row=0,sticky=W)
brush=Label(Makeup_F,text='BRUSH\t\t\tRs.350',bg='pink',font=("arial",12,"bold")).grid(row=1,sticky=W)



eye=Checkbutton(Makeup_F,variable=var2,onvalue=1,offvalue=0,
                    bg='pink',command=chkeye).grid(row=2,sticky=W)

eye=Label(Makeup_F,text='EYESHADOW\t\tRs.630',bg='pink',font=("arial",12,"bold")).grid(row=3,sticky=W)

lip=Checkbutton(Makeup_F,variable=var3,onvalue=1,offvalue=0,
                    bg='pink',command=chk_lip).grid(row=4,sticky=W)
lip=Label(Makeup_F,text='LIPSTICK\t\tRs.1020',bg='pink',font=("arial",12,"bold")).grid(row=5,sticky=W)

########################MakeupEntry###########################
txtbrush = Entry(Makeup_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_brush)
txtbrush.grid(row=0,column=1)

txteye = Entry(Makeup_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_eye)
txteye.grid(row=2,column=1)

txtlip = Entry(Makeup_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_lip)
txtlip.grid(row=4,column=1)
###########################SelfCare############################


kit = Checkbutton(SelfCare_F,variable=var9,onvalue = 1, offvalue=0,
                        bg='pink',command=chk_kit).grid(row=0,sticky=W)
kit=Label(SelfCare_F,text='SELF-CARE KIT\t\tRs.1500',bg='pink',font=("arial",12,"bold")).grid(row=1,sticky=W)



mask = Checkbutton(SelfCare_F,variable=var10,onvalue = 1, offvalue=0,
                        bg='pink',command=chk_mask).grid(row=2,sticky=W)
mask=Label(SelfCare_F,text='TEA TREE MASK\t\tRs.750',bg='pink',font=("arial",12,"bold")).grid(row=3,sticky=W)


perfume = Checkbutton(SelfCare_F,variable=var11,onvalue = 1, offvalue=0,
                        bg='pink',command=chk_perfume).grid(row=4,sticky=W)
perfume=Label(SelfCare_F,text='PERFUME\t\tRs.250',bg='pink',font=("arial",12,"bold")).grid(row=5,sticky=W)
##########################EntrySelfCare#########################
txtkit=Entry(SelfCare_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_kit)
txtkit.grid(row=0,column=1)

txtmask=Entry(SelfCare_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_mask)
txtmask.grid(row=2,column=1)

txtperfume=Entry(SelfCare_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_perfume)
txtperfume.grid(row=4,column=1)
##########################ToTalCost############################
lblCostofSelfCare=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Make-Up\t',bg='violet',
                fg='black',justify=CENTER)
lblCostofSelfCare.grid(row=0,column=0,sticky=W)
txtCostofSelfCare=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofSelfCare)
txtCostofSelfCare.grid(row=0,column=1)

lblCostofMakeup=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Skin Care  ',bg='violet',
                fg='black',justify=CENTER)
lblCostofMakeup.grid(row=1,column=0,sticky=W)
txtCostofMakeup=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofMakeup)
txtCostofMakeup.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='violet',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
#######################Paymentinformation######################
lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='violet',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='violet',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='violet',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)
#########################RECEIPT##############################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)
##########################BUTTONS############################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='violet',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Order',
                        bg='violet',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Clear',
                        bg='violet',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='violet',command=iExit).grid(row=0,column=3)
#############################order############################
name=Label(Cal_F,font=('arial',14,'bold'),text='NAME:',bg='pink',bd=7,
                fg='black',justify=CENTER)
name.grid(row=0,column=0,sticky=W)
mob=Label(Cal_F,font=('arial',14,'bold'),text='MOBILE NO:',bg='pink',bd=7,
                fg='black',justify=CENTER)
mob.grid(row=1,column=0,sticky=W)

txtDisplay=Entry(Cal_F,width=20,bg='white',bd=4,font=('arial',12,'bold'),justify=LEFT,textvariable=text_Input)
txtDisplay.grid(row=0,column=1,sticky=W,pady=1)
txtDisplay1=Entry(Cal_F,width=20,bg='white',bd=4,font=('arial',12,'bold'),justify=LEFT,textvariable=text_Input1)
txtDisplay1.grid(row=1,column=1,sticky=W,pady=1)
root.mainloop()

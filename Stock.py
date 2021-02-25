from tkinter import Tk, Label, Entry, Button

#Profit
def Profit():
    #PROFIT(Label)
    ProfitText=Label(root, text="PROFIT", bg="green")
    ProfitText.grid(row=7, column=0, columnspan=3)

    #ProfitPerStock, ProfitTot, Profit%, ProfitRatio (Labels)
    ProfitPerStockDisp=Label(root, text="Profit per stock:", fg="white", bg='#3b3b3b')
    ProfitPerStockDisp.grid(row=8, column=0)

    ProfitTotDisp=Label(root, text="Total profit:", fg="white", bg='#3b3b3b')
    ProfitTotDisp.grid(row=9, column=0)

    ProfitPercentDisp=Label(root, text="Profit %:", fg="white", bg='#3b3b3b')
    ProfitPercentDisp.grid(row=10, column=0)

    ProfitRatioDisp=Label(root, text="Profit ratio:", fg="white", bg='#3b3b3b')
    ProfitRatioDisp.grid(row=11, column=0)

    #ProfitPerStock, ProfitTot, Profit%, ProfitRatio (Entry)
    ProfitPerStock=Entry(root, width=10, bg='#6e6e6e', fg='white')
    ProfitPerStock.grid(row=8, column=1)

    ProfitTot=Entry(root, width=10, bg='#6e6e6e', fg='white')
    ProfitTot.grid(row=9, column=1)

    ProfitPercent=Entry(root, width=10, bg='#6e6e6e', fg='white')
    ProfitPercent.grid(row=10, column=1)

    ProfitRatio=Entry(root, width=10, bg='#6e6e6e', fg='white')
    ProfitRatio.grid(row=11, column=1)

    #Profit calc, clear, insert
    pps=round(float(Sp.get())-float(Bp.get()), 2)
    ProfitPerStock.delete(0,10)
    ProfitPerStock.insert(0, pps)

    pt=round(pps*float(SpNo.get()), 2)
    ProfitTot.delete(0,10)
    ProfitTot.insert(0, pt)

    pp=round((pt*100)/(float(Bp.get())*float(BpNo.get())), 2)
    ProfitPercent.delete(0, 10)
    ProfitPercent.insert(0, pp)

    pr=round(pt/(float(Bp.get())*float(BpNo.get())), 2)
    ProfitRatio.delete(0, 10)
    ProfitRatio.insert(0, pr)

#Loss func
def Loss():
    #LOSS(Label)
    LossText=Label(root, text="LOSS", bg="red")
    LossText.grid(row=7, column=0, columnspan=3)

    #LossPerStock, LossTot, Loss%, LossRatio (Labels)
    LossPerStockDisp=Label(root, text="Loss per stock:", fg="white", bg='#3b3b3b')
    LossPerStockDisp.grid(row=8, column=0)

    LossTotDisp=Label(root, text="Total loss:", fg="white", bg='#3b3b3b')
    LossTotDisp.grid(row=9, column=0)

    LossPercentDisp=Label(root, text="Loss %:", fg="white", bg='#3b3b3b')
    LossPercentDisp.grid(row=10, column=0)

    LossRatioDisp=Label(root, text="Loss ratio:", fg="white", bg='#3b3b3b')
    LossRatioDisp.grid(row=11, column=0)

    #LossPerStock, LossTot, Loss%, LossRatio (Entry)
    LossPerStock=Entry(root, width=10, bg='#6e6e6e', fg='white')
    LossPerStock.grid(row=8, column=1)

    LossTot=Entry(root, width=10, bg='#6e6e6e', fg='white')
    LossTot.grid(row=9, column=1)

    LossPercent=Entry(root, width=10, bg='#6e6e6e', fg='white')
    LossPercent.grid(row=10, column=1)

    LossRatio=Entry(root, width=10, bg='#6e6e6e', fg='white')
    LossRatio.grid(row=11, column=1)

    #Loss calc, clear, insert
    lps=round(float(Bp.get())-float(Sp.get()), 2)
    LossPerStock.delete(0,10)
    LossPerStock.insert(0, lps)

    lt=round(lps*float(SpNo.get()), 2)
    LossTot.delete(0,10)
    LossTot.insert(0, lt)

    lp=round((lt*100)/(float(Bp.get())*float(BpNo.get())), 2)
    LossPercent.delete(0, 10)
    LossPercent.insert(0, lp)

    lr=round((float(Bp.get())*float(BpNo.get()))/lt, 2)
    LossRatio.delete(0, 10)
    LossRatio.insert(0, lr)

#Break-even func
def Be():
    #LOSS(Label)
    BeText=Label(root, text="Break-even", bg="grey")
    BeText.grid(row=7, column=0, columnspan=3)

#Go button func
def go1():
    #TotBP(Label)
    TotDisp1=Label(root, text="Total BP=", fg="white", bg='#3b3b3b')
    TotDisp1.grid(row=3, column=0)

    #Tot BP(Entry and insert)
    TotEntry1=Entry(root, width=10, bg='#6e6e6e', fg='white')
    TotEntry1.grid(row=3, column=1)

    BpTot=round(float(Bp.get())*float(BpNo.get()), 2)
    TotEntry1.insert(0, BpTot)

#Go button-2
def go2():
    #TotSP(Label)
    TotDisp2=Label(root, text="Total SP", fg="white", bg='#3b3b3b')
    TotDisp2.grid(row=6, column=0)

    #Tot SP(Entry and insert)
    TotEntry2=Entry(root, width=10, bg='#6e6e6e', fg='white')
    TotEntry2.grid(row=6, column=1)

    SpTot=round(float(Sp.get())*float(SpNo.get()), 2)
    TotEntry2.insert(0, SpTot)

    #Profit or loss
    if round(float(Bp.get())*float(BpNo.get()), 2)>round(float(Sp.get())*float(SpNo.get()), 2):
        Loss()
    elif round(float(Sp.get())*float(SpNo.get()), 2)>round(float(Bp.get())*float(BpNo.get()), 2):
        Profit()
    else:
        Be()

#All func
def all():
    SpNo.delete(0,10)
    #Verify if all values are numbers
    BpNoget=BpNo.get()
    SpNo.insert(0, float(BpNo.get()))

#Creating window
root=Tk()
root['bg']='#3b3b3b'
root.geometry("220x270")

#Title
root.title("Stock calculator")

#Heading
head=Label(root, text="Stock clac", fg="white", bg='#3b3b3b')
head.grid(row=0, column=0, columnspan=4)

#BP and BPno(Labels)
BpDisp=Label(root, text="Stock BP", fg="white", bg='#3b3b3b')
BpDisp.grid(row=1, column=0)

BpNoDisp=Label(root, text="Number of stocks", fg="white", bg='#3b3b3b')
BpNoDisp.grid(row=2, column=0)

#BP and BPno(Entry)
Bp=Entry(root, width=10, bg='#6e6e6e', fg='white')
Bp.grid(row=1, column=1)

BpNo=Entry(root, width=10, bg='#6e6e6e', fg='white')
BpNo.grid(row=2, column=1)

#Go button-1
Go1=Button(root, text="Go", command=go1, fg="white", bg='#525252')
Go1.grid(row=2, column=2)

#SP and SPno(Labels)
SpDisp=Label(root, text="Stock SP", fg="white", bg='#3b3b3b')
SpDisp.grid(row=4, column=0)

SpNoDisp=Label(root, text="No of stocks", fg="white", bg='#3b3b3b')
SpNoDisp.grid(row=5, column=0)

#SP and SPno(Entry)
Sp=Entry(root, width=10, bg='#6e6e6e', fg='white')
Sp.grid(row=4, column=1)

SpNo=Entry(root, width=10, bg='#6e6e6e', fg='white')
SpNo.grid(row=5, column=1)

#All button
All=Button(root, text="All", command=all, fg="white", bg='#525252')
All.grid(row=5, column=2)

#Go button-2
Go2=Button(root, text="Go", command=go2, fg="white", bg='#525252')
Go2.grid(row=5, column=3)

#mainlooping window
root.mainloop()

import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
from tkinter import*
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pre
import RFALG as rfproc
import LRALG as lrproc
import prediction as pred
#import script as nnpre
import plant as pl


bgcolor="#ffe6e6"
bgcolor1="#e60000"
fgcolor="#660000"


def Home():
	global window
	def clear():
	    print("Clear")
	    txt.delete(0, 'end') 
	    txt1.delete(0, 'end')  
	    txt2.delete(0, 'end')
	    txt3.delete(0, 'end')
	    txt4.delete(0, 'end')
	    txt5.delete(0, 'end')
	    txt6.delete(0, 'end')
	    txt7.delete(0.0, 'end')
	    txt8.delete(0, 'end')
	    txt9.delete(0.0, 'end')
	def clear1():
	    print("Clear1")
	    txtes.delete(0, 'end') 
	



	window = tk.Tk()
	sb=Scrollbar(window)
	sb.pack(side=RIGHT,fill=Y)
	window.title("CROP PREDICTION AND USE OF FERTILIZER")

 
	window.geometry('1280x900')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="CROP PREDICTION AND USE OF FERTILIZER" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
	message1.place(x=50, y=20)

	lbl = tk.Label(window, text="Select Dataset",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=70, y=100)
	
	txt = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=200, y=100)
	lbl = tk.Label(window, text="Select Image",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=680, y=100)
	
	txtes = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txtes.place(x=820, y=100)



	lbl1 = tk.Label(window, text="Temperature",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=70, y=180)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=200, y=180)

	lbl2 = tk.Label(window, text="Humidity",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=70, y=260)
	
	txt2 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=200, y=260)

	lbl3 = tk.Label(window, text="Soil Moisture",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=70, y=340)
	
	txt3 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=200, y=340)

	lbl4 = tk.Label(window, text="Rain Fall",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl4.place(x=70, y=420)
	
	txt4 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt4.place(x=200, y=420)

	lbl5 = tk.Label(window, text="PH",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl5.place(x=70, y=500)
	
	txt5 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt5.place(x=200, y=500)

	lbl6 = tk.Label(window, text="RF RESULT",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl6.place(x=70, y=580)
	
	txt6 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt6.place(x=200, y=580)

	lbl7 = tk.Label(window, text="RF Fertilizer",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl7.place(x=70, y=640)
	
	#txt7 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt7.place(x=800, y=390)
	txt7 = Text(window,bg="white",fg="red",font=('times', 15, ' bold '))
	txt7.place(x=200, y=640,width=200,height=100)


	lbl8 = tk.Label(window, text="Logistic Result",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl8.place(x=730, y=420)
	
	txt8 = tk.Entry(window,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt8.place(x=960, y=420)

	lbl9 = tk.Label(window, text="Logistic Fertilizer",fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl9.place(x=730, y=500)
	
	#txt9 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt9.place(x=800, y=490)
	txt9 = Text(window, bg="white",fg="red",font=('times', 15, ' bold '))
	txt9.place(x=960, y=500,width=200,height=100)


	def browse():
		path=filedialog.askopenfilename()
		print(path)
		txt.delete(0, 'end') 
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset")
	def browse1():
		path=filedialog.askopenfilename()
		print(path)
		txtes.delete(0, 'end') 
		txtes.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset")	


	def preproc():
		sym=txt.get()
		if sym != "" :
			pre.process(sym)
			print("preprocess")
			tm.showinfo("Input", "Preprocess Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def RFprocess():
		rfproc.process("results/data2.csv")
		tm.showinfo("Input", "RF Successfully Finished")

	def Regressionprocess():
		lrproc.process("results/data2.csv")
		tm.showinfo("Input", "Logistic Regression Successfully Finished")

	def predict1():
		path=txtes.get()
		
		loaded_model, class_to_idx = pl.load_checkpoint('plants9615_checkpoint.pth')
		idx_to_class = { v : k for k,v in class_to_idx.items()}
		if path != "":
			p, c = pl.predict(path, loaded_model)
			c=c[0]


			tm.showinfo("Result", c)
			
		


	def Predictprocess():
		txt6.delete(0, 'end')
		txt7.delete(0.0, 'end')
		txt8.delete(0, 'end')
		txt9.delete(0.0, 'end')

		sym1=txt1.get()
		sym2=txt2.get()
		sym3=txt3.get()
		sym4=txt4.get()
		sym5=txt5.get()
		sym="results/data2.csv"
		
		if sym1 != "" and sym2 != "" and sym3 != "" and sym4 != "" and sym5 != "":
			s=[int(sym1),int(sym2),int(sym3),int(sym4),int(sym5)]
			sv,lr=pred.process(sym,s)
			g=sv[0]
			f="NO"
			Fertilizer=""

			if g==0:
				f="NO"
				
			if g==1:
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"

			if g==2:
				f = "Oats"
				Fertilizer="Nitorgen-110 kg/acre \n P2O5 20-30 kg/acre \n K2O-17 kg/acre \n Sulphur-10 kg/acre\n"

			if g==3:
				f = "Gram"
				Fertilizer="Nitorgen-12.5 kg/acre  \nP2O5-25 kg/acre \nK2O-12.5 kg/acre \nSulphur-10 kg/acre \n"

			if g==4:
				f = "Pea"
				Fertilizer="Nitorgen-55 kg/acre \nPhosphorus-20 kg/acre \nPotash-40 kg/acre \n"

			if g==5:
				f = "Tea"
				Fertilizer="Ammonium phosphate-35 kg/acre \nPotassium sulphate-15 kg/acre \nMOP-12 kg/acre \nMagnesium sulphate-15 kg/acre \nZinc sulphate-3 kg/acre \n"

			if g==6:
				f = "Rice"
				Fertilizer="P2O5-35 kg/acre \nK2O-50 kg/acre \n"

			if g==7:
				f = "Bajra"
				Fertilizer="Nitrogen-80 kg/acre \nPhosphorous-40 kg/acre \nPhotash-40 kg/acre \n"

			if g==8:
				f = "Maize"
				Fertilizer="P2O5-24 kg/acre \nK2O-12 kg/acre \n"

			if g==9:
				f = "Cotton"
				Fertilizer="Nitrogen-150 kg/acre \nPhosphorous-60 kg/acre \nPotassium-90 kg/acre \n"

			if g==10:
				f = "Groundnut"
				Fertilizer="Nitrogen-25 kg/acre \nPhosphorous-50 kg/acre \nPotassium-75 kg/acre \nSulphur sludge-60 kg/acre \n"

			if g==11:
				f = "Jute"
				Fertilizer="Urea-8 kg/acre \nNitrogen-10 kg/acre \nN,P2O5 and K2O-20 kg/acre \n"

			if g==12:
				f = "Sugarcane"
				Fertilizer="Zinc sulphate-37.5 kg/acre \nFerrous sulphate-100 kg/acre \n"

			if g==13:
				f = "Turmeric"
				Fertilizer="Nitrogen-120 kg/acre \nP2O5-50 kg/acre \nK2O-80 kg/acre \n"

			if g==14:
				f = "No Crop"

			txt6.insert(0, f)
			txt7.insert(0.0, Fertilizer)
			g=lr[0]


			f="NO"
			Fertilizer=""

			if g==0:
				f="NO"
				
			if g==1:
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"

			if g==2:
				f = "Oats"
				Fertilizer="Nitorgen-110 kg/acre \n P2O5 20-30 kg/acre \n K2O-17 kg/acre \n Sulphur-10 kg/acre\n"

			if g==3:
				f = "Gram"
				Fertilizer="Nitorgen-12.5 kg/acre  \nP2O5-25 kg/acre \nK2O-12.5 kg/acre \nSulphur-10 kg/acre \n"

			if g==4:
				f = "Pea"
				Fertilizer="Nitorgen-55 kg/acre \nPhosphorus-20 kg/acre \nPotash-40 kg/acre \n"

			if g==5:
				f = "Tea"
				Fertilizer="Ammonium phosphate-35 kg/acre \nPotassium sulphate-15 kg/acre \nMOP-12 kg/acre \nMagnesium sulphate-15 kg/acre \nZinc sulphate-3 kg/acre \n"

			if g==6:
				f = "Rice"
				Fertilizer="P2O5-35 kg/acre \nK2O-50 kg/acre \n"

			if g==7:
				f = "Bajra"
				Fertilizer="Nitrogen-80 kg/acre \nPhosphorous-40 kg/acre \nPhotash-40 kg/acre \n"

			if g==8:
				f = "Maize"
				Fertilizer="P2O5-24 kg/acre \nK2O-12 kg/acre \n"

			if g==9:
				f = "Cotton"
				Fertilizer="Nitrogen-150 kg/acre \nPhosphorous-60 kg/acre \nPotassium-90 kg/acre \n"

			if g==10:
				f = "Groundnut"
				Fertilizer="Nitrogen-25 kg/acre \nPhosphorous-50 kg/acre \nPotassium-75 kg/acre \nSulphur sludge-60 kg/acre \n"

			if g==11:
				f = "Jute"
				Fertilizer="Urea-8 kg/acre \nNitrogen-10 kg/acre \nN,P2O5 and K2O-20 kg/acre \n"

			if g==12:
				f = "Sugarcane"
				Fertilizer="Zinc sulphate-37.5 kg/acre \nFerrous sulphate-100 kg/acre \n"

			if g==13:
				f = "Turmeric"
				Fertilizer="Nitrogen-120 kg/acre \nP2O5-50 kg/acre \nK2O-80 kg/acre \n"

			if g==14:
				f = "No Crop"


			txt8.insert(0, f)
			txt9.insert(0.0, Fertilizer)

			
			tm.showinfo("Input", "Prediction Successfully Finished")
		else:
			tm.showinfo("Input error", "Enter All Fields")

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=420, y=100)
	browse1 = tk.Button(window, text="Browse Image", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse1.place(x=960, y=100)
	predict1 = tk.Button(window, text="Predict Disease", command=predict1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	predict1.place(x=960, y=180)


	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=420, y=180)
	clearButton1 = tk.Button(window, text="Clear", command=clear1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton1.place(x=960, y=260)
	 
	proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=420, y=260)
	

	trainbutton = tk.Button(window, text="RF", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	trainbutton.place(x=420, y=340)


	DCbutton = tk.Button(window, text="LOGISTIC REGRESSION", command=Regressionprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton.place(x=420, y=420)

	DCbutton1 = tk.Button(window, text="Prediction", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton1.place(x=420, y=500)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=420, y=580)

	window.mainloop()
Home()


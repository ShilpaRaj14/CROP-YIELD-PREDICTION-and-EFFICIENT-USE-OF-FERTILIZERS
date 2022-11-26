import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
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
import RFALG as rfprocess
import LRALG as lrproc
import prediction as pred


bgcolor="#ffe6e6"
bgcolor1="#e60000"
fgcolor="#660000"


def Home():
	global window
	def clear():
	    print("Clear1")
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



	window = tk.Tk()
	window.title("CROP YIELD PREDICTION AND EFFICIENT USE OF FETERLIZERS")

 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="CROP YIELD PREDICTION AND USE OF FETERLIZERS" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=20)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=100, y=200)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=400, y=215)


	lbl1 = tk.Label(window, text="Temperature",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=100, y=280)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=400, y=285)

	lbl2 = tk.Label(window, text="Humidity",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=100, y=330)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=400, y=335)

	lbl3 = tk.Label(window, text="Soil Moisture",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=100, y=380)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=400, y=385)

	lbl4 = tk.Label(window, text="Rain Fall",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl4.place(x=100, y=430)
	
	txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt4.place(x=400, y=435)

	lbl5 = tk.Label(window, text="PH",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl5.place(x=100, y=480)
	
	txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt5.place(x=400, y=485)

	lbl6 = tk.Label(window, text="RF RESULT",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl6.place(x=600, y=280)
	
	txt6 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt6.place(x=800, y=290)

	lbl7 = tk.Label(window, text="RF Fertilizer",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl7.place(x=600, y=330)
	
	#txt7 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt7.place(x=800, y=390)
	txt7 = Text(window, width = 40, height = 4, bg="white",fg="red",font=('times', 15, ' bold '))
	txt7.place(x=800, y=340)


	lbl8 = tk.Label(window, text="Logistic Result",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl8.place(x=600, y=450)
	
	txt8 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt8.place(x=800, y=460)

	lbl9 = tk.Label(window, text="Logistic Fertilizer",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl9.place(x=600, y=500)
	
	#txt9 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt9.place(x=800, y=490)
	txt9 = Text(window, width = 40, height = 4, bg="white",fg="red",font=('times', 15, ' bold '))
	txt9.place(x=800, y=500)


	def browse():
		path=filedialog.askopenfilename()
		print(path)
		txt.delete(0, 'end') 
		txt.insert('end',path)
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
		rfprocess.process("results/data2.csv")
		tm.showinfo("Input", "Random Forest Successfully Finished")

	def Regressionprocess():
		lrproc.process("results/data2.csv")
		tm.showinfo("Input", "Logistic Regression Successfully Finished")


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
			rf,lr=pred.process(sym,s)
			g=rf[0]
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
				f = "Peas"
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

	browse = tk.Button(window, text="BROWSE", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=650, y=200)


	clearButton = tk.Button(window, text="CLEAR", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=950, y=200)
	 
	proc = tk.Button(window, text="PREPROCESS", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=50, y=600)
	

	trainbutton = tk.Button(window, text="RANDOM FOREST", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	trainbutton.place(x=300, y=600)


	DCbutton = tk.Button(window, text="LOGISTIC REGRESSION", command=Regressionprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton.place(x=550, y=600)

	DCbutton1 = tk.Button(window, text="PREDICTION", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton1.place(x=800, y=600)

	quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1040, y=600)

	window.mainloop()
Home()


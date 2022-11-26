import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import csv
from pandas.plotting import scatter_matrix

def process(path):
	np.random.seed(0)
	data = pd.read_csv(path)
	print(data.head())
	names=list(data.columns)
	print(data.iloc[:,0:1])
	ss=[]
	ss1=[]
	for line in open(path):
		print(line)
		csv_row = line.split(",") 
		print(csv_row[0],csv_row[1],csv_row[2],csv_row[3])
		a=int(csv_row[0])
		b=int(csv_row[1])
		c=int(csv_row[2])
		d=int(csv_row[3])
		e=int(csv_row[4])
		f="NO"
		g=0
		if (a >= 20 and a <= 35 and b >= 80 and b <= 85 and c >= 70 and c <= 75 and d >= 1000 and d <= 1000):
			f = "Wheat"
			g=1
		elif (a >= 30 and a <= 35 and b >= 82 and b <= 85 and c >= 71 and c <= 74 and d >= 768 and d <= 1000):
			f = "Oats"
			g=2
		elif (a >= 20 and a <= 40 and b >= 80 and b <= 85 and c >= 70 and c <= 75 and d >= 768 and d <= 1000):
			f = "Gram"
			g=3
		elif (a >= 10 and a <= 25 and b >= 83 and b <= 86 and c >= 74 and c <= 77 and d >= 768 and d <= 1000):
			f = "Peas"
			g=4
		elif (a >= 15 and a <= 25 and b >= 85 and b <= 90 and c >= 75 and c <= 80 and d >= 768 and d <= 1000):
			f = "Tea"
			g=5
		elif (a >= 24 and a <= 30 and b >= 85 and b <= 90 and c >= 76 and c <= 79 and d >= 256 and d <= 512):
			f = "Rice";
			g=6
		elif (a >= 25 and a <= 30 and b >= 85 and b <= 90 and c >= 76 and c <= 79 and d >= 768 and d <= 1000):
			f = "Bajra"
			g=7
		elif (a >= 27 and a <= 35 and b >= 90 and b <= 95 and c >= 80 and c <= 85 and d >= 768 and d <= 1000):
			f = "Maize"
			g=8
		elif (a >= 21 and a <= 30 and b >= 90 and b <= 93 and c >= 76 and c <= 79 and d >= 900 and d <= 1000):
			f = "Cotton"
			g=9
		elif (a >= 21 and a <= 35 and b >= 80 and b <= 85 and c >= 80 and c <= 85 and d >= 1004 and d <= 1007):
			f = "Groundnut"
			g=10
		elif (a >= 24 and a <= 35 and b >= 85 and b <= 90 and c >= 85 and c <= 90 and d >= 1003 and d <= 1005):
			f = "Jute"
			g=11
		elif (a >= 20 and a <= 25 and b >= 85 and b <= 90 and c >= 85 and c <= 90 and d >= 1000 and d <= 1002):
			f = "Sugarcane"
			g=12
		elif (a >= 20 and a <= 30 and b >= 95 and b <= 100 and c >= 70 and c <= 90 and d >= 1000 and d <= 1005):
			f = "Turmeric"
			g=13
		elif (d >= 1000 and d <= 1024):
			f = "NC"
			g=14
		elif (b >= 91 and b <= 100):
			f = "NC"
			g=14
		print(f)
		print(g)
		s=[a,b,c,d,e,f]
		s1=[a,b,c,d,e,g]
		ss.append(s)
		ss1.append(s1)
	print(ss)
	print(ss1)

	with open('results/data1.csv', 'w',newline='') as myFile:
		writer = csv.writer(myFile)
		writer.writerows(ss)
	
	with open('results/data2.csv', 'w', newline='') as myFile:
		writer = csv.writer(myFile)
		writer.writerows(ss1)
	
	data = pd.read_csv('results/data2.csv')
	print(data.head())

	names=list(data.columns)



	correlations = data.corr()
	# plot correlation matrix
##	fig = plt.figure()
##	fig.canvas.set_window_title('Correlation Matrix')
##	ax = fig.add_subplot(111)
##	cax = ax.matshow(correlations, vmin=-1, vmax=1)
##	fig.colorbar(cax)
##	ticks = np.arange(0,9,1)
##	ax.set_xticks(ticks)
##	ax.set_yticks(ticks)
##	ax.set_xticklabels(names)
##	ax.set_yticklabels(names)
##	fig.savefig('results/Correlation Matrix.png')
##	plt.pause(5)
##	plt.show(block=False)
##	plt.close()
    
 
	#scatterplot
	scatter_matrix(data)
	plt.savefig('results/scattermatrix.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	ncols=3
	plt.clf()
	f = plt.figure(1)
	f.suptitle("Data Histograms", fontsize=12)
	vlist = list(data.columns)
	nrows = len(vlist) // ncols
	if len(vlist) % ncols > 0:
		nrows += 1
	for i, var in enumerate(vlist):
		plt.subplot(nrows, ncols, i+1)
		plt.hist(data[var].values, bins=15)
		plt.title(var, fontsize=10)
		plt.tick_params(labelbottom='off', labelleft='off')
	plt.tight_layout()
	plt.subplots_adjust(top=0.88)
	plt.savefig('results/DataHistograms.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

import tkinter as tk
import random
import time


# Creates Window
window = tk.Tk()
window.title("Sorting Algorithms")
window.minsize(1000, 600)
window.maxsize(1000, 600)
window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 2)

# List that is filled with the heights of the rectangles
recHeights = []
# List that is filled with the heights of the random rectangles
randRecHeights = []
# List that is filled with the identifiers for each rectangle
rectangles = []

# Options for sorting methods and chart sizes
sortOptions = ["Bubble", "Quick", "Selection", "Insertion", "Merge"]
chartOptions = ["Tiny", "Small", "Medium", "Large", "Gigantic"]




def DrawRandomRectangles():
	global randRecHeights
	global rectangles
	rectangles = []
	randRecHeights = []
	num = float(len(recHeights))
	chartCanvas.delete("all")
	recWidth = float((chartCanvas.winfo_width() - 2) / num) # makes length of each rectangle 1/num of total canvas width
	#recHeight = float((chartCanvas.winfo_height() - 2) / num) # makes height of each rectangle 1/num of total canvas height
	start = 0.00 # declares beginning of rectangles (X)
	size = num # used in loop to generate all rectangles
	step = 1.00 # multiples with height/width to ensure each rectangle is flush against each other
	index = 0
	while size > 0:
		randHeight = (recHeights[random.randint(0, len(recHeights) - 1)])
		randRecHeights.append(randHeight)
		recHeights.remove(randHeight)
		a = chartCanvas.create_rectangle(start, randRecHeights[index], (recWidth * step), chartCanvas.winfo_height(), fill = "red")
		rectangles.append(a)
		step += 1 # scales height/width depending on location
		start += recWidth # makes sure each rectangles starts flush against the previous
		index += 1
		size -= 1



##################### SORTING FUNCTIONS #####################

def Bubble(): # bubble sort randrec list
	global rectangles
	global randRecHeights
	print ("Bubble")
	lenList = len(randRecHeights)     #lenList = # of rectangles
	index = 1
	x = 0
	while x < lenList:
		swapped = False
		for num in randRecHeights:

			if index == lenList:
				chartCanvas.itemconfig(rectangles[index - 1], fill = "green")
				index = 1
				continue

			chartCanvas.itemconfig(rectangles[index], fill = "yellow")
			chartCanvas.itemconfig(rectangles[index - 1], fill = "yellow")
			window.update()
			time.sleep(0.5)

			if num > randRecHeights[index]:
				x0, y0, x1, y1 = chartCanvas.coords(rectangles[index - 1])   						    					## Get coords of first rectangle
				x2, y2, x3, y3 = chartCanvas.coords(rectangles[index])														 #try deleting rectangle and making new one    						## Get coords of second rectangle
				chartCanvas.delete(rectangles[index])  																		## Set coords of first rectangle to that of the second
				chartCanvas.delete(rectangles[index - 1])
				rectangles[index] = chartCanvas.create_rectangle(x0, y0, x1, y1)												## Set coords of second rectangle to that of the first
				rectangles[index - 1] = chartCanvas.create_rectangle(x2, y2, x3, y3)
				rectangles[index], rectangles[index - 1] = rectangles[index - 1], rectangles[index] 						
				randRecHeights[index], randRecHeights[index - 1] = randRecHeights[index - 1], randRecHeights[index]
				window.update()
				swapped = True
			
			chartCanvas.itemconfig(rectangles[index], fill = "red")
			chartCanvas.itemconfig(rectangles[index - 1], fill = "red")
			window.update()
			time.sleep(0.5)

			index += 1
		if swapped == False:
			x += 1
			break
		x += 1
	print("Done")



def Quick():
	print ("Quick")

def Selection():
	print ("Selection")

def Insertion():
	print ("Insertion")

def Merge():
	print ("Merge")







# Begins the sorting algorithm
def StartSort():
	GetRectangles(chartVar.get())     ###### MAY NOT NEED WHEN SORTING IS DONE ######
	DrawRandomRectangles()
	window.update()
	for option in sortOptions:
		if sortVar.get() == option:
			if option == "Bubble": # Bubble Sort
				Bubble()
			elif option == "Quick": # Quick Sort
				Quick()
			elif option == "Selection": # Selection Sort
				Selection()
			elif option == "Insertion": # Insertion Sort
				Insertion()
			else:                   # Merge Sort
				Merge()




##################### CHART ROW #####################

# Frame that will house the sorting chart
chartFrame = tk.Frame(master = window, bg = "gray20", height = 50, width = 50, relief = "groove", bd = 5)
# Makes a row and column in frame so that the canvas can adjust with the size of the window
chartFrame.rowconfigure(0, weight = 1)
chartFrame.columnconfigure(0, weight = 1)
# Places frame in the WINDOWS row 1 and column 0
chartFrame.grid(row = 1, column = 0, sticky = "nsew")
# Create canvas to house bars
chartCanvas = tk.Canvas(master = chartFrame, bg = "gray20", highlightthickness = 0)
# Places canvas in CHARTFRAME row 0 and column 0
chartCanvas.grid(row = 0, column = 0, sticky = "NSEW")




# Draws the rectangles in order based on the chart size
# num = number of rectangles
def DrawRectangles(num):
	global recHeights
	recHeights = []
	num = float(num)
	chartCanvas.delete("all")
	recWidth = float((chartCanvas.winfo_width() - 2) / num) # makes length of each rectangle 1/num of total canvas width
	recHeight = float((chartCanvas.winfo_height() - 2) / num) # makes height of each rectangle 1/num of total canvas height
	start = 0.00 # declares beginning of rectangles (X)
	size = num # used in loop to generate all rectangles
	step = 1.00 # multiples with height/width to ensure each rectangle is flush against each other
	while size > 0:
		chartCanvas.create_rectangle(start, chartCanvas.winfo_height() - recHeight * step, (recWidth * step) + 2, chartCanvas.winfo_height(), fill = "red")
		recHeights.append(chartCanvas.winfo_height() - (recHeight * step)) # Accumulates the height of each rectangle for sorting
		step += 1 # scales height/width depending on location
		start += recWidth # makes sure each rectangles starts flush against the previous
		size -= 1
	recHeights.reverse() # makes sure heights are in order of rectangles (increasing)



# Uses the selected chart size to determine # of rectangles, then calls DrawRectangles to draw them all
def GetRectangles(size):
	recWidth = 0
	recHeight = 0
	# Create rectangles based on size chose by user:
	for option in chartOptions:
		if size == option:
			if option == "Tiny": # 10 rectangles
				DrawRectangles(10)
			elif option == "Small": # 20 rectangles
				DrawRectangles(20)
			elif option == "Medium": # 30 rectangles
				DrawRectangles(30)
			elif option == "Large": # 50 rectangles
				DrawRectangles(50)
			else:                   # 100 rectangles
				DrawRectangles(100)






##################### CONTROL ROW #####################

# Create frame that will house the controls
controlFrame = tk.Frame(master = window, height = 50, width = 50, relief = "groove", bd = 5, bg = "gray29")
# Create 3 columns; one for each control. Ensures each widget is equidistant and moves in unison
controlFrame.columnconfigure(0, weight = 1, minsize = 100)
controlFrame.columnconfigure(1, weight = 1, minsize = 100)
controlFrame.columnconfigure(2, weight = 1, minsize = 100)
controlFrame.rowconfigure(0, weight = 0, minsize = 50)
# Creates drop down menu for sorting algorithms
sortVar = tk.StringVar() #established string variable
sortVar.set(sortOptions[0]) #sets first selected variable
controlSortOption = tk.OptionMenu(controlFrame, sortVar, *sortOptions)
controlSortOption.config(bg = "gray29")
# Creates drop down for size of chart (number of columns)
chartVar = tk.StringVar() #established string variable
chartVar.set(chartOptions[0]) #sets first selected variable
controlChartOption = tk.OptionMenu(controlFrame, chartVar, *chartOptions, command = GetRectangles)
controlChartOption.config(bg = "gray29")
# Button that starts sort when clicked
controlButton = tk.Button(master = controlFrame, text = "SORT", command = StartSort, width = 10, highlightbackground = "gray29")
# Place each item in CONTROLFRAMES rows and columns
controlSortOption.grid(row = 0, column = 0)
controlChartOption.grid(row = 0, column = 1)
controlButton.grid(row = 0, column = 2)
# Places frame in WINDOWS row0 column0
controlFrame.grid(row = 0, column = 0, sticky = "nsew")






window.update()
window.lift()
window.attributes('-topmost', True)
window.attributes('-topmost', False)
GetRectangles(chartVar.get())
window.mainloop()
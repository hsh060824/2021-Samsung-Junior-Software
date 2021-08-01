root = tk.Tk()
root.geometry("400x240")

def getTextInput():
	global name
	name = textExample.get("1.0","end")
	print(name)
	ConfScheduler()

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", command=getTextInput)

btnRead.pack()

root.mainloop()

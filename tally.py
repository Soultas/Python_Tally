from tkinter import *

root = Tk()

root.tally_counter=0
root.row_counter=0
root.geometry('350x200')
root.title('Tally counter app')


def add_tally():
	root.tally_counter += 1
	tally_label['text'] = 'Row: ' + str(root.row_counter) + ' Tally: ' + str(root.tally_counter)
def minus_taly():
	root.tally_counter -=1
	tally_label['text']='Row: '+ str(root.row_counter)+ ' Tally: ' + str(root.tally_counter)
	if root.tally_counter <= 0:
		root.tally_counter = 0
		tally_label['text'] = 'Row: ' + str(root.row_counter) + ' Tally: ' + str(root.tally_counter)

def button_reset():
	root.tally_counter=0
	root.row_counter=0
	tally_label['text'] = 'Row: ' + str(root.row_counter) + ' Tally: ' + str(root.tally_counter)

def add_row():
	root.row_counter += 1
	root.tally_counter = 0
	tally_label['text'] = 'Row: ' + str(root.row_counter) + ' Tally: ' + str(root.tally_counter)

row_add = Button(root, text="Add Row",command=add_row)
row_add.pack()

reset_button = Button(root, text="Reset", command=button_reset)
reset_button.pack()

tally_minus = Button(root,height=10,width=5,text="-1",command=minus_taly)
tally_minus.pack(side=LEFT)

tally_add = Button(root,height=10,width=5, text="+1", command=add_tally)
tally_add.pack(side=RIGHT)


tally_label = Label(root, text="No tallys yet.")
tally_label.pack()

root.mainloop()
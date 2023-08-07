import tkinter

# initialize new object from this class
window = tkinter.Tk()

# # need to keep window open so use while loop, built in as main loop
# keep at bottom of code
# window.mainloop()

window.title("My first GUI")
window.minsize(width = 400, height = 300)
window.config(padx=20, pady=20)

# create a label using the label class
# things wont show up without specifyin ghow it will be displayed
my_label = tkinter.Label(text="I am a label", font = ("arial", 24, "italic"))
# pack places things into screen in center
my_label.grid(column=0,row=0)
# pack comes with its own set of arguments
# my_label.pack(expand=True)
# pack does not show all arguments available in documentation: **kw
my_label.config(padx=0, pady=100)

# how to change label text:
# my_label["text"] = "New Text"
# pass in new text as keyword argument
# my_label.config(text='New Text')

def button_clicked():
  my_label.config(text=input.get())
  # my_label.config(text='I was clicked')
  # print("I was clicked")

# when button detects command, triggers this method, no () because we only want to call the function when the button is clicked
button = tkinter.Button(text= 'click me', command=button_clicked)
button.grid(column=1,row=1)

another_button = tkinter.Button(text="new butt")
another_button.grid(column=3,row=0)

# entry component
input = tkinter.Entry()
input.grid(column=4,row=3)
# get() returns entry string

window.mainloop()

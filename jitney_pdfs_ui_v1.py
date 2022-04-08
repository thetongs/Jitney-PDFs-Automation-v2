# Load Libraries
import os
import shutil
from tkinter import *
from PIL import ImageTk
from tkinter import filedialog,messagebox
from pdf_travel_service import pdf_hunting


root = Tk()
root.geometry("243x250")
root.title('Jitney-PDFs')
root.resizable(0, 0)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

path = resource_path("pdf_jitney_background_ui.png")
img = PhotoImage(file = path, master= root)

# img = PhotoImage(file='XLS.png', master= root)
img_label = Label(root, image = img)
img_label.place(x = 0, y = 0)

s_filepath = ""
d_filepath = ""

# Select Source Path
def s_open_file():
    global s_filepath

    s_filepath = filedialog.askdirectory()
    if(s_filepath):
        # messagebox.showinfo('Information','File Selected')
        source_button.configure(bg = 'light green')
    else:
        messagebox.showwarning('Warning','Source Folder Not Selected')
        source_button.configure(bg = 'red')

# Select Destination Path
def d_open_file():
    global d_filepath

    d_filepath = filedialog.askdirectory()
    if(d_filepath):
        # messagebox.showinfo('Information','Destination Selected')
        destination_button.configure(bg='light green')
    else:
        messagebox.showwarning('Warning','Destination Folder Not Selected')
        destination_button.configure(bg='red')

# 
def pdf_automation():
    if(s_filepath and d_filepath):
        # messagebox.showinfo('Information',s_filepath)
        # messagebox.showinfo('Information',d_filepath)
        n_files = pdf_hunting(s_filepath, d_filepath)
        
        if(n_files == 0):
            messagebox.showwarning('Warning','Zero Files In Source Folder.')
        else:
            messagebox.showinfo('Information',"""Task Completed 
            Total Files Copied : {}
            """.format(n_files))
    else:
        messagebox.showwarning('Warning','Please Select Source and Destination.')

    root.destroy()

# 
def user_manual():
    messagebox.showinfo('User Manual', """Step 1 - Select Source Base Folder
Which Contains PDF Files.

Step 2 - Select Destination Folder
Select destination folder. In this folder we are storing all PDF Files.

Step 3 - Click Action
Perform PDF Traveling Operation.

[Window Will Be Close After Step 3]

Note 
1. User Manual 
    Will give you user manual of application.
""")

# Label - Branding
signature = Label(root, text = "vConstruct-DPR", bg = 'red', fg = 'white')
signature.place(x = 78, y = 205)

# Label - Kishan
signature = Label(root, text = "Kishan T")
signature.place(x = 191, y = 230)

# Create a Button - User Manual 
user_manual = Button(root, text = "User Manual", command = user_manual)
user_manual.place(x = 85, y = 227)

# Create a Button - Take Source File
source_button = Button(root, text="Source", command = s_open_file)
source_button.place(x = 98, y = 50)

# Create a Button - Select Destination Path
destination_button = Button(root, text="Destination", command = d_open_file)
destination_button.place(x = 87, y = 85)

action_button = Button(root, text = "Action", command = pdf_automation)
action_button.place(x = 100, y = 120)

messagebox.showinfo('User Manual', """Step 1 - Select Source Base Folder
Which Contains PDF Files.

Step 2 - Select Destination Folder
Select destination folder. In this folder we are storing all PDF Files.

Step 3 - Click Action
Perform PDF Traveling Operation.

[Window Will Be Close After Step 3]

Note 
1. User Manual 
    Will give you user manual of application.
""")


root.mainloop()
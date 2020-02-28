# Unique Folder Creator using Tkinter dialog

"""
OVERVIEW:
This was intended to be run on Windows 10.
To enable development to continue I am working with this on Mac also.
While developing this I would create a temp folder under /Users/Shared typically just called 9999
  with a sub-folder called '3 WIP'
Then when I ran the code I would input 9999 and check the folder where successfully generated.
So far they are.
"""

from tkinter import *
import os

root = Tk()
root.title('Unique Folder Creator')  # Sets the dialog title

root.geometry("400x175")  # Sets the physical size of the dialog box

myLabel0 = Label(root, wraplength=280, text="Enter Project Number: > ")
myLabel0.pack()
myLabel0.place(x=15, y=25)  # Sets the pos of the TEXT on canvas

e = Entry(root, width=20, borderwidth=1)  # Entry creates an INPUT BOX on the canvas
e.pack()  # Removed >> e.insert(0)  # Default txt in Entry field removed 'Enter...'
e.place(x=175, y=25)  # Sets the pos of the INPUT BOX on canvas

if len(e.get()) == 0:  # Check if the Input Box is empty
    myLabel4 = Label(root, wraplength=280, fg="Red", text="The INPUT BOX is Empty!")
    myLabel4.pack()
    myLabel4.place(x=15, y=145)  # Sets the pos of the TEXT on canvas

myLabel1 = Label(root, wraplength=280, text= \
    "Customer Project Folders will be created under '3 WIP' under the Project selected ")
myLabel1.pack()
myLabel1.place(x=15, y=95)  # Sets the pos of the TEXT on canvas

main = ["1.0  Problem Understanding",
        "2.0  Design Definition",
        "3.0  Design Approval",
        '4.0  Buy-Off',
        '5.0  Technical Risk',
        '6.0  Electronic Storage',
        '7.0  Design History']

sub0 = ['1.01 Requirements-System Engineering Documents']

sub1 = ['2.01 SIR (Europe) - Assembly Drawings (US)',
        '2.02 Design Definition Drawing',
        '2.03 DDR']

sub2 = ['3.01 Design Technical Approval Document',
        '3.02 Product System approval',
        '3.03 Sub-system approval',
        '3.04 Component approval',
        '3.05 Stress Reports',
        '3.06 IPPR Milestone Sign-off Sheet']

sub3 = ['4.01 Manufacturing acceptance - Component',
        '4.02 Manufacturing acceptance - Assembly',
        '4.03 Manufacturing acceptance - Overhaul']

sub4 = ['5.01 DFMEA',
        '5.02 Robust Design evidence',
        '5.03 Verification Strategy',
        '5.04 FMECA  associated material']

sub5 = ['6.01 Computer References',
        '6.02 Layer List',
        '6.03 Check-Mate output',
        '6.04 Part Item Log Sheet']

sub6 = ['7.01 Interface Control Documentation (ICD)',
        '7.02 Communication Sheets',
        '7.03 Engineering Coordination Momos (ECMs)',
        '7.04 Calculations',
        '7.05 Notes',
        '7.06 Sketches',
        '7.07 Alternative Solutions',
        '7.08 Supply Chain Proforma',
        '7.09 Design for Manufacture',
        '7.10 Design for Assembly',
        '7.11 Design for Aftermarket',
        '7.12 Previous Designs - Lessons Learnt Logs',
        '7.13 Patents']


def createFolders():
    rootPath = r'/Users/Shared/' + e.get() + '/3 WIP'

    try:

        for f in main:  # Main folders
            os.mkdir(os.path.join(rootPath, f))  # create parent folders

        for s in sub0:  # Sub-dir 1
            os.mkdir(os.path.join(rootPath, main[0], s))

        for s in sub1:  # Sub-dir 2
            os.mkdir(os.path.join(rootPath, main[1], s))

        for s in sub2:  # Sub-dir 3
            os.mkdir(os.path.join(rootPath, main[2], s))

        for s in sub3:  # Sub-dir 4
            os.mkdir(os.path.join(rootPath, main[3], s))

        for s in sub4:  # Sub-dir 5
            os.mkdir(os.path.join(rootPath, main[4], s))

        for s in sub5:  # Sub-dir 6
            os.mkdir(os.path.join(rootPath, main[5], s))

        for s in sub6:  # Sub-dir 7
            os.mkdir(os.path.join(rootPath, main[6], s))

        myLabel3 = Label(root, wraplength=280, fg="Blue", text="Folders Created Successfully")
        myLabel3.pack()
        myLabel3.place(x=15, y=145)  # Sets the pos of the TEXT on canvas

        exit()

    except OSError:
        myLabel2 = Label(root, wraplength=280, fg="Red", text="FOLDER EXISTS")
        myLabel2.pack()
        myLabel2.place(x=15, y=145)  # Sets the pos of the TEXT on canvas


myButton = Button(root, text='Create Folders', command=createFolders, fg="blue")  # Omit () from 'COMMAND'
myButton.pack()
myButton.place(x=110, y=55)  # Sets the pos of the BUTTON on canvas

root.mainloop()  # Keeps in a loop to remains visible.

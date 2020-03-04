# Unique Folder Creator using Tkinter dialog
"""
--- WORK IN PROGRESS as of 4th Marc 2020 ---
Created by David Ponder, 2020 with thanks and help of the Real Python community.
"""
from tkinter import *
import os

# NOTES:
"""
Background:
- Originally created for Windows 10.
- To enable parallel development and testing work has been continue on Mac.

Overview:
- An app was required by Users to create a set of pre-defined project folders and sub-folders.
- Named in two lists below called 'main and subs' respectively.

Basic Intended Use Case:
- User starts the Python app from a batch file in the main folder called PROJECTS
- User enters a valid project number
- Clicks the Button 'Create Folders' or presses 'Enter'
- Folders & Sub-folders are created.
- Message displays on dialog 'Folders Created Successfully'
- If No or Invalid Project number is entered;
- Respective Error Msg is displayed.

Setup to Test Code:
- While developing this a temp folder is created under /Users/Shared
  typically just called 9999 with a sub-folder called '3 WIP'
- When running the code, input 9999, then check that all folders/sub-folders where successfully created.
- As of test this version (on Mac) Mar, 4 - 2020 the basic folder creation works for the initial test.

Know Bugs:
- Error presents if folders exist, to be fixed.

"""

root = Tk()
root.title('Unique Folder Creator')  # Sets the dialog title

root.geometry("400x175")  # Sets the physical size of the dialog box

myLabel0 = Label(root, wraplength=280, text="Enter Project Number: > ")
myLabel0.pack()
myLabel0.place(x=15, y=25)  # Sets the pos of the TEXT on canvas

e = Entry(root, width=20, borderwidth=1)  # Entry creates an INPUT BOX on the canvas
e.pack()  # Removed >> e.insert(0) which sets default txt in Entry field removed 'Enter...'
e.place(x=175, y=25)  # Sets the pos of the INPUT BOX on canvas

if len(e.get()) == 0:  # Check if the Input Box is empty
    myLabel1 = Label(root, wraplength=280, fg="Red", text="The INPUT BOX is Empty!")
    myLabel1.pack()
    myLabel1.place(x=15, y=145)  # Sets the pos of the TEXT on canvas

myLabel2 = Label(root, wraplength=280, text= \
    "Customer Project Folders will be created under '3 WIP' under the Project selected ")
myLabel2.pack()
myLabel2.place(x=15, y=95)  # Sets the pos of the TEXT on canvas

# Main/Top level folders
main = ["1.0  Problem Understanding",
        "2.0  Design Definition",
        "3.0  Design Approval",
        '4.0  Buy-Off',
        '5.0  Technical Risk',
        '6.0  Electronic Storage',
        '7.0  Design History']

# Unique sub-folders for each respective Main/Top Level folder
subs = [
    ['1.01 Requirements-System Engineering Documents'],
    ['2.01 SIR (Europe) - Assembly Drawings (US)',
     '2.02 Design Definition Drawing',
     '2.03 DDR'],
    ['3.01 Design Technical Approval Document',
     '3.02 Product System approval',
     '3.03 Sub-system approval',
     '3.04 Component approval',
     '3.05 Stress Reports',
     '3.06 IPPR Milestone Sign-off Sheet'],
    ['4.01 Manufacturing acceptance - Component',
     '4.02 Manufacturing acceptance - Assembly',
     '4.03 Manufacturing acceptance - Overhaul'],
    ['5.01 DFMEA',
     '5.02 Robust Design evidence',
     '5.03 Verification Strategy',
     '5.04 FMECA  associated material'],
    ['6.01 Computer References',
     '6.02 Layer List',
     '6.03 Check-Mate output',
     '6.04 Part Item Log Sheet'],
    ['7.01 Interface Control Documentation (ICD)',
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
]


def createFolders():
    rootPath = r'/Users/Shared/' + e.get() + '/3 WIP'

    try:

        for root, sub in zip(main, subs):  # Main folders
            os.mkdir(os.path.join(rootPath, root))  # create parent folders
            for s in sub:  # Sub-dirs
                os.mkdir(os.path.join(rootPath, root, s))

    except FileExistsError:
        myLabel3 = Label(root, wraplength=280, fg="Red", text="FOLDER EXISTS")
        myLabel3.pack()
        myLabel3.place(x=15, y=145)  # Sets the pos of the TEXT on canvas


myLabel4 = Label(root, wraplength=280, fg="Blue", text="Folders Created Successfully")
myLabel4.pack()
myLabel4.place(x=15, y=145)  # Sets the pos of the TEXT on canvas

myButton = Button(root, text='Create Folders', command=createFolders, fg="blue")  # Omit () from 'COMMAND'
myButton.pack()
myButton.place(x=110, y=55)  # Sets the pos of the BUTTON on canvas

root.mainloop()  # Keeps in a loop to remains visible.

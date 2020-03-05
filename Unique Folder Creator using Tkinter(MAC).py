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
- none
"""
# REVISIONS:
'''
Thu, 5 Mar 2020
_______________
 X  = Implemented
 W  = WIP
[ ] = Planned
*** = Error Occurred After Implementation, Other Features Affected
____________________________________________________________
[X] Solved various bugs and introduced some improvements.
[X] Created the following new function blocks further up in the prog structure:
    - checkInputBox
    - foldersCreatedMsg  
    - foldersExistMsg
[X] Reordered and moved all functions and list to top of structure.
[X] Bound the ENTER key to the User Input box to call createFolders func.
[X] Center align the Button and Information text on the dialog.
[X] Fix Button colour
[X] Make msg for FOLDERS EXISTING font = BOLD, colour = Red
[X] Make dialog size FIXED (Non-resizable)
[X] Add 'focus' to the dialog Input box to control the default & entry text properties
    Set the default text to light grey when the dialog has no focus.
    Clear the input box when selected with cursor
    Set text entered to black colour.
[X] Set 5 second Timeout to close dialog after either even occurs:
    - The Create Folders button is pressed
    - The ENTER key is pressed. 
[ ] When inputting additional project numbers, do the following.
    Delete previous message (Success / Fail) once first project number has been processed.
*** Currently there is overlap with 2 messages appearing in the same pos without the prev being deleted.    
[W] For inputting 'any' Project Number -- Validate, check folder path exists:
    Check in two stages, check using a:
    [X] FULL path match
    [ ] PARTIAL match using one of the following combinations:
        - \d{3}.
        - \d{4}.
        - \w{3}\d{4}.
    Include Error Handling for non-existent folders(projects)
'''


# Check if Input box is empty when Button / Enter key pressed.
def checkInputBox():
    if len(e.get()) == 0:
        myLabel1 = Label(root, wraplength=280, fg="Red", text="The INPUT BOX is Empty!")
        myLabel1.pack()
        myLabel1.place(x=xPos, y=yPos)


# Message displays when folders are successfully created (label on dialog).
def foldersCreatedMsg():
    myLabel2 = Label(root, wraplength=280, fg="Blue", text="Folders Created Successfully",
                     font="none 16 bold")
    myLabel2.pack()
    myLabel2.place(x=xLen/2, y=yPos, anchor="center")

    closeDialog()


# Message displays if folder(project) already exists (label on dialog).
def foldersExistMsg():
    myLabel3 = Label(root, wraplength=280, fg="Red", text="FOLDER(S) EXISTS", font="none 16 bold")
    myLabel3.pack()
    myLabel3.place(x=xLen/2, y=yPos, anchor="center")

    closeDialog()


def folderMissing():
    myLabel4 = Label(root, wraplength=280, fg="Red", text="Required PROJECT Folder is MISSING",
                     font="none 16 bold")
    myLabel4.pack()
    myLabel4.place(x=xLen / 2, y=yPos, anchor="center")

    closeDialog()


# Create main and sub-folders
def createFolders(*args):
    rootPath = r'/Users/Shared/' + e.get() + '/3 WIP'

    checkInputBox()  # Check for User Input

    try:
        if os.path.isdir(rootPath):
            for rt, sub in zip(main, subs):  # Main folders
                os.mkdir(os.path.join(rootPath, rt))  # Create parent folders
                for s in sub:  # Create Sub-dirs
                    os.mkdir(os.path.join(rootPath, rt, s))

            foldersCreatedMsg()  # Displays msg that folder have been created

        else:
            folderMissing()  # Displays msg that the target folder has not been found

    except FileExistsError:  # Error Handling if folder already exists
        foldersExistMsg()


# Make entry box text 'black' when dialog has 'focus'
def handle_focus_in(_):
    e.delete(0, END)
    e.config(fg='black')


# Make entry box text 'grey' when dialog has no 'focus'
def handle_focus_out(_):
    e.delete(0, END)
    e.config(fg='grey')
    e.insert(0, "Enter the Project Number")


# After EVENT (Button / Enter key) Start 5 second timer to close dialog.
def closeDialog(*args):
    root.after(3000, root.destroy)  # 3000 = 3 seconds


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

# Dialog size
xLen = 400
yLen = 200

# Common Label position for msgs on dialog
xPos = 15
yPos = 180

# Initialises dialog and sets dialog name on top border
root = Tk()
root.title('Unique Folder Creator')

# Defines physical size of FIXED (non-resizable) dialog box
root.geometry("400x200")
root.resizable(False, False)

# Controls 'Helper' text appearance in input box
root.bind("<FocusIn>", handle_focus_in)
root.bind("<FocusOut>", handle_focus_out)

# Information label informing user where folders will be created.
myLabel2 = Label(root, wraplength=280,
                 text="Customer Project Folders will be created under '3 WIP' under the Project selected ",
                 font=('Helvetica', 14))
myLabel2.pack()
myLabel2.place(x=xLen/2, y=135, anchor="center")  # Sets the pos

# Creates Input box for user entry
e = Entry(root, width=20, borderwidth=2, font=('Helvetica', 14))
e.bind("<Return>", createFolders)  # Bind ENTER key to func 'createFolders' NB: Omit () from func call.
# e.bind("<Return>", closeDialog)  # Triggers 5 sec countdown timer to close dialog, omit () from func call.
e.insert(0, "Enter the Project Number")
e.pack()  # Removed >> e.insert(0) which sets default txt in Entry field removed 'Enter...'
e.place(x=xLen/2, y=25, anchor="center")  # Sets the pos

# Dialog Button to create folders
myButton = Button(root, text='Create Folders', command=createFolders, fg="black", highlightbackground='yellow',
                  font=('Helvetica', 20))  # Omit () from 'COMMAND'
myButton.pack()
myButton.place(x=xLen/2, y=80, anchor="center")

root.mainloop()  # Keeps in a loop to remains visible.

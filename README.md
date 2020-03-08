# Unique Folder Creator

## Basic Overview / Purpose of the App
A pre-defined set of folders are required to be created in the sub-folder '3 WIP' under some existing project folders.
The app creates 7 Top level folders eg:
- 1.0 INPUTS
- 2.0 WORK
- 3.0 OUTPUT

After which each of the above top level folders has a unique sub-folder eg:

Under folder 1.0 INPUTS
- 1.1 Financial
- 1.2 Standards
- 1.3 Requirements

Under folder 2.0 WORK
- 2.1 WIP
- 2.2 Studies
- 2.3 Images

Under folder 3.0 OUTPUT
- 3.0 Deliverables
- 3.1 Communications
- 3.2 Agreements

## Background
Originally developed to be used on a Windows 10 pc but remote development continues on a Mac.
Hence this version is uses Mac file paths.
Users were originally performing a manual copy /paste from an existing template folder.

The currently developed app using a temp folder '9999' for testing.
The temp folder makes it easier to test the folder creation is working.
Also to check the basic Error Handling for: existing or missing.

For this purpose, the following folder is created:

    /Users/Shared/9999/3 WIP

Notes on Project numbers and structure.
- Regardless of what project number is entered, sub-folder'3 WIP' exist under all project folders. 
- Project number patterns can vary, eg [12345, 1234, abc1234] are general patterns to be expected.

## Basic Intended Use Case
1. User starts the Python app from a batch file in the main folder called PROJECTS
2. User enters a valid project number
3. Clicks the Button 'Create Folders' or presses 'Enter'
4. Folders & Sub-folders are created.
5. Message displays on dialog 'Folders Created Successfully'
6. If No or Invalid Project number is entered;
7. Respective Error Msg is displayed.


## Currently Developed Features
Tkinter dialog with the following functionality
1. Tkinter of set size created.
2. Title added to dialog
3. Input box added, positioned towards top and center
4. Instruction added to left of Input box
5. Button with text 'Create Folders' added directly below Input box
6. User messages positioned below User Info, In BOLD red/blue font.

Basic Error Handling considered / implemented for:
- No user input
- Wrong project number
- Characters entered too small


## Future / Planned Futures to be Implemented
[X] - Check if user entered project number exists

[ ] - Read in folder structure from customer provided .xlsx or .csv file

[ ] - Move all folder from 2.0 WORK to 3.0 OUTPUT

[X] - Accept ENTER key pressed for User entry of Project Number in Input box.
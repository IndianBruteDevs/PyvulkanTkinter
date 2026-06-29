""" vAlpha main-version : v_0.0.1 ;
    Vtkcreotr (VulkanTkinter-Creator) is developed
    keeping a figure of Qt-creator (inspirer) 
    VTkcreator provides a full IDE to make and develop 
    desktop apps using pyvullkantkinter frameowrk
"""
    
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *

root = Tk() 

#dialog class
class DialogBox(Toplevel):
  def __init__(self, dialogparent):
    super().__init__() 
    self.transient(dialogparent)
    self.grab_set() 


#project_panel
class ProjectPanel(DialogBox):
  def __init__(self, mparent):
    super().__init__(mparent) 


projectdialog = ProjectPanel(root)



root.mainloop() 

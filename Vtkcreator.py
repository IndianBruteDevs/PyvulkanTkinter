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
    self.title("Welcome!") 
    self.geometry("500x400") 
    self.create_new = ttk.Button(self, text="Create new project") 
    self.create_new.pack(side=TOP , pady=10)
    self.handleEvents()
    
  def handleEvents(self):
      self.elems = (self.create_new) 
      self.create_new.bind("<Button-1>" , redirect)

def redirect(event=None):
         projectdialog.destroy()
         new_dialog = DialogBox(root)  
         new_dialog.geometry("700x600") 
         new_dialog.title("New project")
          
        
      


projectdialog = ProjectPanel(root)



root.mainloop() 

# PyvulkanTkinter
This a tkinter build and based on tkinter a python module for making a vulkan application with tkinter and pure python (might it's own language called tml and tmlconfig noted as .tcnfg and  .tml) 

# Usage - 
start by installing it by writing in your terminal -

_______________________
Shell
_______________________

pip install pyvulkancreator
pip install vtktools-extratips
pip install pyvulkantkinter

__________________________

now create a new file called `vtkvonfig.tcnfg`
and `creator.tdata.tml`

now write this in the `vtkconfig.tcnfg`

<tcnfg to="vullkantkinter">
  main... (vtkay){
   tcnfg.relate_file("creator.tdata.tml");
   vtk::bundles.create_(); 
  }
  allocate  new vtkBundle **auto new vtklanguageconfigs;
  rmallocation old **default vtkjavaJDK 
  rename(vtkjavaJDK) as pyvtk;
  changeConfigs(pyvtk, configs=[language : "python", stdversion="3.X") 
</tcnfg>

now write the given below text in the `creator.tdata.tml`

<tml typespecification="tdata">
  <tdata>
    <jsonxml>
      {
      
       "name" : "pyvulkantkinter-creator", 
       "status" : "installed" , 
       <data>@hiddendata.tml</data>


      }
    </jsonxml>
  </tdata>
</tml>

now, you are ready to go!! 
now next follow the instructions
 instructions -
 1. open terminal
 2. write "vtk load creator"
 3. click the new icon on the toolbar and tap "New Vtk project"
 4. click next
 5. click "add sample cube code by default"
 6. click "Create project"
 7. click the save icon on the toolbar and save that file
 8. choose python files as defalut extension



now clcik on the run button (a triangle button on the toolbar) and booom! 


for more 
















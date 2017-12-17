import FreeCAD,FreeCADGui,Part

path_to_ui = str(FreeCAD.getUserAppDataDir()) + 'Mod/FreeCAD_Python/ui/task.ui'

class PythonObjectTool():

	def GetResources(self):
		return {'Pixmap'  : 'My_Command_Icon', # the name of a svg file available in the resources
			'Accel' : "Shift+S", # a default shortcut (optional)
			'MenuText': "PythonObject Command",
			'ToolTip' : "PythonObject"}

	def Activated(self):
		obj = makePythonObject()
		FreeCADGui.activeDocument().setEdit(obj.Name,0)

	def IsActive(self):
		return True

class PythonObject:
	def __init__(self, obj):
		obj.addProperty("App::PropertyPythonObject","Script","python script","python script").Script="#fp is current object\nif not 'length' in fp.PropertiesList:\n\
  fp.addProperty('App::PropertyLength','length').length=5.0\n\
fp.Shape = Part.makeBox(fp.length,fp.length,fp.length)\n\
FreeCAD.Console.PrintMessage('makeBox\\n')"
		obj.Proxy = self
		FreeCAD.Console.PrintMessage("init\n")

	def onChanged(self, fp, prop):
		'''Do something when a property has changed'''

	def execute(self, fp):
		exec(fp.Script)
		FreeCAD.Console.PrintMessage("\n")

class PythonObjectViewProvider:

    def __init__(self,vobj):
        vobj.Proxy = self

#    def getIcon(self):
#        return ":/icons/PartDesign_InternalExternalGear.svg"

    def attach(self, vobj):
        self.ViewObject = vobj
        self.Object = vobj.Object

    def setEdit(self,vobj,mode):
        taskd = PythonObjectTaskPanel(self.Object,mode)
        taskd.obj = vobj.Object
        FreeCADGui.Control.showDialog(taskd)
        return True

    def unsetEdit(self,vobj,mode):
        FreeCADGui.Control.closeDialog()
        return

    def __getstate__(self):
        return None

    def __setstate__(self,state):
		return None

class PythonObjectTaskPanel:
	def __init__(self,obj,mode):
		self.obj = obj
		self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
		self.form.textEdit.setPlainText(obj.Script)
		self.form.refreshButton.clicked.connect( self.refresh)

	def refresh(self):
		self.obj.Script = self.form.textEdit.toPlainText()
		FreeCAD.ActiveDocument.recompute()

	def accept(self):
		self.obj.Script = self.form.textEdit.toPlainText()
		FreeCADGui.ActiveDocument.resetEdit()

	def reject(self):
		FreeCADGui.ActiveDocument.resetEdit()

FreeCADGui.addCommand('PythonObjectTool',PythonObjectTool())

def makePythonObject():
	FreeCAD.Console.PrintMessage("makePythonObject\n")
	if FreeCAD.ActiveDocument is None:
		FreeCAD.newDocument("pyObject")
	obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","PythonObject")
	PythonObject(obj)
	PythonObjectViewProvider(obj.ViewObject)
	FreeCAD.ActiveDocument.recompute()
	return obj


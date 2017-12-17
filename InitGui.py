import FreeCAD,FreeCADGui

class PythonObject ( Workbench ):
	"PythonObject Workbench"
	Icon = """
	/* XPM */
static char * python_xpm[] = {
"16 16 76 1",
" 	c None",
".	c #3674A6",
"+	c #3672A4",
"@	c #3671A2",
"#	c #3670A0",
"$	c #366E9D",
"%	c #366D9B",
"&	c #366C99",
"*	c #3B6C93",
"=	c #3573A6",
"-	c #B9CEDF",
";	c #709ABD",
">	c #366A97",
",	c #3673A6",
"'	c #83A8C7",
")	c #5687B1",
"!	c #366FA0",
"~	c #366B97",
"{	c #3672A6",
"]	c #3672A3",
"^	c #3671A1",
"/	c #376FA0",
"(	c #2E74B9",
"_	c #3678AD",
":	c #3676AA",
"<	c #3675A8",
"[	c #366F9F",
"}	c #FFCD3E",
"|	c #FFCB3C",
"1	c #FFCA39",
"2	c #FFC33C",
"3	c #3578AF",
"4	c #3677AD",
"5	c #366A98",
"6	c #FFCD3F",
"7	c #FFCA3A",
"8	c #FFCA37",
"9	c #3678AF",
"0	c #3674A8",
"a	c #386B97",
"b	c #FFCC3F",
"c	c #FFC937",
"d	c #3671A3",
"e	c #366E9E",
"f	c #366E9B",
"g	c #376F99",
"h	c #F4C846",
"i	c #FFC936",
"j	c #3678B0",
"k	c #74948B",
"l	c #FFD651",
"m	c #FFD54F",
"n	c #FFD44C",
"o	c #FFD249",
"p	c #FFD148",
"q	c #FFCF44",
"r	c #FFCE42",
"s	c #3774A8",
"t	c #FFD854",
"u	c #FFD147",
"v	c #3678AE",
"w	c #3780B6",
"x	c #3573A9",
"y	c #FFD044",
"z	c #FFBF40",
"A	c #FFD54C",
"B	c #FFD24A",
"C	c #FFCF42",
"D	c #FFDD78",
"E	c #FFE598",
"F	c #FFD754",
"G	c #FFDF7F",
"H	c #FFE7A3",
"I	c #FFD555",
"J	c #FFCF43",
"K	c #FFD146",
"    .+@#$%&*    ",
"    =-;#$%&>    ",
"    ,')!$%&~    ",
"    {]^/$%&~    ",
"(_:<,+@[$%&~}|12",
"34:<,+@[$%&56|78",
"94:0,+@[$%&ab|7c",
"94:0,+d[efgh6|7i",
"j4:0klmnopqr6|7c",
"94:stlmnouqr6|7i",
"v4:0tlmnouqr6|7i",
"w4:xtlmnouyr6|1z",
"    tlmABuqC    ",
"    tlmnoDEr    ",
"    FlmnoGHr    ",
"    IlmnouJK    "};
"""
	MenuText = "PythonObject"
	ToolTip = "PythonObject workbench"

	def GetClassName(self):
		return "Gui::PythonWorkbench"

	def Initialize(self):
		FreeCAD.Console.PrintMessage("init")
		import core
		self.appendToolbar("My Tools", ["PythonObjectTool"])
		self.appendMenu("My Tools", ["PythonObjectTool"])

FreeCADGui.addWorkbench(PythonObject)

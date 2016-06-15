from tkinter import *
import subprocess


class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

class CoreGUI(object):
    def __init__(self,parent):
        self.parent = parent
        self.InitUI()
        button = Button(self.parent, text="Check Device", command=lambda: self.adb( "devices"))
        button.grid(column=0, row=0, columnspan=1)

    def InitUI(self):
        self.text_box = Text(self.parent, wrap='word', height = 6, width=50)
        self.text_box.grid(column=0, row=10, columnspan = 2, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)

    def adb(self, *args):
        process = subprocess.Popen(['adb.exe', args], stdout=subprocess.PIPE, shell=True)
        print(process.communicate())
        #return x.communicate(stdout)


root = Tk()
gui = CoreGUI(root)


root.mainloop()
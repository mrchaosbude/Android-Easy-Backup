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

    def InitUI(self):
        self.adb_Main()
        self.text_box = Text(self.parent, wrap='word', height = 6, width=50)
        self.text_box.grid(column=0, row=10, columnspan = 2, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)

    def adb_Main(self):
        labelframe = LabelFrame(self.parent, text="ADB Main function:")
        labelframe.grid(column=0, row=0, rowspan=3)

        check_device = Button(labelframe, text="Check Device", command=lambda: self.adb("devices"))
        check_device.pack(padx=2, pady=2)

        reboot = Button(labelframe, text="Reboot Normal", command=lambda: self.adb("reboot"))
        reboot.pack(padx=2, pady=2)

        reboot_recovery = Button(labelframe, text="Reboot Recovery", command=lambda: self.adb("reboot", "recovery"))
        reboot_recovery.pack(padx=2, pady=2)

        reboot_bootloader = Button(labelframe, text="Reboot Bootloader", command=lambda: self.adb("reboot","bootloader"))
        reboot_bootloader.pack(padx=2, pady=2)

    def adb(self, *args):#übergiebt die befehle an adb
        process = subprocess.Popen(['adb.exe', args], stdout=subprocess.PIPE, shell=True)
        print(process.communicate())
        #return x.communicate(stdout)


root = Tk()
gui = CoreGUI(root)


root.mainloop()
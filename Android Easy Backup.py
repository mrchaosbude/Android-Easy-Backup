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
        self.adb_backup()
        self.adb_test()
        self.text_box = Text(self.parent, wrap='word', height = 6, width=50)
        self.text_box.grid(column=0, row=10, columnspan=4, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)

    def adb_Main(self):
        adbmain_frame = LabelFrame(self.parent, text="ADB Main function:")
        adbmain_frame.grid(column=0, row=0, rowspan=1)

        check_device = Button(adbmain_frame, text="Check Device", command=lambda: self.adb("devices"))
        check_device.pack(padx=2, pady=2)

        reboot = Button(adbmain_frame, text="Reboot Normal", command=lambda: self.adb("reboot"))
        reboot.pack(padx=2, pady=2)

        reboot_recovery = Button(adbmain_frame, text="Reboot Recovery", command=lambda: self.adb("reboot", "recovery"))
        reboot_recovery.pack(padx=2, pady=2)

        reboot_bootloader = Button(adbmain_frame, text="Reboot Bootloader", command=lambda: self.adb("reboot","bootloader"))
        reboot_bootloader.pack(padx=2, pady=2)

    def adb_test(self):
        adbBackup_frame = LabelFrame(self.parent, text="Backup:")
        adbBackup_frame.grid(column=1, row=0, rowspan=1)

        check_device = Button(adbBackup_frame, text="Check Device", command=lambda: self.adb("devices"))
        check_device.pack(padx=2, pady=2)

    def adb_backup(self):
        adbBackup_frame = LabelFrame(self.parent, text="Backup:")
        adbBackup_frame.grid(column=2, row=0, rowspan=1)

        check_device = Button(adbBackup_frame, text="Check Device", command=lambda: self.adb("devices"))
        check_device.pack(padx=2, pady=2)



    def adb(self, *args):#übergiebt die befehle an adb
        process = subprocess.Popen(['adb.exe', args], stdout=subprocess.PIPE, shell=True)
        print(process.communicate())
        #return x.communicate(stdout)


root = Tk()
gui = CoreGUI(root)


root.mainloop()
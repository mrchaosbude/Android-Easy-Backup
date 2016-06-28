import os
from tkinter import *
from tkinter import messagebox
import subprocess
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.ttk import Combobox
import threading

import time
from past.types import basestring

import adbExist

buttonw = "15"

class adb(object):
    def __init__(self, args, firdt_print_text="", after_print_text=""):
        t = threading.Thread(target=self.adb2, args=(args, firdt_print_text, after_print_text))
        t.start()

    def adb2(self, args, firdt_print_text="", after_print_text=""):
        print(firdt_print_text + "\n")
        command = ["adb.exe ", ]
        if isinstance(args, basestring) == True:
            command.append(args)
        else:
            command = command + args
        #print(command) #only  for testing
        try:
            out_bytes = subprocess.check_output([command, ] )
        except subprocess.CalledProcessError as e:
            out_bytes = e.output  # Output generated before error
            code = e.returncode  # Return code
        out_text = out_bytes.decode('utf-8')
        print(out_text)
        print(after_print_text + "\n")

    def adb(self, *args):  # übergiebt die befehle an adb
        process = subprocess.Popen(['adb.exe', args], stdout=subprocess.PIPE, shell=True)
        print(process.communicate())
        # return x.communicate(stdout)

class StdoutRedirector(object):
    def __init__(self ,text_widget):
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
        self.adb_device_info()

        #root.bind('<Escape>', lambda e: root.destroy()) # esc kill the window
        root.protocol("WM_DELETE_WINDOW", self.on_exit) # ask for exit

        self.scrollbar = Scrollbar(self.parent)
        self.scrollbar.grid(column=4, row=10, sticky=N+S )


        self.text_box = Text(self.parent, wrap='word', yscrollcommand=self.scrollbar.set, height = 10, width=88)
        self.text_box.grid(column=0, row=10, columnspan=4, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)
        self.scrollbar.config(command=self.text_box.yview)
        #self.adb2("start-server", print_text="Service Startet...", )
        adb("start-server", after_print_text="Service Startet...", )

    def on_exit(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            try:
                adb("kill-server", after_print_text="Stop Server" )
            except:
                None
            root.destroy()
            exit()

    def adb_Main(self):
        adbmain_frame = LabelFrame(self.parent, text="ADB Main function:", padx=3, pady=3)
        adbmain_frame.grid(column=0, row=0, rowspan=1)

        check_device = Button(adbmain_frame, text="Check Device", command=lambda: adb("devices"),width=buttonw)
        check_device.pack(padx=2, pady=2)

        reboot = Button(adbmain_frame, text="Reboot", command=lambda: self.comboget(),width=buttonw)
        reboot.pack(padx=2, pady=2)

        global v
        v = StringVar()  # a string variable to hold user selection
        options = ["Normal", "Recovery", "Bootloade"]  # available combobox options
        combo = Combobox(adbmain_frame, textvariable=v, values=options, width=buttonw)
        #combo.bind('<<ComboboxSelected>>', self.comboget)  # binding of user selection with a custom callback
        combo.current(0)  # set as default "option 2"
        combo.pack()

        reboot_recovery = Button(adbmain_frame, text="Start Service", command=lambda: adb("start-server", after_print_text="Service startet"), width=buttonw)
        reboot_recovery.pack(padx=2, pady=2)

        reboot_bootloader = Button(adbmain_frame, text="Stop Service", command=lambda: adb("kill-server", after_print_text="Service Stopt"), width=buttonw)
        reboot_bootloader.pack(padx=2, pady=2)

    def adb_device_info(self):
        adb_device_info_frame = LabelFrame(self.parent, text="Device info:")
        adb_device_info_frame.grid(column=1, row=0, rowspan=1)

        screenshot = Button(adb_device_info_frame, text="Screenshot", command=lambda: self.screenshot(), width=buttonw)
        screenshot.pack(padx=2, pady=2)

        battery_info = Button(adb_device_info_frame, text="Battery info", command=lambda: adb("shell dumpsys battery"), width=buttonw)
        battery_info.pack(padx=2, pady=2)

        wifi_info = Button(adb_device_info_frame, text="Wifi info", command=lambda: adb("shell dumpsys wifi"), width=buttonw)
        wifi_info.pack(padx=2, pady=2)

        cpu_info = Button(adb_device_info_frame, text="CPU info", command=lambda: adb("shell dumpsys cpuinfo"), width=buttonw)
        cpu_info.pack(padx=2, pady=2)

    def adb_backup(self):
        adbBackup_frame = LabelFrame(self.parent, text="Backup:")
        adbBackup_frame.grid(column=2, row=0, rowspan=1)

        backup_all = Button(adbBackup_frame, text="Backup All", command=lambda: adb("backup -all"), width=buttonw)
        backup_all.pack(padx=2, pady=2)

        backup = Button(adbBackup_frame, text="Backup", command=self.getvar, width=buttonw)
        backup.pack(padx=2, pady=2)

        global apk,shared,system
        apk = IntVar()
        Checkbutton(adbBackup_frame, text="Apps", variable=apk).pack(padx=2, pady=2)

        shared = IntVar()
        Checkbutton(adbBackup_frame, text="shared", variable=shared).pack(padx=2, pady=2)

        system = IntVar()
        Checkbutton(adbBackup_frame, text="system", variable=system).pack(padx=2, pady=2)

        restore = Button(adbBackup_frame, text="Restore", command=self.restore_backup, width=buttonw)
        restore.pack(padx=2, pady=2)

    def getvar(self):
        name = asksaveasfilename(initialdir="/", initialfile="backup", filetypes=(("Android backup", ".ab"),), title="Backup", defaultextension=".ab",)

        if apk.get() == 1:
            capk = "-apk"
            cobb= "-obb"
        else:
            capk = "-noapk"
            cobb = "-noobb"

        if shared.get() == 1:
            cshared = "-shared"
        else:
            cshared = "-noshared"

        if system.get() == 1:
            csystem = "-system"
        else:
            csystem = "-nosystem"

        adb_set ="backup %s %s %s %s -all -f %s " %(capk, cobb, cshared, csystem, name)
        adb(adb_set)

    def restore_backup(self):
        filename = askopenfilename(parent=self.parent, filetypes=[('Android backup', '*.ab'), ('allfiles', '*')], title='Select Module')
        command = "backup %s" %(filename)
        adb(command, firdt_print_text="start restore this can tacke a wihle", after_print_text="Finish" )

    def comboget (self): #get the chosen entery from  the combobox and give it to adb
        comboboxv = ""
        if v.get() == "Normal":
            comboboxv = "reboot"
        elif v.get() == "Recovery":
            comboboxv = "reboot recovery"
        elif v.get() == "Bootloade":
            comboboxv = "reboot bootloader"
        else:
            print ("please choose")
        adb(comboboxv)
    def screenshot(self):
        adb("shell screencap -p /sdcard/screen.png")
        time.sleep(3)
        adb("pull /sdcard/screen.png")
        adb("shell rm /sdcard/screen.png")
        os.startfile("screen.png")


adbExist
root = Tk()
root.title('Android Easy Backup')
gui = CoreGUI(root)

root.mainloop()

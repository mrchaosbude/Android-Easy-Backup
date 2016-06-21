import os
import wget
import zipfile
import tkinter as tk

#check file exist
def exist(filename):
    if os.path.exists(filename):
        print("adb.exe exist")
    else:
        dialog()

#download the zip unpack and destroy the dialog
def get_zip():
    root.destroy()
    file_url = "http://forum.xda-developers.com/attachment.php?attachmentid=478154&d=1293906896"
    x = wget.download(file_url)
    with zipfile.ZipFile(x, "r") as zip_ref:
        zip_ref.extractall("")
    os.remove(x)
    print("Download finch")


#ask for download the adb
def dialog():
    global root
    root = tk.Tk()
    root.title("ADB Not found")

    label = tk.Label(root, text="Can not find adb.exe should i download it ?")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    button_label = tk.Frame(root)
    button_label.pack(side="bottom", ipadx=10,ipady=10)
    yes = tk.Button(button_label, text="Yes",width=20, command=lambda: get_zip())
    yes.pack(side="left", fill="none", expand=True, padx=2, pady=10 )

    no = tk.Button(button_label, text="no",width=20 , command=lambda: root.destroy())
    no.pack(side="right", fill="none", expand=True, padx=2, pady=10)

    root.mainloop()


#run
exist("adb.exe")

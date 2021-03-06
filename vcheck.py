from threading import Thread
from urllib import request
import tkinter as tk
import webbrowser
import json

version = "0.1.0"

def auto_version_check():
    t = Thread(target=runCheck, args=(True,))
    t.start()

def version_check():
    print("This will only take a moment, please wait!")
    t = Thread(target=runCheck, args=(False,))
    t.start()

def return_version():
    return version

def runCheck(autocheck):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except (OSError, IOError) as e:
        with open('data.json', 'w') as f:
            json.dump(0, f)
            data = 0

    if data == 0:
        vcheck(autocheck)

def vcheck(autocheck):
    req = "http://pick.cetus.uberspace.de/adb/version.json"
    update = request.urlopen(req).read().decode('utf8')
    json_data = json.loads(update)

    currentVersionValue = json_data["version"]

    messageValue = json_data["massage"]

    urlValue = json_data["url"]

    if currentVersionValue != version:
        dialog(messageValue,urlValue, status=True)
    else:
        if autocheck == False:
            dialog(messageValue,urlValue, status=False)

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def dialog(masage,url,status=None):
    global root_vcheck
    root_vcheck = tk.Toplevel()
    root_vcheck.title("Update")
    root_vcheck.resizable(False, False)
    if status == True:
        label = tk.Label(root_vcheck, text=masage)
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        lbl = tk.Label(root_vcheck, text=url, fg="blue", cursor="hand2")
        lbl.pack()
        lbl.bind("<Button-1>", callback)

        button_label = tk.Frame(root_vcheck)
        button_label.pack(ipadx=10, ipady=10)
        yes = tk.Button(button_label, text="Update", width=20,
                        command=lambda: webbrowser.open(url, new=0, autoraise=True))
        yes.pack(side="left", fill="none", expand=True, padx=2, pady=10)

        no = tk.Button(button_label, text="No", width=20, command=lambda: root_vcheck.destroy())
        no.pack(side="right", fill="none", expand=True, padx=2, pady=10)
    else:
        label = tk.Label(root_vcheck, text="You are already running the most up to date version!")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        no = tk.Button(root_vcheck, text="No", width=20, command=lambda: root_vcheck.destroy())
        no.pack( fill="none", expand=True, padx=2, pady=10)

    separator = tk.Frame(root_vcheck, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)

    global donot
    donot = tk.IntVar()
    with open('data.json', 'r') as f:
        data = json.load(f)
    donot.set(data)
    tk.Checkbutton(root_vcheck, text="Don't show this message again!", variable=donot, command=save).pack(side="left",padx=2, pady=2)

    #root_vcheck.mainloop()

def save ():
    with open('data.json', 'w') as f:
        json.dump(donot.get(), f)

    #print ("variable is {0}".format(donot.get()))
if __name__ == '__main__':
    pass
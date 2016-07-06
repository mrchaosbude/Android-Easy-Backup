from urllib import request
from lxml import etree
import tkinter as tk
import webbrowser
import json

version = "0.9.0"


def runCheck():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except (OSError, IOError) as e:
        with open('data.json', 'w') as f:
            json.dump(0, f)
            data = 0

    if data == 0:
        vcheck()

def vcheck():
    req = "http://pick.cetus.uberspace.de/adb/version.xml"
    update = request.urlopen(req).read()

    root_vcheck = etree.XML(update)

    currentVersion = root_vcheck.find(".//currentVersion")
    currentVersionValue = currentVersion.text

    message = root_vcheck.find(".//message")
    messageValue = message.text

    url = root_vcheck.find(".//url")
    urlValue = url.text

    if currentVersionValue != version:
        dialog(messageValue,urlValue, status=True)
    else:
        dialog(status=False)

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def dialog(masage,url,status=None):
    global root_vcheck
    root_vcheck = tk.Toplevel()
    root_vcheck.title("Update")
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
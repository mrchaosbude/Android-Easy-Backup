from urllib import request
from lxml import etree
import tkinter as tk
import webbrowser

version = "0.9.0"

def vcheck():
    req = "http://pick.cetus.uberspace.de/adb/version.xml"
    update = request.urlopen(req).read()

    root = etree.XML(update)

    currentVersion = root.find(".//currentVersion")
    currentVersionValue = currentVersion.text

    message = root.find(".//message")
    messageValue = message.text

    url = root.find(".//url")
    urlValue = url.text

    if currentVersionValue != version:
        dialog(messageValue,urlValue, status=True)
    else:
        dialog(status=False)

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def dialog(masage,url,status=None):
    global root
    root = tk.Tk()
    root.title("Update")
    if status == True:
        label = tk.Label(root, text=masage)
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        lbl = tk.Label(root, text=url, fg="blue", cursor="hand2")
        lbl.pack()
        lbl.bind("<Button-1>", callback)
        button_label = tk.Frame(root)
        button_label.pack(side="bottom", ipadx=10, ipady=10)
        yes = tk.Button(button_label, text="Update", width=20,
                        command=lambda: webbrowser.open(url, new=0, autoraise=True))
        yes.pack(side="left", fill="none", expand=True, padx=2, pady=10)

        no = tk.Button(button_label, text="No", width=20, command=lambda: root.destroy())
        no.pack(side="right", fill="none", expand=True, padx=2, pady=10)
    else:
        label = tk.Label(root, text="You are already running the most up to date version!")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        no = tk.Button(root, text="No", width=20, command=lambda: root.destroy())
        no.pack( fill="none", expand=True, padx=2, pady=10)

    separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)
    donot = tk.IntVar()
    tk.Checkbutton(root, text="Don't show this message again!", variable=donot).pack(side="left",padx=2, pady=2)

    root.mainloop()

vcheck()
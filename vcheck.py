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
        print (messageValue)
        print (urlValue)
        dialog(messageValue,urlValue)

def dialog(masage,url):
    global root
    root = tk.Tk()
    root.title("Update")

    label = tk.Label(root, text=masage)
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    label_1 = tk.Label(root, text=url)
    label_1.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    button_label = tk.Frame(root)
    button_label.pack(side="bottom", ipadx=10,ipady=10)
    yes = tk.Button(button_label, text="Update",width=20, command=lambda: webbrowser.open(url, new=0, autoraise=True))
    yes.pack(side="left", fill="none", expand=True, padx=2, pady=10 )

    no = tk.Button(button_label, text="No",width=20 , command=lambda: root.destroy())
    no.pack(side="right", fill="none", expand=True, padx=2, pady=10)

    root.mainloop()

vcheck()
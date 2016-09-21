from tkinter import *
import json

version = {"version": "", "massage" : "", "url" : ""}

def write_json():
    version["version"] = e1.get()
    version["massage"] = e2.get()
    version["url"] = e3.get()
    js= json.dumps(version)
    with open('version.json', 'w') as f:
        f.write(js)

def load_json():
    try:
        with open('version.json', 'r') as f:
            data = json.load(f)
            print(data)
    except (OSError, IOError) as e:
        print("no file")



master = Tk()
Label(master, text="Version").grid(row=0)
Label(master, text="Massage").grid(row=1)
Label(master, text="Url").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
#e1.insert(10,"Miller")
#e2.insert(10,"Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Save', command=write_json).grid(row=3, column=0, sticky=W, pady=4, padx=4)
Button(master, text='Show', command=load_json).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=E, pady=4, padx=4)

mainloop( )
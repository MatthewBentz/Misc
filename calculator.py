#!/usr/bin/python

import tkinter as tk

# Instatiate the window w/ default size
window = tk.Tk()
window.geometry("400x215")
window.title("Address Entry Form")
window.minsize(width=400, height=215)

# Label and entry frame
frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frame.pack(fill=tk.X)

# Entry resizing
frame.columnconfigure(1, weight=1)

# Labels for form
entries = ["First Name:", "Last Name:", "Address Line 1:", "Address Line 2:",
           "City:", "State/Province:", "Postal Code:", "Country:"]

# Add labels and entries in frame for each row
for row in range(0, len(entries)):

    label = tk.Label(master=frame, text=entries[row])
    label.grid(row=row, column=0, sticky="e")

    entry = tk.Entry(master=frame, width=50)
    entry.grid(row=row, column=1, sticky="ew")

# Buttons frame
btn_frame = tk.Frame(master=window)
btn_frame.pack(fill=tk.BOTH, padx=10, pady=5)

btn_submit = tk.Button(master=btn_frame, text="Submit", height=2, width=10)
btn_submit.pack(side=tk.RIGHT)

btn_clear = tk.Button(master=btn_frame, text="Clear", height=2, width=10)
btn_clear.pack(side=tk.RIGHT, padx=10)

window.mainloop()

#! /usr/bin/env python
import requests
import ttkbootstrap as ttk

API_KEY = "iE6syJ1PrdZ8B1FBDQ5RcDLllJMngXYMpfT7p98S"
API = "https://api.api-ninjas.com/v2/randomquotes"
HEADERS = {"X-Api-Key": API_KEY}

# Functionality

# GUI
WIDTH = 1366
HEIGHT = 768
SCALING = 0.7
MAX_WRAP = 500
root = ttk.Window(themename='journal')
root.title("Random Quotes Generator")
root.geometry(f"{int(WIDTH * SCALING)}x{int(HEIGHT * SCALING)}")

label = ttk.Label(
        master=root, text="", font="IosevkaNerdFont 12",
        wraplength=int(WIDTH * SCALING) - 40, justify='center',
        )
label.pack(side='top')

def get_new_quote():
    try:
        data = requests.get(url=API,headers=HEADERS)
        data.raise_for_status()
        datajs = data.json()
        quote = datajs[0]["quote"]
        author = datajs[0]["author"]
        label.config(text=f"{quote} - {author}")
    except (requests.RequestException, KeyError, IndexError) as e:
        label.config(text=f"Error fetching quote: {e}")

    root.update_idletasks()
    root.geometry("")

frame = ttk.Frame(master=root)
button = ttk.Button(master=frame, text='Generate', command=get_new_quote)
button.pack(pady=10)
frame.pack(side='bottom')

get_new_quote()

root.mainloop()

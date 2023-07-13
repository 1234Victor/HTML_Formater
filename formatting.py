from bs4 import BeautifulSoup

def convert(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
         
    non_tag_texts = soup.find_all(text=True, recursive=True, limit=None)
    for text in non_tag_texts:
        if text.strip():  # Exclude empty strings
            if text.parent.name == '[document]' and not text.isspace():  # Exclude spaces
                # Create a new <span> tag and wrap the text with it
                span_tag = soup.new_tag('span')
                text.wrap(span_tag)

    # Change font color for headers, <ul> elements, text elements, and links
    elements_to_change_color = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'li', 'p', 'span', 'div', 'strong']

    for element in soup.find_all(elements_to_change_color):
        element['style'] = 'color: black; font-size:14px;'

    links = soup.find_all('a')
    for link in links:
        link['style'] = 'color: #1F55C1; font-size:14px;' 
        link.wrap(soup.new_tag('strong'))
        
    return str(soup)

import tkinter as tk
from tkinter import  *

window = tk.Tk()
window.title("Format Converter")

def commit_change():
    outputBox.delete("1.0", END)
    inputValue= inputBox.get("1.0","end-1c")
    outputBox.insert("1.0", convert(inputValue))
    
def clear():
    inputBox.delete("1.0",END)
    outputBox.delete("1.0",END)
    
def on_input_modified():
    outputBox.delete("1.0", END)
    
inputBox = Text(window, height=20, width=100)
inputBox.grid(row=0, column=0, padx = 10, pady = 10)
inputBox.bind("<<TextModified>>", on_input_modified)

buttonCommit = Button(window, height=1, width=10, text="Commit",command=lambda: commit_change())
buttonClear = Button(window, height=1, width=10, text="Clear",command=lambda: clear())

outputBox = Text(window, height=20, width=100)
outputBox.grid(row=2, column=0,padx=10, pady=10)

buttonCommit.grid(row=1, column=0, padx = 10, sticky = 'w')
buttonClear.grid(row=1, column=0, padx = 10, sticky = 'e')

window.mainloop()
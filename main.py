import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import os
import fnmatch

def search_code():
    query = search_entry.get()
    results_text.delete(1.0, tk.END)  # Clear previous results
    if not query:
        results_text.insert(tk.END, "Please enter a search query.")
        return
    
    if not selected_directory:
        results_text.insert(tk.END, "Please select a directory to search.")
        return
    
    search_method = search_method_var.get()
    if search_method == "Wild Card":
        search_files_with_wildcard(query)
    elif search_method == "Phrase":
        search_files_with_phrase(query)

def search_files_with_wildcard(query):
    for root, _, files in os.walk(selected_directory):
        for file in files:
            if fnmatch.fnmatch(file, query):
                results_text.insert(tk.END, f"File: {os.path.join(root, file)}\n")

def search_files_with_phrase(query):
    for root, _, files in os.walk(selected_directory):
        for file in files:
            if file.endswith('.py'):  # Only search Python files for demonstration
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query in content:
                        results_text.insert(tk.END, f"File: {os.path.join(root, file)}\n")
                        results_text.insert(tk.END, content + '\n')

def select_directory():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    directory_label.config(text=f"Selected Directory: {selected_directory}")

# GUI setup
root = tk.Tk()
root.title("Code Search Engine")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="black", font=("Segoe UI", 10))
style.configure("TLabel", foreground="black", font=("Segoe UI", 10))
style.configure("TEntry", foreground="black", font=("Segoe UI", 10))
style.configure("TFrame", background="#007A4D", borderwidth=2, relief="groove")

# Directory selection frame
directory_frame = ttk.Frame(root)
directory_frame.pack(pady=10, padx=20)

directory_label = ttk.Label(directory_frame, text="Selected Directory:", font=("Segoe UI", 10))
directory_label.grid(row=0, column=0, padx=(0, 5), pady=5)

directory_button = ttk.Button(directory_frame, text="Select Directory", command=select_directory)
directory_button.grid(row=0, column=1, padx=5, pady=5)

# Search entry frame
search_frame = ttk.Frame(root)
search_frame.pack(pady=10, padx=20)

search_label = ttk.Label(search_frame, text="Enter search query:", font=("Segoe UI", 10))
search_label.grid(row=0, column=0, padx=(0, 5), pady=5)

search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="ew")

search_method_var = tk.StringVar()
search_method_var.set("Wild Card")  # Default search method

search_method_label = ttk.Label(search_frame, text="Search Method:", font=("Segoe UI", 10))
search_method_label.grid(row=0, column=2, padx=(0, 5), pady=5)

search_method_combobox = ttk.Combobox(search_frame, textvariable=search_method_var, values=["Wild Card", "Phrase"], state="readonly")
search_method_combobox.grid(row=0, column=3, padx=5, pady=5)

search_button = ttk.Button(search_frame, text="Search", command=search_code)
search_button.grid(row=0, column=4, padx=5, pady=5)

# Results display
results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
results_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()

import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import os

def search_code():
    query = search_entry.get()
    results_text.delete(1.0, tk.END)  # Clear previous results
    if not query:
        results_text.insert(tk.END, "Please enter a search query.")
        return
    
    if not selected_directory:
        results_text.insert(tk.END, "Please select a directory to search.")
        return
    
    # Search for code files in the selected directory
    for root, dirs, files in os.walk(selected_directory):
        for file in files:
            if file.endswith('.py'):  # Only search Python files for demonstration
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if query in line:
                            results_text.insert(tk.END, f"File: {os.path.join(root, file)}, Line: {i+1}\n")
                            results_text.insert(tk.END, line + '\n')
                            results_text.insert(tk.END, '-'*50 + '\n')

def select_directory():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    directory_label.config(text=f"Selected Directory: {selected_directory}")

# GUI setup
root = tk.Tk()
root.title("Code Search Engine")

# Set window attributes to fullscreen
root.attributes('-fullscreen', True)

# Style
style = ttk.Style()
style.theme_use("clam")  # Use the clam theme for a modern look
style.configure("TButton", foreground="black", background="#DDDDDD", font=("Segoe UI", 10))
style.configure("TLabel", foreground="black", background="#F0F0F0", font=("Segoe UI", 10))
style.configure("TEntry", foreground="black", background="#FFFFFF", font=("Segoe UI", 10))
style.configure("TFrame", background="#F0F0F0")

# Directory selection
directory_frame = ttk.Frame(root)
directory_frame.grid(row=0, column=0, padx=10, pady=10)
directory_button = ttk.Button(directory_frame, text="Select Directory", command=select_directory)
directory_button.grid(row=0, column=0, padx=5, pady=5)
selected_directory = None
directory_label = ttk.Label(directory_frame, text="Selected Directory:")
directory_label.grid(row=0, column=1, padx=5, pady=5)

# Search entry
search_frame = ttk.Frame(root)
search_frame.grid(row=1, column=0, padx=10, pady=10)
search_label = ttk.Label(search_frame, text="Enter search query:")
search_label.grid(row=0, column=0, padx=5, pady=5)
search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = ttk.Button(search_frame, text="Search", command=search_code)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Results display
results_label = ttk.Label(root, text="Search Results:")
results_label.grid(row=2, column=0, padx=10, pady=5)
results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
results_text.grid(row=3, column=0, padx=10, pady=5)

# Configure grid weights to make the widgets expandable
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

root.mainloop()

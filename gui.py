import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from search_engine import SearchEngine

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Search Engine")
        self.search_engine = SearchEngine()
        self.selected_directories = ""
        self.setup_gui()

    def setup_gui(self):
        # Directory selection frame
        directory_frame = ttk.Frame(self.root)
        directory_frame.pack(pady=10, padx=20)

        self.directories_label = ttk.Label(directory_frame, text="Selected Directories:", font=("Segoe UI", 10))
        self.directories_label.grid(row=0, column=0, padx=(0, 5), pady=5)

        directories_button = ttk.Button(directory_frame, text="Select Directory", command=self.select_directories)
        directories_button.grid(row=0, column=1, padx=5, pady=5)

        # Tokenizer selection frame
        tokenizer_frame = ttk.Frame(self.root)
        tokenizer_frame.pack(pady=10, padx=20)

        tokenizer_label = ttk.Label(tokenizer_frame, text="Select Tokenizer:", font=("Segoe UI", 10))
        tokenizer_label.grid(row=0, column=0, padx=(0, 5), pady=5)

        self.tokenizer_var = tk.StringVar()
        self.tokenizer_var.set("Word Tokenizer")  # Default tokenizer

        tokenizer_combobox = ttk.Combobox(tokenizer_frame, textvariable=self.tokenizer_var, values=["Word Tokenizer", "Stopword Tokenizer", "Stemming Tokenizer"], state="readonly")
        tokenizer_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Search entry frame
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=10, padx=20)

        search_label = ttk.Label(search_frame, text="Enter search query:", font=("Segoe UI", 10))
        search_label.grid(row=0, column=0, padx=(0, 5), pady=5)

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="ew")

        search_method_var = tk.StringVar()
        search_method_var.set("Wild Card")  # Default search method

        search_method_label = ttk.Label(search_frame, text="Search Method:", font=("Segoe UI", 10))
        search_method_label.grid(row=0, column=2, padx=(0, 5), pady=5)

        self.search_method_combobox = ttk.Combobox(search_frame, textvariable=search_method_var, values=["Wild Card", "Phrase", "Approximate", "Boolean"], state="readonly")
        self.search_method_combobox.grid(row=0, column=3, padx=5, pady=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.search_code)
        search_button.grid(row=0, column=4, padx=5, pady=5)

        # Results display
        self.results_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def select_directories(self):
        self.selected_directories = filedialog.askdirectory()
        if self.selected_directories:
            self.directories_label.config(text=f"Selected Directories: {self.selected_directories}")

    def search_code(self):
        query = self.search_entry.get()
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        if not query:
            self.results_text.insert(tk.END, "Please enter a search query.")
            return
        
        if not self.selected_directories:
            self.results_text.insert(tk.END, "Please select directories to search.")
            return
        
        search_method = self.search_method_combobox.get()
        tokenizer_type = self.tokenizer_var.get()  # Get selected tokenizer type
        matches = self.search_engine.search_files(self.selected_directories, query, search_method, tokenizer_type)
        for match in matches:
            self.results_text.insert(tk.END, f"Match found in: {match}\n")

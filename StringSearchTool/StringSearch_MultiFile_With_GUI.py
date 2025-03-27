import os
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

g_displayWidth = 100

def search_string_in_files(directory, search_string):
    fileCount = 0
    # List to store matching file names
    matching_files = []


    # Recursively walk through all subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # Update results display in real-time
                fileCount += 1
                display_results(f"Processing file {fileCount}: {file_path}")
                results_text.update()  # Refresh the display window
                # Search for the string in the file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        if search_string in f.read():
                            matching_files.append(file_path)
                except Exception as e:
                    display_results(f"Error reading file {file_path}: {e}")
    display_results('-'*(g_displayWidth-1))
    footerMessage = f"Found {len(matching_files)} files with instances of {search_string} \n"
    # If file output is enabled, write matching file names to output file
    if write_to_file_var.get():  # Check if the checkbox is selected
        output_file = f"StringMatches_{search_string}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(footerMessage)
                for match in matching_files:
                    f.write(match + '\n')
        except Exception as e:
            display_results(f"Error writing to output file: {e}")
    # Display matching files in the text area
    for match in matching_files:
        display_results(match)
    display_results('-'*(g_displayWidth-1))
    display_results(footerMessage)
    if write_to_file_var.get():
        display_results(f"Match file results written to {output_file}")
	
def scan_button_clicked():
    directory = directory_field.get()
    search_string = search_field.get()
    if not search_string:
        display_results("Please enter a search string.")
        return
    results_text.delete('1.0', tk.END)  # Clear previous results
    search_string_in_files(directory, search_string)

def browse_button_clicked():
    directory = filedialog.askdirectory()
    if directory:
        directory_field.delete(0, tk.END)
        directory_field.insert(0, directory)

def display_results(message):
    results_text.insert(tk.END, message + "\n")
    results_text.see(tk.END)

def update_scan_button(*args):
    """Enable/Disable the Scan button based on the Directory field's content."""
    directory = directory_field.get()
    if directory.strip():  # If field is not empty
        scan_button.config(state=tk.NORMAL)
    else:  # Disable when field is empty
        scan_button.config(state=tk.DISABLED)

# Create the GUI application
app = tk.Tk()
app.title("Text Dump String Search Tool (String-search over a collection of .txt files")

# Directory Selection
ttk.Label(app, text="TXT Dump Directory:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
directory_field = ttk.Entry(app, width=80)
directory_field.grid(row=0, column=1, padx=10, pady=5, sticky="w")
browse_button = ttk.Button(app, text="Browse", command=browse_button_clicked)
browse_button.grid(row=0, column=2, padx=10, pady=5)

# Add trace to monitor Directory field changes
directory_field_var = tk.StringVar()
directory_field.config(textvariable=directory_field_var)
directory_field_var.trace_add("write", update_scan_button)


# Search String Entry Field
ttk.Label(app, text="Enter Search String:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
search_field = ttk.Entry(app, width=80)
search_field.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Scan Button
scan_button = ttk.Button(app, text="Scan", command=scan_button_clicked)
scan_button.grid(row=1, column=2, padx=10, pady=5)
scan_button.config(state=tk.DISABLED)  # Start disabled

# File Output Checkbox
write_to_file_var = tk.BooleanVar(value=False)  # Default to enabled
file_output_checkbox = ttk.Checkbutton(app, text="Write results to file", variable=write_to_file_var)
file_output_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Results Text Display
results_text = scrolledtext.ScrolledText(app, width=g_displayWidth, height=20, wrap=tk.WORD)
results_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the application
app.mainloop()

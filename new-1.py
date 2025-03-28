import tkinter as tk
from tkinter import filedialog
import os
import ctypes

# Enable High DPI Awareness (Windows)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except AttributeError:
    pass

def browse_file(label, file_type):
    file_types = [("Excel Files", "*.xlsx")] if file_type == "excel" else [("All Files", "*.*")]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path:
        label.config(text=os.path.normpath(file_path), fg="black")

def browse_directory(label):
    folder_path = filedialog.askdirectory()
    if folder_path:
        label.config(text=os.path.normpath(folder_path), fg="black")

def update_log_ui(message):
    log_text.config(state="normal")
    log_text.insert(tk.END, message + "\n")
    log_text.yview(tk.END)
    log_text.config(state="disabled")

def disable_ui():
    """Disables UI except the log area when Submit is clicked."""
    for widget in root.winfo_children():
        disable_recursive(widget)
    validation_button.config(state="disabled")
    consolidation_button.config(state="disabled")

def disable_recursive(widget):
    """Disables all interactive elements except the log area."""
    if isinstance(widget, tk.Button) and widget["text"] in ["Submit", "Clear", "Cancel", "Browse"]:
        widget.config(state="disabled")

    if isinstance(widget, tk.Frame):
        for child in widget.winfo_children():
            disable_recursive(child)

def process_validation():
    disable_ui()
    update_log_ui("Starting validation process...")
    root.after(1000, lambda: update_log_ui("Checking file format... Done"))
    root.after(2000, lambda: update_log_ui("Loading data... Done"))
    root.after(3000, lambda: update_log_ui("Validating rules... Done"))
    root.after(4000, lambda: update_log_ui("Saving results... Done"))
    root.after(5000, lambda: update_log_ui("Validation Completed Successfully!"))

def process_consolidation():
    disable_ui()
    update_log_ui("Starting consolidation process...")
    root.after(1000, lambda: update_log_ui("Fetching files from directory... Done"))
    root.after(2000, lambda: update_log_ui("Merging files... Done"))
    root.after(3000, lambda: update_log_ui("Applying configurations... Done"))
    root.after(4000, lambda: update_log_ui("Saving consolidated file... Done"))
    root.after(5000, lambda: update_log_ui("Consolidation Completed Successfully!"))

def show_validation_layout():
    clear_dynamic_widgets()

    tk.Label(root, text="Validation Layout", font=("Arial", 14)).pack(pady=10)

    frame1 = tk.Frame(root)
    frame1.pack(pady=5)
    tk.Label(frame1, text="File Path:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    file_label = tk.Label(frame1, text="No file selected", font=("Arial", 10), fg="gray", wraplength=250)
    file_label.grid(row=0, column=1, padx=5)
    tk.Button(frame1, text="Browse", command=lambda: browse_file(file_label, "excel")).grid(row=0, column=2, padx=5)

    frame2 = tk.Frame(root)
    frame2.pack(pady=5)
    tk.Label(frame2, text="Config File:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    config_label = tk.Label(frame2, text="No config file selected", font=("Arial", 10), fg="gray", wraplength=250)
    config_label.grid(row=0, column=1, padx=5)
    tk.Button(frame2, text="Browse", command=lambda: browse_file(config_label, "config")).grid(row=0, column=2, padx=5)

    frame3 = tk.Frame(root)
    frame3.pack(pady=20)
    tk.Button(frame3, text="Clear", command=lambda: clear_labels(file_label, config_label)).grid(row=0, column=0, padx=10)
    tk.Button(frame3, text="Cancel", command=root.quit).grid(row=0, column=1, padx=10)
    tk.Button(frame3, text="Submit", command=process_validation).grid(row=0, column=2, padx=10)

    show_log_area()

def show_consolidation_layout():
    clear_dynamic_widgets()

    tk.Label(root, text="Consolidation Layout", font=("Arial", 14)).pack(pady=10)

    frame1 = tk.Frame(root)
    frame1.pack(pady=5)
    tk.Label(frame1, text="Select File Directory:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    dir_label = tk.Label(frame1, text="No directory selected", font=("Arial", 10), fg="gray", wraplength=250)
    dir_label.grid(row=0, column=1, padx=5)
    tk.Button(frame1, text="Browse", command=lambda: browse_directory(dir_label)).grid(row=0, column=2, padx=5)

    frame2 = tk.Frame(root)
    frame2.pack(pady=5)
    tk.Label(frame2, text="Consolidated File Destination:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    dest_label = tk.Label(frame2, text="No destination selected", font=("Arial", 10), fg="gray", wraplength=250)
    dest_label.grid(row=0, column=1, padx=5)
    tk.Button(frame2, text="Browse", command=lambda: browse_directory(dest_label)).grid(row=0, column=2, padx=5)

    frame3 = tk.Frame(root)
    frame3.pack(pady=5)
    tk.Label(frame3, text="Config File:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    config_label = tk.Label(frame3, text="No config file selected", font=("Arial", 10), fg="gray", wraplength=250)
    config_label.grid(row=0, column=1, padx=5)
    tk.Button(frame3, text="Browse", command=lambda: browse_file(config_label, "excel")).grid(row=0, column=2, padx=5)

    frame4 = tk.Frame(root)
    frame4.pack(pady=20)
    tk.Button(frame4, text="Clear", command=lambda: clear_labels(dir_label, dest_label, config_label)).grid(row=0, column=0, padx=10)
    tk.Button(frame4, text="Cancel", command=root.quit).grid(row=0, column=1, padx=10)
    tk.Button(frame4, text="Submit", command=process_consolidation).grid(row=0, column=2, padx=10)

    show_log_area()

def show_log_area():
    global log_text
    log_text = tk.Text(root, height=6, width=50, state="disabled", wrap="word")
    log_text.pack(pady=10)

def clear_dynamic_widgets():
    for widget in root.winfo_children():
        if widget not in (button_frame, title_label, description_label):
            widget.destroy()

def clear_labels(*labels):
    for label in labels:
        label.config(text="No file selected", fg="gray")

# Main window
root = tk.Tk()
root.title("Data Processing Tool")
root.geometry("500x500")

title_label = tk.Label(root, text="Data Processing Tool", font=("Arial", 18, "bold"))
title_label.pack(pady=5)

description_label = tk.Label(root, text="This tool allows you to validate and consolidate data effortlessly.", font=("Arial", 12), wraplength=400, justify="center")
description_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

validation_button = tk.Button(button_frame, text="Validation", command=show_validation_layout, width=15)
validation_button.pack(side="left", padx=10)

consolidation_button = tk.Button(button_frame, text="Consolidation", command=show_consolidation_layout, width=15)
consolidation_button.pack(side="left", padx=10)

root.mainloop()

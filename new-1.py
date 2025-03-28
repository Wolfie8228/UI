import tkinter as tk
from tkinter import filedialog

selected_files = {}
all_buttons = []
cancel_button = None  

def reset_selected_files(mode):
    selected_files.clear()
    if mode == "validation":
        selected_files.update({"file": None, "config": None})
    elif mode == "consolidation":
        selected_files.update({"directory": None, "destination": None, "config": None})

def browse_file(file_type, key):
    file_types = [("Excel Files", "*.xlsx")] if file_type == "excel" else [("All Files", "*.*")]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path:
        selected_files[key] = file_path
        update_log_ui(f"{key.capitalize()} Selected: {file_path}")

def browse_directory(key):
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_files[key] = folder_path
        update_log_ui(f"{key.capitalize()} Selected: {folder_path}")

def update_log_ui(message, is_error=False):
    log_text.config(state="normal")
    if is_error:
        log_text.insert(tk.END, message + "\n", "error")
    else:
        log_text.insert(tk.END, message + "\n")
    log_text.yview(tk.END)
    log_text.config(state="disabled")

def process_validation():
    if not validate_selections(["file", "config"]):
        return
    disable_all_buttons()
    update_log_ui("Starting validation process...")
    root.after(1000, lambda: complete_process("Validation Completed Successfully!"))

def process_consolidation():
    if not validate_selections(["directory", "destination", "config"]):
        return
    disable_all_buttons()
    update_log_ui("Starting consolidation process...")
    root.after(1000, lambda: complete_process("Consolidation Completed Successfully!"))

def complete_process(message):
    update_log_ui(message)
    enable_all_buttons()

def validate_selections(required_keys):
    missing = [key.capitalize() for key in required_keys if not selected_files.get(key)]
    if missing:
        update_log_ui(f"Error: Missing selections - {', '.join(missing)}", is_error=True)
        return False
    return True

def show_validation_layout():
    global all_buttons, cancel_button
    reset_selected_files("validation")
    disable_consolidation()
    clear_dynamic_widgets()
    all_buttons = []

    tk.Label(root, text="Validation Layout", font=("Arial", 14)).pack(pady=10)

    btn1 = tk.Button(root, text="Browse File", command=lambda: browse_file("excel", "file"), width=20)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Browse Config", command=lambda: browse_file("config", "config"), width=20)
    btn2.pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    clear_button = tk.Button(frame, text="Clear", command=clear_labels, width=10)
    clear_button.grid(row=0, column=0, padx=10)

    cancel_button = tk.Button(frame, text="Cancel", command=return_to_main, width=10)
    cancel_button.grid(row=0, column=1, padx=10)

    submit_button = tk.Button(frame, text="Submit", command=process_validation, width=10)
    submit_button.grid(row=0, column=2, padx=10)

    all_buttons.extend([btn1, btn2, submit_button, clear_button, cancel_button])
    show_log_area()

def show_consolidation_layout():
    global all_buttons, cancel_button
    reset_selected_files("consolidation")
    disable_validation()
    clear_dynamic_widgets()
    all_buttons = []

    tk.Label(root, text="Consolidation Layout", font=("Arial", 14)).pack(pady=10)

    btn1 = tk.Button(root, text="Browse Directory", command=lambda: browse_directory("directory"), width=20)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Select Destination", command=lambda: browse_directory("destination"), width=20)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Browse Config", command=lambda: browse_file("excel", "config"), width=20)
    btn3.pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    clear_button = tk.Button(frame, text="Clear", command=clear_labels, width=10)
    clear_button.grid(row=0, column=0, padx=10)

    cancel_button = tk.Button(frame, text="Cancel", command=return_to_main, width=10)
    cancel_button.grid(row=0, column=1, padx=10)

    submit_button = tk.Button(frame, text="Submit", command=process_consolidation, width=10)
    submit_button.grid(row=0, column=2, padx=10)

    all_buttons.extend([btn1, btn2, btn3, submit_button, clear_button, cancel_button])
    show_log_area()

def return_to_main():
    reset_selected_files("")
    enable_all_buttons()
    clear_dynamic_widgets()
    show_main_buttons()

def show_log_area():
    global log_text
    log_text = tk.Text(root, height=6, width=60, state="disabled", wrap="word", bg="black", fg="white")
    log_text.pack(pady=10)
    log_text.tag_config("error", foreground="red")

def clear_dynamic_widgets():
    for widget in root.winfo_children():
        if widget not in (button_frame, title_label, description_label):
            widget.destroy()

def clear_labels():
    log_text.config(state="normal")
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, "Cleared file selections.\n")
    log_text.config(state="disabled")
    for key in selected_files:
        selected_files[key] = None

def show_main_buttons():
    button_frame.pack(pady=10)

def disable_validation():
    validation_button.config(state="disabled")

def disable_consolidation():
    consolidation_button.config(state="disabled")

def enable_main_buttons():
    validation_button.config(state="normal")
    consolidation_button.config(state="normal")

def disable_all_buttons():
    for btn in all_buttons:
        if btn.winfo_exists():
            btn.config(state="disabled")
    validation_button.config(state="disabled")
    consolidation_button.config(state="disabled")

def enable_all_buttons():
    validation_button.config(state="normal")
    consolidation_button.config(state="normal")
    for btn in all_buttons:
        if btn.winfo_exists():
            btn.config(state="normal")

# Main window
root = tk.Tk()
root.title("Data Processing Tool")
root.configure(bg="#F4F4F4")

title_label = tk.Label(root, text="Data Processing Tool", font=("Arial", 18, "bold"), bg="#F4F4F4")
title_label.pack(pady=5)

description_label = tk.Label(root, text="This tool allows you to validate and consolidate data effortlessly.",
                             font=("Arial", 12), wraplength=400, justify="center", bg="#F4F4F4")
description_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#F4F4F4")
button_frame.pack(pady=10)

validation_button = tk.Button(button_frame, text="Validation", command=show_validation_layout, width=15)
validation_button.pack(side="left", padx=10)

consolidation_button = tk.Button(button_frame, text="Consolidation", command=show_consolidation_layout, width=15)
consolidation_button.pack(side="left", padx=10)

root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox

# Global variables to store file paths
file_path_df1 = ""
file_paths_df2 = []
file_paths_df3 = []

# Mock function to simulate file processing
def process_files(df1, df2, df3):
    # Simulate processing files (replace this with your actual code)
    print("File is reading...")
    print("File is executing...")
    # Simulate a return of a file or result (this is where your actual processing logic will go)
    print("File processed.")
    return True  # Simulate successful processing

# Function to open the file selection window for DF1
def open_file_selection_window():
    selection_window = tk.Toplevel(root)
    selection_window.title("Select Files for DF1")
    selection_window.geometry("500x200")

    # Function to browse and select a file
    def browse_file(entry_var):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file_path:
            entry_var.set(file_path)

    # Create UI for file selection for DF1
    file_path_var = tk.StringVar()
    
    label = tk.Label(selection_window, text="File Path 1:", font=('Arial', 12))
    label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    entry = tk.Entry(selection_window, textvariable=file_path_var, width=40)
    entry.grid(row=0, column=1, padx=10, pady=5)

    browse_button = tk.Button(selection_window, text="Browse", command=lambda: browse_file(file_path_var))
    browse_button.grid(row=0, column=2, padx=10, pady=5)

    # Function to open the next window and store the selected paths
    def open_next_window():
        global file_path_df1
        file_path_df1 = file_path_var.get()  # Store path for DF1
        selection_window.destroy()  # Close the current window
        open_df2_selection_window()  # Open the next window

    # Function to clear the file path
    def clear_entry():
        file_path_var.set('')

    # Buttons at the bottom
    button_frame = tk.Frame(selection_window)
    button_frame.grid(row=1, column=0, columnspan=3, pady=20)

    cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_entry)
    clear_button.pack(side=tk.LEFT, padx=10)

    next_button = tk.Button(button_frame, text="Next ->", command=open_next_window)
    next_button.pack(side=tk.LEFT, padx=10)

# Function to open the file selection window for DF2
def open_df2_selection_window():
    selection_window = tk.Toplevel(root)
    selection_window.title("Select Files for DF2")
    selection_window.geometry("500x300")

    # Function to browse and select a file
    def browse_file(entry_var, file_type):
        if file_type == 'excel':
            file_path = filedialog.askopenfilename(
                title="Select an Excel File",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
            )
        elif file_type == 'csv':
            file_path = filedialog.askopenfilename(
                title="Select a CSV File",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
        if file_path:
            entry_var.set(file_path)

    # Create UI for file selection for DF2
    file_paths = [tk.StringVar() for _ in range(3)]
    
    # Indicate file types for DF2
    file_labels = [
        "File Path 1 (Select Excel):",
        "File Path 2 (Select CSV):",
        "File Path 3 (Select Excel):"
    ]
    
    for i in range(3):
        label = tk.Label(selection_window, text=file_labels[i], font=('Arial', 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = tk.Entry(selection_window, textvariable=file_paths[i], width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)

        file_type = 'excel' if i in [0, 2] else 'csv'
        browse_button = tk.Button(selection_window, text="Browse", command=lambda i=i: browse_file(file_paths[i], file_type))
        browse_button.grid(row=i, column=2, padx=10, pady=5)

    # Load previously selected paths
    for i in range(3):
        file_paths[i].set(file_paths_df2[i] if i < len(file_paths_df2) else '')

    # Function to open the next window and store the selected paths
    def open_next_window():
        global file_paths_df2
        file_paths_df2 = [path.get() for path in file_paths]  # Store paths for DF2
        selection_window.destroy()  # Close the current window
        open_df3_selection_window()  # Open the next window

    # Function to clear all file paths
    def clear_entries():
        for path in file_paths:
            path.set('')

    # Function to go back to DF1 selection
    def go_back():
        selection_window.destroy()  # Close DF2 window
        open_file_selection_window()  # Reopen DF1 window with previously selected path

    # Buttons at the bottom
    button_frame = tk.Frame(selection_window)
    button_frame.grid(row=3, column=0, columnspan=3, pady=20)

    cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_entries)
    clear_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(button_frame, text="Back", command=go_back)
    back_button.pack(side=tk.LEFT, padx=10)

    next_button = tk.Button(button_frame, text="Next ->", command=open_next_window)
    next_button.pack(side=tk.LEFT, padx=10)

# Function to open the file selection window for DF3
def open_df3_selection_window():
    selection_window = tk.Toplevel(root)
    selection_window.title("Select Files for DF3")
    selection_window.geometry("500x300")

    # Function to browse and select a file
    def browse_file(entry_var):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file_path:
            entry_var.set(file_path)

    # Create UI for file selection for DF3
    file_paths = [tk.StringVar() for _ in range(3)]
    
    for i in range(3):
        label = tk.Label(selection_window, text=f"File Path {i + 1}:", font=('Arial', 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = tk.Entry(selection_window, textvariable=file_paths[i], width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)

        browse_button = tk.Button(selection_window, text="Browse", command=lambda i=i: browse_file(file_paths[i]))
        browse_button.grid(row=i, column=2, padx=10, pady=5)

    # Load previously selected paths
    for i in range(3):
        file_paths[i].set(file_paths_df3[i] if i < len(file_paths_df3) else '')

    # Function to clear all file paths
    def clear_entries():
        for path in file_paths:
            path.set('')

    # Function to store the paths for DF3 and close the window
    def submit_and_close():
        global file_paths_df3
        file_paths_df3 = [path.get() for path in file_paths]  # Store paths for DF3
        
        # Execute file processing
        success = process_files(file_path_df1, file_paths_df2, file_paths_df3)
        
        # Close the current window
        selection_window.destroy()  
        
        # Show appropriate message based on processing success
        if success:
            messagebox.showinfo("Processing Complete", "Files have been successfully processed.")
        else:
            messagebox.showwarning("Processing Error", "There was an error processing the files.")

    # Function to go back to DF2 selection
    def go_back():
        selection_window.destroy()  # Close DF3 window
        open_df2_selection_window()  # Reopen DF2 window with previously selected paths

    # Buttons at the bottom
    button_frame = tk.Frame(selection_window)
    button_frame.grid(row=3, column=0, columnspan=3, pady=20)

    cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_entries)
    clear_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(button_frame, text="Back", command=go_back)
    back_button.pack(side=tk.LEFT, padx=10)

    submit_button = tk.Button(button_frame, text="Submit", command=submit_and_close)
    submit_button.pack(side=tk.LEFT, padx=10)

# Function for cancel button on the main window
def cancel_action():
    root.quit()

# Create the main tkinter window
root = tk.Tk()
root.title("File Selection Wizard")
root.geometry("500x300")  # Set window size

# Add a title label with a description
title_label = tk.Label(root, text="File Selection", font=('Helvetica', 20, 'bold'))
title_label.pack(pady=20)

description_label = tk.Label(root, text="Select the files you wish to process.", font=('Arial', 12))
description_label.pack(pady=10)

# Button to start the file selection
start_button = tk.Button(root, text="Select Files", command=open_file_selection_window)
start_button.pack(pady=20)

# Cancel button to exit the application
cancel_button = tk.Button(root, text="Cancel X", command=cancel_action)
cancel_button.pack(pady=5)

# Start the main event loop
root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox

# # Global variables to store file paths
# file_path_df1 = ""
# file_paths_df2 = []
# file_paths_df3 = []

# # Function to open the file selection window for DF1
# def open_file_selection_window():
#     selection_window = tk.Toplevel(root)
#     selection_window.title("Select Files for DF1")
#     selection_window.geometry("500x200")

#     # Function to browse and select a file
#     def browse_file(entry_var):
#         file_path = filedialog.askopenfilename(
#             title="Select a File",
#             filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
#         )
#         if file_path:
#             entry_var.set(file_path)

#     # Create UI for file selection for DF1
#     file_path_var = tk.StringVar()
    
#     label = tk.Label(selection_window, text="File Path 1:", font=('Arial', 12))
#     label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

#     entry = tk.Entry(selection_window, textvariable=file_path_var, width=40)
#     entry.grid(row=0, column=1, padx=10, pady=5)

#     browse_button = tk.Button(selection_window, text="Browse", command=lambda: browse_file(file_path_var))
#     browse_button.grid(row=0, column=2, padx=10, pady=5)

#     # Function to open the next window and store the selected paths
#     def open_next_window():
#         global file_path_df1
#         file_path_df1 = file_path_var.get()  # Store path for DF1
#         selection_window.destroy()  # Close the current window
#         open_df2_selection_window()  # Open the next window

#     # Function to clear the file path
#     def clear_entry():
#         file_path_var.set('')

#     # Buttons at the bottom
#     button_frame = tk.Frame(selection_window)
#     button_frame.grid(row=1, column=0, columnspan=3, pady=20)

#     cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
#     cancel_button.pack(side=tk.LEFT, padx=10)

#     clear_button = tk.Button(button_frame, text="Clear", command=clear_entry)
#     clear_button.pack(side=tk.LEFT, padx=10)

#     next_button = tk.Button(button_frame, text="Next ->", command=open_next_window)
#     next_button.pack(side=tk.LEFT, padx=10)

# # Function to open the file selection window for DF2
# def open_df2_selection_window():
#     selection_window = tk.Toplevel(root)
#     selection_window.title("Select Files for DF2")
#     selection_window.geometry("500x300")

#     # Function to browse and select a file
#     def browse_file(entry_var, file_type):
#         if file_type == 'excel':
#             file_path = filedialog.askopenfilename(
#                 title="Select an Excel File",
#                 filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
#             )
#         elif file_type == 'csv':
#             file_path = filedialog.askopenfilename(
#                 title="Select a CSV File",
#                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
#             )
#         if file_path:
#             entry_var.set(file_path)

#     # Create UI for file selection for DF2
#     file_paths = [tk.StringVar() for _ in range(3)]
    
#     # Indicate file types for DF2
#     file_labels = [
#         "File Path 1 (Select Excel):",
#         "File Path 2 (Select CSV):",
#         "File Path 3 (Select Excel):"
#     ]
    
#     for i in range(3):
#         label = tk.Label(selection_window, text=file_labels[i], font=('Arial', 12))
#         label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

#         entry = tk.Entry(selection_window, textvariable=file_paths[i], width=40)
#         entry.grid(row=i, column=1, padx=10, pady=5)

#         file_type = 'excel' if i in [0, 2] else 'csv'
#         browse_button = tk.Button(selection_window, text="Browse", command=lambda i=i: browse_file(file_paths[i], file_type))
#         browse_button.grid(row=i, column=2, padx=10, pady=5)

#     # Function to open the next window and store the selected paths
#     def open_next_window():
#         global file_paths_df2
#         file_paths_df2 = [path.get() for path in file_paths]  # Store paths for DF2
#         selection_window.destroy()  # Close the current window
#         open_df3_selection_window()  # Open the next window

#     # Function to clear all file paths
#     def clear_entries():
#         for path in file_paths:
#             path.set('')

#     # Buttons at the bottom
#     button_frame = tk.Frame(selection_window)
#     button_frame.grid(row=3, column=0, columnspan=3, pady=20)

#     cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
#     cancel_button.pack(side=tk.LEFT, padx=10)

#     clear_button = tk.Button(button_frame, text="Clear", command=clear_entries)
#     clear_button.pack(side=tk.LEFT, padx=10)

#     next_button = tk.Button(button_frame, text="Next ->", command=open_next_window)
#     next_button.pack(side=tk.LEFT, padx=10)

# # Function to open the file selection window for DF3
# def open_df3_selection_window():
#     selection_window = tk.Toplevel(root)
#     selection_window.title("Select Files for DF3")
#     selection_window.geometry("500x300")

#     # Function to browse and select a file
#     def browse_file(entry_var):
#         file_path = filedialog.askopenfilename(
#             title="Select a File",
#             filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
#         )
#         if file_path:
#             entry_var.set(file_path)

#     # Create UI for file selection for DF3
#     file_paths = [tk.StringVar() for _ in range(3)]
    
#     for i in range(3):
#         label = tk.Label(selection_window, text=f"File Path {i + 1}:", font=('Arial', 12))
#         label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

#         entry = tk.Entry(selection_window, textvariable=file_paths[i], width=40)
#         entry.grid(row=i, column=1, padx=10, pady=5)

#         browse_button = tk.Button(selection_window, text="Browse", command=lambda i=i: browse_file(file_paths[i]))
#         browse_button.grid(row=i, column=2, padx=10, pady=5)

#     # Function to clear all file paths
#     def clear_entries():
#         for path in file_paths:
#             path.set('')

#     # Function to store the paths for DF3 and close the window
#     def submit_and_close():
#         global file_paths_df3
#         file_paths_df3 = [path.get() for path in file_paths]  # Store paths for DF3
#         selection_window.destroy()  # Close the current window
        
#         # Show processing message
#         show_processing_window()

#     # Function to show the processing window
#     def show_processing_window():
#         processing_window = tk.Toplevel(root)
#         processing_window.title("Processing")
#         processing_window.geometry("300x150")
        
#         label = tk.Label(processing_window, text="Data is processing, please wait...", font=('Arial', 12))
#         label.pack(pady=20)

#         # Simulate processing time and then close the window
#         processing_window.after(3000, processing_complete)  # 3 seconds delay

#     # Function to execute when processing is complete
#     def processing_complete():
#         messagebox.showinfo("Processing Complete", "Files have been successfully processed.")
#         for widget in root.winfo_children():  # Close processing window
#             if isinstance(widget, tk.Toplevel):
#                 widget.destroy()

#     # Buttons at the bottom
#     button_frame = tk.Frame(selection_window)
#     button_frame.grid(row=3, column=0, columnspan=3, pady=20)

#     cancel_button = tk.Button(button_frame, text="Cancel X", command=selection_window.destroy)
#     cancel_button.pack(side=tk.LEFT, padx=10)

#     clear_button = tk.Button(button_frame, text="Clear", command=clear_entries)
#     clear_button.pack(side=tk.LEFT, padx=10)

#     submit_button = tk.Button(button_frame, text="Submit", command=submit_and_close)
#     submit_button.pack(side=tk.LEFT, padx=10)

# # Function for cancel button on the main window
# def cancel_action():
#     root.quit()

# # Create the main tkinter window
# root = tk.Tk()
# root.title("File Selection Wizard")
# root.geometry("500x300")  # Set window size

# # Add a title label with a description
# title_label = tk.Label(root, text="File Selection", font=('Helvetica', 20, 'bold'))
# title_label.pack(pady=20)

# description_label = tk.Label(root, text="Select the files you wish to upload. Click 'Select Files' to browse.")
# description_label.pack(pady=10)

# # Add "Select Files" and "Cancel" buttons
# button_frame = tk.Frame(root)  # Button frame with no background color
# button_frame.pack(pady=20)

# select_button = tk.Button(
#     button_frame,
#     text="Select Files",
#     command=open_file_selection_window,
#     font=('Arial', 12),
#     padx=20,
#     pady=5,
#     bd=2,
#     relief="raised"
# )
# select_button.pack(side=tk.LEFT, padx=10)

# cancel_button = tk.Button(
#     button_frame,
#     text="Cancel",
#     command=cancel_action,
#     font=('Arial', 12),
#     padx=20,
#     pady=5,
#     bd=2,
#     relief="raised"
# )
# cancel_button.pack(side=tk.LEFT, padx=10)

# # Start the main event loop
# root.mainloop()

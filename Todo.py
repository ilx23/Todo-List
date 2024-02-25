from tkinter import *
from tkinter import messagebox  # Import necessary modules for GUI and error handling
import pandas as pd  # Import Pandas library for data manipulation

app = Tk()  # Create the main application window
app.title("Todo List Application")  # Set the window title
app.geometry("500x500")  # Set the window size
app.configure(padx=10, pady=10)  # Add padding to the window


# Function to add a task to the list
def add_task():
    task = todo_entry.get()  # Get the task text from the entry widget
    if task != "":  # Check if the task is not empty
        todo_list_item.insert(END, task)  # Insert the task into the listbox
        todo_entry.delete(0, END)  # Clear the entry widget after adding the task
    else:
        messagebox.showwarning("Error", "Please Type A Task")  # Show a warning message if the task is empty


# Function to delete a selected task from the list
def delete_task():
    try:
        task_selected_index = todo_list_item.curselection()[0]  # Get the index of the selected task
        todo_list_item.delete(task_selected_index)  # Delete the selected task from the listbox
    except IndexError:
        messagebox.showwarning("Error",
                               "Please Select Your Task Before Delete it")  # Show a warning if no task is selected


# Function to export tasks to a CSV file
def export_as_csv():
    tasks = todo_list_item.get(0, END)  # Get all tasks from the listbox
    if not tasks:  # Check if there are no tasks
        messagebox.showerror("Error", "There Are No Tasks to Export")  # Show an error message if no tasks are present
    if tasks:  # Check if there are tasks
        df = pd.DataFrame({'Task': tasks})  # Create a DataFrame with tasks
        df.to_csv("tasks.csv", index=False)  # Export tasks to a CSV file without index
        messagebox.showinfo("Info", "Tasks exported to tasks.csv")  # Show an info message after exporting tasks


# Function to reset all tasks
def reset_tasks():
    todo_list_item.delete(0, END)  # Delete all tasks from the listbox


# Create and position GUI widgets
todo_label = Label(app, text="Enter Your Todo Item: ", font="arial")  # Label for task entry
todo_label.grid(row=0, column=0)  # Grid placement for the label

todo_entry = Entry(app, width=30)  # Entry widget for task input
todo_entry.grid(row=0, column=1)  # Grid placement for the entry widget

todo_add_button = Button(app, text="Add Todo", borderwidth=2, relief=GROOVE, width=10,
                         command=add_task)  # Button to add task
todo_add_button.grid(row=0, column=2, padx=5)  # Grid placement for the add button

todo_list_item = Listbox(app, width=65, height=20)  # Listbox to display tasks
todo_list_item.grid(row=1, column=0, columnspan=3, padx=5, pady=5)  # Grid placement for the listbox

delete_todo_button = Button(app, text="Delete", borderwidth=2, relief=GROOVE,
                            command=delete_task)  # Button to delete task
delete_todo_button.grid(row=2, column=0)  # Grid placement for the delete button

export_todo_button = Button(app, text="Export As CSV", borderwidth=2, relief=GROOVE,
                            command=export_as_csv)  # Button to export tasks
export_todo_button.grid(row=2, column=1)  # Grid placement for the export button

reset_todo_button = Button(app, text="Reset", borderwidth=2, relief=GROOVE,
                           command=reset_tasks)  # Button to reset tasks
reset_todo_button.grid(row=2, column=2)  # Grid placement for the reset button

developer_name = Label(app, text="Made By Ilia keshavarz", font=("arial", 9, "bold"),
                       fg="#212121")  # Label for developer information
developer_name.grid(row=3, column=0, columnspan=3, pady=20)  # Grid placement for the developer info label

app.mainloop()  # Start the Tkinter event loop to display the GUI and handle user interactions

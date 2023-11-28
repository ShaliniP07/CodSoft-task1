import tkinter as tk                      
from tkinter import ttk                 
from tkinter import messagebox           
import sqlite3 as sql                   
def adding_task():  
    string_task = field_task.get()  
    if len(string_task) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(string_task)  
        the_cursor.execute('insert into tasks values (?)', (string_task ,))  
        updating_list()  
        field_task.delete(0, 'end')  
def updating_list():    
    clearing_list()  
    for task in tasks:    
        task_listbox.insert('end', task)  
def deleting_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:    
            tasks.remove(the_value)    
            updating_list()    
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:    
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
def deleting_all_the_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:     
        while(len(tasks) != 0):    
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        updating_list()  
def clearing_list():  
    task_listbox.delete(0, 'end')  
def closing():  
    print(tasks)  
    guiWindow.destroy()  
def retrieving_database():    
    while(len(tasks) != 0):  
          tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager - SHALINI'S PROJECT")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#6F2DA8")  
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    tasks = []  
    header_frame = tk.Frame(guiWindow, bg = "#6F2DA8")  
    functions_frame = tk.Frame(guiWindow, bg = "#6F2DA8")  
    listbox_frame = tk.Frame(guiWindow, bg = "#6F2DA8")  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List:",  
        font = ("Futura", "30"),  
        background = "#6F2DA8",  
        foreground = "#E55451"  
    )  
    header_label.pack(padx = 20, pady = 20)  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Bodoni", "11", "bold"),  
        background = "#6F2DA8",  
        foreground = "#000000"  
    )  
    task_label.place(x = 30, y = 40)  
    field_task = ttk.Entry(  
        functions_frame,  
        font = ("Bodoni", "12"),  
        width = 18,  
        background = "#F660AB",  
        foreground = "#DA8A67"  
    )  
    field_task.place(x = 30, y = 80)  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = adding_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = deleting_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All The Tasks",  
        width = 24,  
        command = deleting_all_the_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = closing  
    )  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#F87217",  
        selectforeground = "#FFFFFF"  
    )    
    task_listbox.place(x = 10, y = 20)  
    retrieving_database()  
    updating_list()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close() 
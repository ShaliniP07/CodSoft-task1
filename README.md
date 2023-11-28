# CodSoft-task1
## To-do List application in Python programming Language
## Author: Shalini P
## Batch: (1 November- 30 November,2023)
## Domain: 
Python Programming
## Aim: 
To build a To-Do List application
## Description/Working of Code:
1. First, the necessary modules are imported, such as tkinter, sqlite3, and messagebox.

2. Next, a connection is established with the SQLite database named 'listOfTasks.db'.

3. A function named adding_task() is defined to add tasks to the database. This function takes the task as input, checks if the input field is empty, and then adds the task to the database.

4. Another function named updating_list() is defined to refresh the listbox in the GUI. This function fetches all the tasks from the database and updates the listbox to display them.

5. Finally, the GUI is created using tkinter widgets like Label, Entry, and Button. The main window has a label for the header, an entry box for inputting tasks, and several buttons for adding tasks, deleting tasks, deleting all tasks, and exiting the application.

6. When the user enters a task and clicks on the 'Add Task' button, the adding_task() function is called. This function appends the task to the tasks list and inserts it into the SQLite database. The updating_list() function is then called to update the listbox in the GUI.

7. When the user clicks on the 'Delete Task' button, the deleting_task() function is called. This function fetches the selected task from the listbox, removes it from the tasks list, and deletes it from the SQLite database. The updating_list() function is again called to update the listbox in the GUI.

8. When the user clicks on the 'Delete All The Tasks' button, the deleting_all_the_tasks() function is called. This function iterates through the tasks list and removes each task. It then deletes all the tasks from the SQLite database. The updating_list() function is once again called to update the listbox in the GUI.

9. When the user clicks on the 'Exit' button, the closing() function is called. This function closes the GUI window.

10. Before closing the GUI, the changes made to the database are committed using the_connection.commit(). This ensures that the changes made by the user are permanently saved to the database. After the user closes the GUI, the database connection is closed using the_cursor.close().

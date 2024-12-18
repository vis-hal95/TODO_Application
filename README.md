# TODO Application

### Features:

- **Add Task**: Add a new task to the list.
- **Delete Task**: Remove a selected task.
- **Mark as Completed**: Mark a task as completed (append "✓" to the task).
- **Task List Display**: Tasks are displayed in a Listbox widget.
- **Responsive Layout**: Buttons and listbox are arranged in a user-friendly layout.

  ![TODO](https://github.com/vis-hal95/TODO_Application/blob/2ba1c6e0029d78237aba199318fe355bd066e319/985ca52d-5cf4-48d2-9d18-f0e7f1921782.jpeg)

### Required Libraries:

- **Tkinter**: For creating the graphical interface.
- **tkinter.messagebox**: For showing alerts.
- **tkinter.font**: For customizing the fonts.
- **ttk** (from Tkinter): For themed widgets (like buttons, labels, etc.).

If you don’t have `tkinter` installed (it’s bundled with Python in most installations), you can install it via your system package manager or by using pip . 

1. **Task List (Listbox)**:
    - A `Listbox` widget displays the tasks added to the to-do list. The tasks are displayed in a clean, scrollable manner.
   Added the Task : 
  ![TODO](https://github.com/vis-hal95/TODO_Application/blob/2ba1c6e0029d78237aba199318fe355bd066e319/82f8fa0a-6dcc-43e3-9414-1cce23b046ac.jpeg)
2. **Entry Widget**:
    - An `Entry` widget is used for typing in new tasks. When the user clicks the "Add Task" button, the task is added to the list.
      
3. **Buttons**:
    - The **Add Task** button allows users to add tasks.
    - The **Delete Task** button deletes the selected task from the list.
    - The **Mark as Completed** button appends a checkmark ("✓") to a completed task.

    complete the task :
   ![TODO](https://github.com/vis-hal95/TODO_Application/blob/2ba1c6e0029d78237aba199318fe355bd066e319/dc5613b0-8659-4f9f-988b-a5b7935dcf20.jpeg)
5. **Error Handling**:
    - If the user attempts to delete or complete a task without selecting one, a warning message is shown using
       `messagebox.showwarning()`.

    Remove the task:
   ![TODO]( https://github.com/vis-hal95/TODO_Application/blob/2ba1c6e0029d78237aba199318fe355bd066e319/90531f13-c3a5-4a3b-a637-e59b5290fed4.jpeg)
7. **Theming and Layout**:
    - The `ttk.Style()` is used to create custom button styles (with colors like green, blue, and red for better visual impact).
    - The window layout is responsive, centered, and aesthetically pleasing.
    - `frame` is used to group and organize widgets.
8. **Font Customization**:
    - `font.Font()` is used to set a custom font for buttons and text entries, ensuring a clean and modern look.
9. **Window Configuration**:
    - The window is fixed at 400x400 pixels to maintain a consistent and clean layout.
    - The window title and non-resizable property (`root.resizable(False, False)`) ensure the UI looks consistent on different screen sizes.

###
### Example of Use:

1. **Start the App**: When you run the app, a window will pop up with a listbox and a text entry box.
2. **Add Tasks**: Type a task into the entry box and click "Add Task" to add it to the list.
3. **Delete Tasks**: Select a task from the list and click "Delete Task" to remove it.
4. **Complete Tasks**: Select a task from the list and click "Mark as Completed" to append a checkmark ("✓") to the task.

# CLI To-Do List App

This is a simple Command-Line Interface (CLI) To-Do List application built using Python and `curses`. It allows users to add, view, mark as completed, and delete tasks while displaying a neat interface with a persistent task list.

## Features

✅ Add tasks to your list  
✅ View all pending tasks  
✅ Mark tasks as completed  
✅ Delete tasks  
✅ Interactive UI with menu on the right side

## Prerequisites

Ensure you have Python installed on your system. You also need `curses`, which is included by default in Linux/macOS. On Windows, install `windows-curses`:

```bash
pip install windows-curses
```

## Installation & Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/gauravsingh-02/cli-todo-list.git
    cd cli-todo-list
    ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```
    
3. Run the application:

    ```bash
    python todo.py
    ```

4. Exit the application by selecting the **Exit** option.

## How It Works

-   The tasks are stored in a simple text file (`tasks.txt`).
-   The app displays tasks on the left and the menu on the right.
-   User input is taken interactively using `curses`.

## Future Improvements

-   Implement SQLite database support
-   Add color themes for better UI
-   Export tasks to a file

---

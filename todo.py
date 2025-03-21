import os
import curses

TASKS_FILE = "tasks.txt"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Get input in a pop-up box
def get_input(stdscr, prompt):
    height, width = stdscr.getmaxyx()
    win = curses.newwin(3, width // 2, height // 2, width // 4)
    win.border()
    win.addstr(1, 1, prompt)
    win.refresh()
    curses.echo()
    input_str = win.getstr(1, len(prompt) + 2).decode("utf-8").strip()
    curses.noecho()
    return input_str


# Toggle task completion
def complete_task(tasks, selected_task):
    if selected_task is not None:
        if tasks[selected_task].startswith("[✔]"):
            tasks[selected_task] = tasks[selected_task][4:]  # Remove [✔]
        else:
            tasks[selected_task] = "[✔] " + tasks[selected_task]  # Add [✔]
    return tasks


# Delete selected task
def delete_task(tasks, selected_task):
    if selected_task is not None:
        del tasks[selected_task]
    return tasks


# Main menu loop using curses
def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    tasks = load_tasks()
    selected_task = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 20, "Your To-Do List", curses.A_BOLD | curses.A_UNDERLINE)

        # Display tasks
        for i, task in enumerate(tasks):
            if i == selected_task:
                stdscr.addstr(
                    i + 2, 2, f"> {task}", curses.A_REVERSE
                )  # Highlight selected task
            else:
                stdscr.addstr(i + 2, 4, task)

        # Display menu
        stdscr.addstr(1, 40, "Menu", curses.A_BOLD)
        menu_options = [
            "1. Add Task",
            "2. Toggle Completed",
            "3. Delete Task",
            "4. Exit",
        ]
        for i, option in enumerate(menu_options):
            stdscr.addstr(i + 2, 40, option)

        # Refresh screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        if key == ord("1"):  # Add task
            new_task = get_input(stdscr, "Enter task: ")
            if new_task:
                tasks.append(new_task)
        elif key == ord("2"):  # Toggle completion
            tasks = complete_task(tasks, selected_task)
        elif key == ord("3"):  # Delete task
            tasks = delete_task(tasks, selected_task)
            selected_task = max(0, selected_task - 1)  # Adjust selection after deletion
        elif key == ord("4"):  # Exit
            break
        elif key == curses.KEY_UP and selected_task > 0:
            selected_task -= 1  # Move selection up
        elif key == curses.KEY_DOWN and selected_task < len(tasks) - 1:
            selected_task += 1  # Move selection down

    save_tasks(tasks)  # Auto-save before exiting


# Run the curses application
curses.wrapper(main)

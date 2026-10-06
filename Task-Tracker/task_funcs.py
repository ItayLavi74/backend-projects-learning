import json
import datetime

ERROR_UPDATE_TASK_NOT_FOUND = "ERROR: couldnt update task status, task not found"
ERROR_NO_TASKS = "ERROR: tasks not found"


# add task to DB
def add(task_description):
    # var to load existing tasks to

    # building task format
    task = build_task(task_description)

    # handeling first task
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            # id = number of existing tasks + 1
            id = len(data) + 1
    except:
        id = 1
        data = {}

    # add task to DB (json file)
    data.update({str(id): task})

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=True, default=str)

    print("Task added successfully.")


# build task format (auxiliary)
def build_task(task_description):

    curr_time = datetime.datetime.now()

    task = {
        "description": task_description,
        "status": "todo",
        "createdAt": curr_time,
        "updatedAt": curr_time
    }

    return task


# delete task from DB
def delete(id):
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            tasks_len = len(data) + 1
            del data[str(id)]
            data = update_tasks_id(data, int(id) + 1, tasks_len)

        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4, sort_keys=True, default=str)

        print("Task deleted successfully.")
    except:
        print("ERROR: couldnt delete task, task not found")


# updates task's id after deleting a task
def update_tasks_id(data, start_id, tasks_len):
    for i in range(start_id, tasks_len):
        data[str(i - 1)] = data.get(f"{i}")
        del data[str(i)]
    return data


# updates task's description
def update(id, new_description):
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            data[str(id)]["description"] = new_description
            data[str(id)]["updatedAt"] = datetime.datetime.now()
    except:
        print("ERROR: couldnt update task, task not found")
        return

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=True, default=str)

    print("Task updated successfully.")


# change task's status to "in-progress"
def mark_in_progress(id):
    response = change_status(id, "in-progress")

    if response:
        print(f'Task {id} status updated succesfuly to "in-progress"')
    else:
        print(ERROR_UPDATE_TASK_NOT_FOUND)


# change task's status to "done"
def mark_done(id):
    response = change_status(id, "done")

    if response:
        print(f'Task {id} status updated succesfuly to "done"')
    else:
        print(ERROR_UPDATE_TASK_NOT_FOUND)


# change task's status (auxiliary)
def change_status(id, new_status) -> bool:
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)

        data[str(id)]["status"] = new_status
        data[str(id)]["updatedAt"] = datetime.datetime.now()

        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4, sort_keys=True, default=str)

        return True
    except:
        return False


# print all tasks
def show_all():
    try:
        print_tasks_from_status(None)
    except:
        print(ERROR_NO_TASKS)


# print tasks with "todo" status
def show_todo():
    try:
        print_tasks_from_status("todo")
    except:
        print(ERROR_NO_TASKS)


# print tasks with "in-progress" status
def show_in_progress():
    try:
        print_tasks_from_status("in-progress")
    except:
        print(ERROR_NO_TASKS)


# print tasks with "done" status
def show_done():
    try:
        print_tasks_from_status("done")
    except:
        print(ERROR_NO_TASKS)

# print tasks that has specific status or all if status=None (auxiliary)


def print_tasks_from_status(status):
    with open("tasks.json", "r") as f:
        data = json.load(f)

    ids = list(data.keys())

    # filter only if status is defined (None for show all tasks)
    if status is not None:
        ids = list(filter(lambda id: data[str(id)]["status"] == status, ids))
        print(f'Found {len(ids)} tasks with status "{status}".')
    else:
        print(f'Found {len(ids)} tasks:')

    for id in ids:
        curr = data[id]
        print(
            f'  • Task {id:<5}description={curr.get("description"):<10}\tstatus={curr.get("status"):<15}\tcreated at={curr.get("createdAt")}')

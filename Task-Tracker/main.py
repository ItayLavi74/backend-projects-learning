from user_input import *
from task_funcs import add, delete, update, mark_in_progress, mark_done, show_all, show_todo, show_in_progress, show_done


def main():
    # fetch args from user_input.py file
    args = get_args()

    # program selection
    match args.prog:
        case "task-cli": task_cli(args)
        case _:
            print("Invlaid program")


def task_cli(args):
    match args.func:
        case 'add': add(args.task)
        case 'delete': delete(args.task)
        case 'update': update(args.task, args.new_description)
        case 'mark-in-progress': mark_in_progress(args.task)
        case 'mark-done': mark_done(args.task)
        case 'list': show_all()
        case 'list-done': show_done()
        case 'list-todo': show_todo()
        case 'list-in-progress': show_in_progress()
        case _:
            print(f'ERROR: "{args.func}" is an invalid command')


if __name__ == "__main__":
    main()

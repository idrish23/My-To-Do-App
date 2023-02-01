def getTODO():
    with  open("todo.txt", 'r') as file:
        local_file = file.readlines()
    return local_file


def writeTODO(todos_arg):
    with  open("todo.txt", 'w') as file:
        file.writelines(todos_arg)
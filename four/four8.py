from pyrob.api import *


@task
def task_5_7():
    while wall_is_beneath() == True or wall_is_above() == True:
        move_right()



if __name__ == '__main__':
    run_tasks()
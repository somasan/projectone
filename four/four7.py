from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() == False:
        move_down()
    while wall_is_beneath() == True:
        move_right()
    move_down()
    move_left()
    while wall_is_above() == True:
        if wall_is_on_the_left() == False:
             move_left()
        else:
            break



if __name__ == '__main__':
    run_tasks()
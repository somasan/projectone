from pyrob.api import *


@task
def task_8_22():

        while wall_is_above() == False:
            move_up()
        if wall_is_on_the_left() == True:
            while wall_is_on_the_right() == False:
                move_right()
        elif wall_is_on_the_left() == False:
            while wall_is_on_the_left() == False:
                move_left()


if __name__ == '__main__':
    run_tasks()
from pyrob.api import *


@task
def task_8_28():
        if wall_is_above() == True:
             while wall_is_on_the_left() == False:
                 if wall_is_above() == True:
                     move_left()
                 else:
                     break
             while wall_is_on_the_right() == False:
                 if wall_is_above() == True:
                     move_right()
                 else:
                    break
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()


if __name__ == '__main__':
    run_tasks()
from pyrob.api import *


@task
def task_8_30():
    def step():
        n = 0
        while wall_is_beneath() == False:
            move_down()
            n = 1
        while wall_is_beneath() == True and wall_is_on_the_left() == False:
                move_left()
                n = 0
        while wall_is_beneath() == True and wall_is_on_the_right() == False:
                move_right()
                n = 0
        while wall_is_beneath() == False:
            move_down()
            n = 1
        if n == 1:
           step()
    step()
    while wall_is_on_the_left() == False:
        move_left()




if __name__ == '__main__':
    run_tasks()
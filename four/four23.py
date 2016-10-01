from pyrob.api import *


@task
def task_6_6():

             move_right()
             while wall_is_on_the_right() == False:
                     while wall_is_above() == False:
                         move_up()
                         fill_cell()
                     while wall_is_beneath() == False:
                         move_down()
                     move_right()
             while wall_is_above() == False:
                 move_up()
                 fill_cell()
             while wall_is_beneath() == False:
                 move_down()
             while wall_is_beneath() == True:
                 move_left()

if __name__ == '__main__':
    run_tasks()
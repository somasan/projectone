from pyrob.api import *


@task
def task_8_18():

             r = 0
             while wall_is_on_the_right() == False:
                 if wall_is_above() == False:
                     move_up()
                     while wall_is_above() == False:
                         if cell_is_filled() == True:
                             move_up()
                             r += 1
                         else:
                             fill_cell()
                             move_up()
                     if cell_is_filled() == False:
                         fill_cell()
                     else:
                         r += 1
                     while wall_is_beneath() == False:
                         move_down()
                     move_right()
                 else:
                     while wall_is_above() == True:
                         fill_cell()
                         move_right()
             mov('ax', r)
if __name__ == '__main__':
    run_tasks()
from pyrob.api import *


@task
def task_4_11():
             l = 13
             a = 11
             move_right()
             for i in range(6):

                  for j in range(l):
                     move_down()
                     fill_cell()
                  l -= 2
                  move_right()
                  fill_cell()
                  for k in range(a):
                     move_up()
                     fill_cell()
                  a -= 2
                  move_right()
             move_down()
             fill_cell()
             move_down()
             move_left(12)






if __name__ == '__main__':
    run_tasks()
from pyrob.api import *


@task
def task_4_3():
             move_right()
             fill_cell()
             for i in range(6):
                  for j in range(26):
                     move_right()
                     fill_cell()
                  move_down()
                  fill_cell()
                  for k in range(26):
                     move_left()
                     fill_cell()
                  move_down()
                  if i != 5:
                      fill_cell()




if __name__ == '__main__':
    run_tasks()
from pyrob.api import *


@task
def task_7_6():
    a = 0
    while a != 5:
       if cell_is_filled() == True:
              a +=1
       if a != 5:
           move_right()




if __name__ == '__main__':
    run_tasks()
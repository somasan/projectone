from pyrob.api import *


@task
def task_9_3():
    a = 1
    while wall_is_on_the_right() == False:
           move_right()
           a += 1
    s = a
    y = s - 1
    print(a)
    print(s)
    while wall_is_on_the_left() == False:
           move_left()
    for i in range(1, a):

        for j in range(1, a):
            print(i,j)
            if i == j or j == ((a + 1) - i):
               move_right()
            else:
                fill_cell()
                move_right()
        print(i,j)
        if i == j or (j + i) == (s):
            if i == y and j == y:
                fill_cell()
                move_down()
            else:
                move_down()
        else:
            fill_cell()
            move_down()
        for k in range(1, a):
            move_left()
        if i == a - 1 and j == a - 1:
            for t in range(1, a):
                if t == 1:
                    move_right()
                else:
                    fill_cell()
                    move_right()
            for d in range(1, a):
                move_left()





if __name__ == '__main__':
    run_tasks()
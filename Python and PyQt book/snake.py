import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = int(sw/4)
snk_y = int(sh/2)
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [int(sh/2), int(sw/2)]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

 key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    if (key<260 and next_key<260) or (key>=260 and next_key>=260):
        next_key = -1
    key = key if next_key == -1 else next_key

    #if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
    if snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    if new_head[0] >= sh:
        new_head[0] = 0
    elif new_head[0] < 0:
        new_head[0] = sh-1
    elif new_head[1] >= sw:
        new_head[1] = 0
    elif new_head[1] < 0:
        new_head[1] = sw-1
    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(nf[0], nf[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
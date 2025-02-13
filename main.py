import curses 
import time

def main(stdscr): 
    #hide cursor
    curses.curs_set(0)

    #get screen dimensions
    height, width = stdscr.gatmaxyx()

    #game loop 
    while True: 
        #clear the screen
        stdscr.clear()

        #drawing the water line at the bottom
        water_line_y = height - 2 #place water line close to the bottom
        stdscr.addstr(water_line_y, 0, "~" * width)

        #refresh the screen
        stdscr.refresh()

        #wait before updating again 
        time.sleep(0.1)

#run the game in a curses wrapper
curses.wrapper(main)
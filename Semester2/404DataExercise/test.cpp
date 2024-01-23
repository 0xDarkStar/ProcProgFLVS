#include <ncurses.h>

int main()
{   
    initscr();          /* Start curses mode          */
    noecho();   
    printw("Hello World !!!");  /* Print Hello World          */
    refresh();          /* Print it on to the real screen */
    while (true == true) {
        char input = getch();            /* Wait for user input */
        if (input == 'q') {
            break;
        }
    }
    endwin();           /* End curses mode        */

    return 0;
}
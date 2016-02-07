# -*- coding: utf-8 -*- 
import curses 

screen = curses.initscr() 
curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 

top_pos = 0 
left_pos = 12 
y,x = screen.getmaxyx()
#screen.addstr(top_pos, left_pos, "Positioned String")
screen.addstr(0,x/2,"Reverse Styled String", curses.A_REVERSE)

# screen.addstr("This is a Sample Curses Script\n\n") 

#screen.addstr(40, left_pos, "Positioned String")


def my_raw_input(screen, r, c, prompt_string):
    # curses.echo() 
    screen.addstr(r, c, prompt_string)
    screen.refresh()
    input = screen.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line 

while True: 
   event = screen.getch() 
   if event == ord("q"): break
   elif event == ord("w"):
   	  screen.move(y -1,0)
   	  screen.insdelln(1)
   	  screen.insdelln(2)
   	  screen.addstr(">")
   	  curses.echo() 
   	  screen.refresh()
   	  input = screen.getstr(y-1, 1, 20)
   	  screen.addstr(input)
	  # choice = my_raw_input(screen, y-1, 0, "cool or hot?\n>").lower()
   elif event == ord("p"): 
      screen.clear()
      screen.addstr(0,x/2,"Reverse Styled String", curses.A_REVERSE)
      screen.move(y -1,0)
      screen.addstr("This is the footer")
      screen.move(y- 2,0)
      screen.addstr("The User Pressed Lower Case p") 
   elif event == ord("o"): 
      screen.clear()
      screen.addstr(0,x/2,"Reverse Styled String", curses.A_REVERSE)
      screen.move(y -1,0)
      screen.addstr("This is the footer")
      screen.move(y- 2,0)
      screen.addstr("The User Pressed Lower Case o")  
   elif event == ord("3"): 
      screen.clear()
      screen.addstr(0,x/2,"Reverse Styled String", curses.A_REVERSE)
      screen.move(y -1,0)
      screen.addstr("This is the footer")
      screen.move(y- 2,0)
      screen.addstr("The User Pressed 3")  
   elif event == ord(" "): 
      screen.clear()
      screen.addstr(0,x/2,"Reverse Styled String", curses.A_REVERSE)
      screen.move(y -1,0)
      screen.addstr("This is the footer")
      screen.move(y- 2,0)
      screen.addstr("The User Pressed space bar")  
curses.endwin()
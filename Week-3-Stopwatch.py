# template for "Stopwatch: The Game"
import simplegui
# define global variables
value=101
timer_value=0
attempts=0
success=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    last=t%10
    seconds=t/10
    min=seconds/60
    only_sec=seconds-min*60
    if(only_sec<10):
        only_sec='0'+str(only_sec)
    return str(min)+':'+str(only_sec)+'.'+str(last)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_handler():
    global timer_value
    timer_value+=1
    
def start():
    timer.start()
    
def stop():
    global attempts
    global success
    if(timer.is_running()):
        attempts+=1
        if(timer_value%10==0):
            success+=1
    timer.stop()
    
def reset():
    timer.stop()
    global timer_value
    global attempts
    global success
    timer_value=0
    attempts=0
    success=0
# define event handler for timer with 0.1 sec interval


# define draw handler

def draw(canvas):
    canvas.draw_text(format(timer_value),[175,200],24,"White")
    show_stat=str(success)+'/'+str(attempts)
    canvas.draw_text(show_stat,[350,50],18,'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 400, 400)

# register event handlers
start = frame.add_button('Start', start,150)
stop = frame.add_button('Stop', stop,150)
reset = frame.add_button('Reset', reset,150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)


# start frame
frame.start()


# Please remember to review the grading rubric

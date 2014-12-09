# Programmed by Jibin Liu
# "Stopwatch: The Game"
# Can be played at http://www.codeskulptor.org/#user30_KUiwTKXBHrLME4o.py

import simplegui

# define global variables
time_counter = 0
trial_counter = 0
success_counter = 0
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    bc = (t % 600) // 10
    b = bc // 10
    c = bc % 10
    d = t - (a * 600 + bc * 10)
    if b == 0:
        return str(a) + ':' + '0' + str(c) + '.' + str(d)
    else:
        return str(a) + ':' + str(bc) + '.' + str(d)

def trial_format(x, y):
    return str(x) + '/' + str(y)

# define event handlers for buttons; "Start", "Stop", "Reset"
def time_start():
    global running
    running = True
    timer.start()

    
def time_stop():
    timer.stop()
    global time_counter, trial_counter, success_counter, running
    if running:
        running = False
        trial_counter += 1
        last_digit = time_counter % 10
        if last_digit == 0:
            success_counter += 1
    
def time_reset():
    timer.stop()
    global time_counter, trial_counter, success_counter, running
    time_counter = 0
    trial_counter = 0
    success_counter = 0
    running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_counter
    time_counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_counter), [100, 100], 30, 'White')
    canvas.draw_text(trial_format(success_counter, trial_counter), [250, 30], 30, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
button_start = frame.add_button('Start', time_start, 50)
button_stop = frame.add_button('Stop', time_stop, 50)
button_reset = frame.add_button('Reset', time_reset, 50)

# start frame
frame.start()

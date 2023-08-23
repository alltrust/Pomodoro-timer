import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def restart_timer():
    global reps
    mainWindow.after_cancel(timer)
    reps = 0
    pomoCanvas.itemconfig(pomodor_timer_label, text="00:00")
    timerHeading.config(text="Timer")
    checkMarkLabel.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """starts the count down"""
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    short_break_sec = 2
    reps += 1

    work_reps = [1, 3, 5, 7]
    if reps in work_reps:
        count_down(work_sec)
        timerHeading.config(text="Work", fg=GREEN)
    elif reps not in work_reps and reps < 7:
        count_down(short_break_sec)
        timerHeading.config(text="Break", fg=RED)
    else:
        count_down(long_break_sec)
        timerHeading.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    pomoCanvas.itemconfig(pomodor_timer_label,
                          text=f"{count_min}:{count_sec:02}")
    if count >= 0:
        global timer
        timer = mainWindow.after(1000, count_down, count-1)
    else:
        mark = ""
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkMarkLabel.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

mainWindow = tkinter.Tk()
mainWindow.minsize(500, 500)

mainWindow.config(bg=YELLOW)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=2)
mainWindow.rowconfigure(4, weight=2)


pomoCanvas = tkinter.Canvas(
    mainWindow, bg="white", highlightthickness=0, width=300, height=300, background=YELLOW)

pomodoro_img = "tomato.png"
photoPomodoro = tkinter.PhotoImage(file=pomodoro_img)
image = pomoCanvas.create_image(150, 150, image=photoPomodoro)


pomodor_timer_label = pomoCanvas.create_text(
    150, 160, text="00:00", font=(FONT_NAME, 36))

pomoCanvas.grid(column=1, row=1, sticky='n')


timerHeading = tkinter.Label(mainWindow, text="Timer", font=(
    FONT_NAME, 48), background=YELLOW, foreground=GREEN)
timerHeading.grid(column=1, row=0, sticky="s")

startBtn = tkinter.Button(mainWindow, text="Start",
                          highlightbackground=YELLOW, justify='right', command=start_timer)
startBtn.grid(column=0, row=2, sticky='ne')

resetBtn = tkinter.Button(mainWindow, text="Reset",
                          highlightbackground=YELLOW, justify="left", command=restart_timer)
resetBtn.grid(column=2, row=2, sticky='nw')

checkMarkLabel = tkinter.Label(
    mainWindow, fg=GREEN, background=YELLOW, font=(50))
checkMarkLabel.grid(column=1, row=3)


mainWindow.mainloop()

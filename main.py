from tkinter import *

sec = 5
typed_values = []

# list to str
# passage = passage.join(passage_list)
# print(passage)

# str to list
# print(passage_list)

screen1 = None
time_left = None
input = None
current_input = 0
old_input = 0


def start_typing(sec):
    global screen1
    global time_left
    global input
    global current_input
    global old_input

    print(f"current_input: {current_input}")
    print(f"old_input: {old_input}")

    INPUT_value = input.get("1.0", "end-1c")
    input_len = len(INPUT_value)
    print(f"input length :{len(INPUT_value)}\n\n")

    if sec!=-1:
        if input_len == current_input:
            screen1.after(1000, start_typing, sec - 1)
            time_left.config(text=sec)
        else:
            current_input = input_len
            old_input = current_input
            sec = 5
            print("input got")
            screen1.after(1000, start_typing, sec)
            time_left.config(text=sec)
    else:
        sec=5
        input.delete("1.0", "end-1c")
        screen1.after(1000, start_typing, sec)
        time_left.config(text=sec)

def screen1_screen():
    global screen1
    global time_left
    global input
    screen1 = Tk()
    screen1.geometry("1200x600")
    screen1.title("Typing Test Desktop App")
    screen1.config(bg="lightblue", padx=300, pady=50)

    title = Label(text="Disappearing Text Writing App", font=("Arial", 25, "bold"), bg="lightblue")
    title.grid_configure(row=1, column=1)

    time_left = Label(text=f"Time left:", font=("Arial", 14))
    time_left.grid_configure(row=2, column=2)

    time_left = Label(text=sec, font=("Arial", 14), fg="red")
    time_left.grid_configure(row=2, column=3)

    input = Text(width=60, height=10, font=("Arial", 14))
    input.grid_configure(row=5, column=1)

    note = Label(text="Note: Please click start button and start to type", font=("Arial", 14), fg="red")
    note.grid_configure(row=2, column=1)

    start = Button(text="start",
                   command=lambda: start_typing(sec),
                   font=("Arial", 14))
    start.grid_configure(row=5, column=0)

    screen1.mainloop()


screen1_screen()

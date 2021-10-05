import pandas
import turtle

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's another state name?").title()

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_data = data[data.state == answer]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(answer, font=("Arial", 8, "bold"))

    # turtle.mainloop()

    # screen.exitonclick()
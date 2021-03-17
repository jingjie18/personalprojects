import turtle
import pandas as pd
import csv

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US. States Game")
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

df = pd.read_csv("50_states.csv")


all_states = df["state"].to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{len(correct_guesses)}/50 States Correct","What's another state name?").title()

    if answer_state == "Exit":
        break

    #Check if guess among 50 states
    if df["state"].str.contains(answer_state).any():
        df_filt = df[df["state"] == answer_state]
        new_x = int(df_filt["x"])
        new_y = int(df_filt["y"])
        turtle.goto(new_x,new_y)
        turtle.write(f"{answer_state}",align="center")
        correct_guesses.append(answer_state)

missing_states_list = [states for states in df["state"] if states not in correct_guesses]

new_data = pd.DataFrame(missing_states_list)
new_data.to_csv("states_to_learn.csv")
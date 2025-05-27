import os
import sys
import json
from datetime import datetime

file_name = "tasks.json"


name = input('Enter your name:')
age = input('What is your age?')
married = input("Are you married?")
sex = input('What is your gender?')
morning = input('What is the most important thing you have do?')
wake_up = input('What time do you wake up?')
evening = input('What do you do at Midday?')
afternoon = input('what do you do during your free time?')
night = input('what do you do before bedtime?')
sleep = input('What time do you go to sleep?')

x = {
  "name": name, 
  "age": age, 
  "sex": sex,
  "married": married
  # "cars":[
  #   {"model":'Lamboghini',"Horsepower": 2000},
  #   {"model":'Ford Mustang',"Horsepower": 500}
  #   ]
  }

y = json.dumps(x,indent = 4, separators=(" <"," = "))

g = {
  "Wake up": wake_up, 
  "Sleep": sleep
  }

h = json.dumps(g,indent = 4)

activities = {
  "Morning": morning, 
  "Evening": evening,
  "Afternoon": afternoon,
  "Night": night
  }

k = json.dumps(activities,indent = 4, separators=(","," = "))

print(y,h,k)
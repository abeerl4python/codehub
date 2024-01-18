prompt = "\nWhat topping would you like to add on your pizza?"
prompt += "\nEnter 'exit' when toppings are finished: "

while True:
    topping = input(prompt)
    if topping != 'exit':
        print("  I'll add " , topping ," to your pizza.")
    else:
        break
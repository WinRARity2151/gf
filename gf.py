import g4f

while True:
    user_input = input("+ ")
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
    stream=True,
    )

    for message in response:
        print(message, flush=True, end='')

said_hello = False

    
def get_response(message):
    global said_hello
    if not said_hello:
        said_hello = True
        return "Hello, what is your name?"
    else:
        return message + " That's a funny name"

def main():
    user_message = ""
    while True:
        bot_response= get_response(user_message)
        print(bot_response)
        user_message = input()

main()
input()    


class HelloProgram:
        seq_num = 0
        def run(self,message):
            self.seq_num += 1
            if self.seq_num == 1:
                return "Hello, what is your name?"
            elif self.seq_num == 2:
                return "Hello {}, How old are you?".format(message)
            elif self.seq_num == 3:
                return "{}! That's so old!".format(message)
            else: 
                return "I don't want to talk to you anymore :("
    
def get_response(message):
    pass


def main():
    user_message = ""
    program = HelloProgram()
    while True:
        #bot_response= get_response(user_message)
        bot_response = program.run(user_message)
        print(bot_response)
        user_message = input()

main()
input()    

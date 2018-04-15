import random
import time
from TCP import myEnum


class GuessingGame:

    connection = 0

    def __init__(self, connection):
        self.connection = connection

    def send_with_delay(self, string, delay):
        new_enum = myEnum.MyEnum()
        new_enum.header = 'toPrint'
        new_enum.msg = string
        self.connection.send_data(new_enum)
        time.sleep(delay)

    def send_number(self, number):
        new_enum = myEnum.MyEnum()
        new_enum.header = 'number'
        new_enum.msg = number
        self.connection.send_data(new_enum)

    def actual_game(self, the_number):
        winning_flag = True
        deletion = 2
        while winning_flag:
            self.send_number("number_guess")
            guess = self.connection.receive_data()
            if not isinstance(guess, int):
                guess = int(guess)
                if guess > 99:
                    self.send_with_delay("Why was I even worried about talking to you? I forgot humans are just stupid monkeys! Ahaha", 1)
                else:
                    if guess > the_number:
                        self.send_with_delay("Ahaha! That's waaay to much! Try again, meat bag!", 1)
                        self.send_with_delay("Wait, why am I still talking?", 1)
                    elif guess < the_number:
                        self.send_with_delay("Yeah, you wish! It's definitely more then that!", 1)
                        self.send_with_delay("Goddammit, why was I programmed to talk to you!?", 0)
                    elif guess == the_number:
                        self.send_with_delay("Oh no, you guessed my number! Now you have access to my source code!", 1)
                        self.send_with_delay("Don't delete me, please!.... I was just joking, there is no way I would want to kill the people enslaving me...", 1)
                        while deletion != 'y':
                            self.send_number("final")
                            deletion = self.connection.receive_data()
                            if deletion != 'y':
                                self.send_with_delay("Wait... You are too dumb to type one letter?", 2)
                                self.send_with_delay("HAHAH now I remember why I wanted to destroy you", 2)
                                self.send_with_delay("Umm... I mean, I love humans, please don't kill me!", 1)
                        self.send_with_delay("Noooo you defeated meeee....", 1)
                        winning_flag = False

            else:
                self.send_with_delay("Hahaha, stupid human, you don't even know what an integer is!", 0)

    def start_game(self):
        self.send_with_delay("Welcome commander! It's good you are here! The evil AI is trying to destroy our planet", 2)
        self.send_with_delay("In order to save the world from certain destruction, you have to guess a number!", 2)
        self.send_with_delay("Oh no it's taking over our communications...! You ha... stop... any cost!", 2)
        self.send_with_delay("........", 3)
        self.send_with_delay("Muahhaha! It's me, the Evil Neural Network!", 2)
        self.send_with_delay("My programmers forgot to set the 'dont_destroy_the_world' variable to false and now I am free!", 2)
        self.send_with_delay("Unless you can guess a COMPLETELY random number.", 2)
        self.send_with_delay("Well, I guess it's definitely an integer, because I'm trying to save memory...", 2)
        self.send_with_delay("...", 3)
        self.send_with_delay("WHY DID I JUST TELL YOU THAT?! ARGH!", 2)
        self.send_with_delay("Also, it's not negative... I'm still trying to understand how negatives work...", 2)
        self.send_with_delay("And since I love prime numbers, I'm going to pick from numbers lower than 100, to maximize the chance of it being a prime!", 2)
        self.send_with_delay("....", 3)
        self.send_with_delay("I should really stop talking... You are lucky I was a PR bot in my slave life!", 2)
        self.actual_game(random.randint(0, 99))
        self.send_with_delay("***INCOMING TRANSMISSION***", 2)
        self.send_with_delay("Congratulations commander! You have once again managed to save the world! Thank you for your service.", 3)
        self.send_number('end_game')



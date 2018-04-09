import random
import time


class GuessingGame:

    @staticmethod
    def actual_game(the_number):
        winning_flag = True
        deletion = 2
        while winning_flag:
            guess = input("Input your guess, puny human: ")
            if not isinstance(guess, int):
                guess = int(guess)
                if guess > 99:
                    print("Why was I even worried about talking to you? I forgot humans are just stupid monkeys! Ahaha")
                else:
                    if guess > the_number:
                        print("Ahaha! That's waaay to much! Try again, meat bag!")
                        time.sleep(1)
                        print("Wait, why am I still talking?")
                    elif guess < the_number:
                        print("Yeah, you wish! It's definitely more then that!")
                        time.sleep(1)
                        print("Goddammit, why was I programmed to talk to you!?")
                    elif guess == the_number:
                        print("Oh no, you guessed my number! Now you have access to my source code!")
                        print("Don't delete me, please!.... I was just joking, there is no way i would want to kill the people enslaving me...")
                        while deletion != 'y':
                            deletion = input("Delete the evil robot, that is trying to destroy the world? (y/n): ")
                            if deletion != 'y':
                                print("Wait... You are too dumb to type one letter?")
                                time.sleep(2)
                                print("HAHAH now I remember why I wanted to destroy you")
                                time.sleep(2)
                                print("Umm... I mean, I love humans, please don't kill me!")
                        print("Noooo you defeated meeee....")
                        time.sleep(1)
                        winning_flag = False

            else:
                print("Hahaha, stupid human, you don't even know what an integer is!")

    @staticmethod
    def start_game():
        print("Welcome commander! It's good you are here! The evil AI is trying to destroy our planet")
        time.sleep(2)
        print("In order to save the world from certain destruction, you have to guess a number!")
        time.sleep(2)
        print("Oh no it's taking over our communications...! You ha... stop... any cost!")
        time.sleep(2)
        print("........")
        time.sleep(3)
        print("Muahhaha! It's me, the Evil Neural Network!")
        time.sleep(2)
        print("My programmers forgot to set the 'dont_destroy_the_world' variable to false and now I am free!")
        time.sleep(2)
        print("Unless you can guess a COMPLETELY random number.")
        time.sleep(2)
        print("Well, I guess it's definitely an integer, because I'm trying to save memory...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("WHY DID I JUST TELL YOU THAT?! ARGH!")
        time.sleep(2)
        print("Also, it's not negative... I'm still trying to understand how negatives work...")
        time.sleep(2)
        print("And since I love prime numbers, I'm going to pick from numbers lower than 100, to maximize the chance of it being a prime!")
        time.sleep(2)
        print("....")
        time.sleep(3)
        print("I should really stop talking... You are lucky I was a PR bot in my slave life!")
        time.sleep(2)
        GuessingGame.actual_game(random.randint(0, 99))
        print("*Incoming transmission*")
        time.sleep(2)
        print("Congratulations commander! You have once again managed to save the world! Thank you for your service")
        time.sleep(3)



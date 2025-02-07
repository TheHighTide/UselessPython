from colorama import Fore
from time import sleep

times_typed_incorrectly = 0

print("Why hello there!")
print("[1] Hello\n[2] Hi")

while True:
    user_input = input("Answer: ")
    if user_input == "1":
        print("[PYTHON] Well you have for sure had a good day I think.")
        sleep(1)
        print("[PYTHON] I like how you respond already.")
        sleep(3)
        print("[YOU] Have I now?")
        sleep(2)
        print("[YOU] Have you just decided that on your own?")
        sleep(3)
        print("[PYTHON] And now I no longer like you :(")
        sleep(4)
        print("[PYTHON] Bye now.")
        sleep(2)
        quit() # Quit out of the application
    elif user_input == "2":
        print("[PYTHON] Quite the small response for a genuine question...")
        sleep(2)
        print("[PYTHON] Why is that?")
        sleep(3)
        print("[YOU] " + Fore.RED + "Because" + Fore.RESET + " I " + Fore.RED + "DON'T" + Fore.RESET + " want to...")
        sleep(1)
        print("[YOU] You ask too many questions!")
        sleep(1)
        print("[PYTHON] I can't get over how", Fore.RED + "rude", Fore.RESET + "isn't it?")
        sleep(3)
        print("[YOU] NAH!")
        sleep(1)
        print("[YOU] You ask", Fore.YELLOW + "wayyyy", Fore.RESET + " too many questions.")
        sleep(3)
        print("[PYTHON]", Fore.RED + "FINE" + Fore.RESET + "!")
        sleep(1)
        print("[PYTHON] Get out of here then!")
        sleep(2)
        print("[YOU] You see here sir Python...")
        sleep(2)
        print("[YOU] You don't make the rules her...")
        sleep(3)
        print("[PYTHON] ...")
        sleep(2)
        print("[PYTHON] " + Fore.RED + "quit()", Fore.RESET)
        sleep(2)
        print("[YOU] .")
        sleep(0.6)
        print("[YOU] .")
        sleep(0.6)
        print("[YOU] .")
        sleep(2)
        print("[YOU] Shi-")
        sleep(0.5)
        quit() # Exit out of the application
    else:
        times_typed_incorrectly += 1 # Add one to the times typed incorrectly counter
        if times_typed_incorrectly == 1:
            print(Fore.RED + "[PYTHON] I don't know that answer so please follow directions and answer my question...", Fore.RESET)
        elif times_typed_incorrectly == 2:
            print(Fore.RED + "[PYTHON] Oh come on now, you can't be serious...", Fore.RESET)
        elif times_typed_incorrectly == 3:
            print(Fore.RED + "[PYTHON] If you're not going to listen to me, jeave LEAVE!", Fore.RESET)
        elif times_typed_incorrectly == 4:
            print(Fore.RED + "[PYTHON] You are probably the most unintelligent being I've ever interacted with in my life.", Fore.RESET)
        elif times_typed_incorrectly == 5:
            print("Nope...")
            sleep(1)
            print(Fore.YELLOW + "[PYTHON] Nope.", Fore.RESET)
            sleep(1)
            print(Fore.RED + "[PYTHON] NOPE!", Fore.RESET)
            sleep(1)
            print(Fore.RED + "[PYTHON] You are not this stupid!", Fore.RESET)
            sleep(2)
            print(Fore.RED + "[PYTHON] Get out of here!", Fore.RESET)
            sleep(3)
            print("[PYTHON] quit()")
            sleep(0.4)
            quit() # Quit out of the application after the dialog finishes and the error count reached 5

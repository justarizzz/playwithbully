import time
import sys
import os
import platform
import webbrowser

youareanidiot = "https://youareanidiot.cc/safe/"
devs_website = "https://justarizzz.github.io"
devs_github = "https://github.com/justarizzz"
funnysekaimusiclolidkwhattosay = "https://youtu.be/VWVtIg5cdDU?si=SoErNys1RJYKegFM"

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

print('This is a Bully! You have to make choices btw. Developed by Aria!')
time.sleep(3)
clear_screen()
print('Give me something great!')
time.sleep(0.09)
for i in range(10):
    print('great!')
time.sleep(2)
clear_screen()   
choice = input('What you want to give to Bully?: ')
if choice == 'candy':
    print("I'm gonna take your candy...")
    if i in range(100):
        print('candy...')
    time.sleep(2)
    clear_screen()
    print('Thanks for plaaaaaaaaying')
    time.sleep(1)  
    sys.exit(0)
elif choice == 'quarter':
    print('Thanks for the generous donation!...')
    if i in range(100):
        print('donation...')
    time.sleep(2)
    clear_screen()
    print('Thanks for plaaaaaaaaying')
    time.sleep(1)
    sys.exit(0)
elif choice == 'bsoda':
    print('Huh?')
    time.sleep(2)
    clear_screen()
    time.sleep(1)
    print('You wanted to get rid of me, huh?')
    time.sleep(0.5)
    print("Well, let's see how you can get rid of this! You are an idiot! Hahaha!")
    webbrowser.open(youareanidiot)
    time.sleep(0.7)
    sys.exit(0)
elif choice == 'aride':
    print("Oh, that devgirl's nickname? Well, that's a lil outta character, but hi! That's me! You found an easter egg. Once you'll see this, this window will close, as always.")
    time.sleep(1)
    print('...')
    time.sleep(0.1)
    print("Here, you can check my site and my GitHub. I'll now self close this.")
    webbrowser.open(devs_website)
    webbrowser.open(devs_github)
    time.sleep(2)
    clear_screen()
    print('Thanks for plaaaaaaaaying')
    time.sleep(0.05)
    sys.exit(0)
    # Пасхалка / An Easter egg (1, maybe)
elif choice == "no items":
    print("What? No items? No items, no pass...")
    for i in range(100):
        print("no pass...")
    time.sleep(2)
    clear_screen()
    time.sleep(1)    
    sys.exit(0)
elif choice == 'nyan.mp3':
    print("A note from Aria: 'Uhh...nyan.mp3 is the best!' This game will close now.")
    time.sleep(2)
    sys.exit(0)
else:
    print("I'll take that! It's mine now...")
    for i in range (100):
        print('now...')
    time.sleep(1)
    clear.screen()
    time.sleep(0.05)
    print('...')
    time.sleep(1)
    print("Or is it? You've entered something that's else from what I expected.")
    time.sleep(1)
    print("But hey! Don't be sad. Here's a cool music I found. Have a nice day :)")
    webbrowser.open(funnysekaimusiclolidkwhattosay)
    time.sleep(1)
    clear_screen()
    print('Thanks for plaaaaaaaaying')
    time.sleep(0.05)
    sys.exit(0)
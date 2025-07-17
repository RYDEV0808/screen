# To get previous versions of setup, select "Blame" (top-left)
# Please read "README.md" in the repository's Files
# Download this file

def scan() :
    try :
        import pygame
        print("screen requirment satisfied")
    except :
        import platform

        system = platform.system()
        if system == "Windows" :
            try :
                print("Installing Pygame...\n")
                pygame_install = "pip install pygame"
                import subprocess

                subprocess.run(pygame_install, shell=True)
                print("Pygame installed")
            except :
                pygame_install = "pip install pygame"
                print("Unidentified error")
                print(f"Please install pygame manually in cmd with \"{pygame_install}\"")

    print("\n\nscreen V1.0 -- GitHub repository\n")
    print("Hello!\n")

scan()

import pygame

class Screen :
        def __init__(self, width, height,caption) :

            self.width = width
            self.height = height
            self.caption = caption

            self.display = pygame.display.set_mode((self.width, self.height))

        def GetScreen(self) :
            return self.display
        def info(self) :
            print("\n\nINFO\n\n")
            print(f"Width : {self.width}")
            print(f"Height : {self.height}")
            print(f"Caption : {self.caption}")
        def ExitCondition(self) :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    from sys import exit

                    exit()
        def GetEvent(self) :
            self.event = pygame.event.get()
            return self.event
        

def Defo(caption) :
    print("Setting window with default atribute")

    width, height = 700, 600
    display = Screen(width, height, caption)

    return display
                

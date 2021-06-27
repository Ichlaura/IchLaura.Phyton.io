

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 4
# W04 - Prove : Homework - Data Structures
#Articulate the strengths and weaknesses of Linked Lists.
#Use Linked Lists in Python to solve problems.

#deque
from collections import deque

#creo la clase song
class Song:
    #con variables title y artist
    def __init__(self):
        self.title = "No title"
        self.artist = "No artist"

#que deberia tenet una función prompt que pregunte al usuario el titulo y el artista de la canción 
    def prompt(self):
        self.title = input("Enter title name: ")
        self.artist = input("Enter artist name: ")
        
# creó una función display que muestra en la pantalla el titulo y el artista
    def display(self):
        print("Playing song: ")
        print("{} by {}".format(self.title, self.artist))

#aqui creo un main loop 
def main():
    #deque
    playlist = deque()

    # le coloco nombre Song
    s = Song()

    # el menu 
    menu = 0
# creó un bucle "while" que termina hasta que se tenga el 4

    while menu != 4:

#lo que aparece en la pantalla para el usuario
        print("Options: ")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
 #el menu de los 4        
        menu = int(input("Enter selection: "))

        # Add a new song to the end of the playlist
        if menu == 1:
            s.prompt()
            playlist.append(s)

        # Insert a new song to the beginning of the playlist
        elif menu == 2:
            s.prompt()
            playlist.appendleft(s)
#Play the next song y quit
        elif menu == 3:
            if len(playlist) == 0:
                print("The playlist is currently empty")
            else:
                s = playlist.popleft()
                s.display()
        print("\n")

    print("Goodbye")


if __name__ == "__main__":
    main()
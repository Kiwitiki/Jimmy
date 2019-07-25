import textwrap
import clinical
import tiles


class Adventure(object):
    def prompt(self):
        x = input.lower("Type a command: ")
        return(x)

########################################### beginning stats ###########################################

    def __init__(self):
        self.gold = 2
        self.health = 10
        self.energy = 10
        self.melee = 1
        self.ranged = 0
        self.ammo = 0
        self.full_health = 10
        self.attack_num = 0

    def checkstats(self):
        global = ranged
        print('''
        ********''')
        print("Gold:", self.gold)
        print("Health:", self.health, "/", self.full_health)
        print("Melee:", self.melee)
        print("Energy:", self.energy)

        if ranged > 0:
            print("Ranged:", ranged)
            print("Ammo:", ammo)

########################################### Greeting ###########################################

    def start(self):
        msg = textwrap.dedent('''
        ****************************************
        *                                      *
        *      *Welcome to Jimmy's World*
        *                                      *
        ****************************************
        ''')
        print(msg)
        self.StartingRoom()

        if player in StartingRoom():
          command = input(prompt)
           if command == "1":
                Room_description()
            elif command == "2":
                print("********")
                print (
                    "You're hiding behind a chair thats right in front of you. You hear a strange noise from the back of the room.")
            elif command == "9":
                checkstats()
                StartingRoom()
            else:
                StartingRoom()


def main():
    adventure = Adventure()
    adventure.start()


if __name__ == '__main__':
    main()

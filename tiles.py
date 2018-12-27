import items
import textwrap
import clinical

########################################## Starting tiles ########################################
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

# all directions
directions = ("norden", "osten", "süden", "westen", "oben", "unten")



########################################### Rooms #############################################   


    class StartingRoom(MapTile):
        def intro_text(self):
            print("""
            You find yourself in a big, square room.
            It looks abandoned and smells musty.
            """)



            
        def modify_player(self, player):
            #Room has no action on player
            pass


    class LootRoom1(MapTile):
        def intro_text(self):
            print("""
            A big Room full of old Chests. Most of them are open and only filled with spiderwebs. You can feel a cold wind and wonder where it comes from. You cant see any windows.
            You are standing at the door on the South. Through some spiderwebs that are filled with dust you can see a door to the West. It is a dark wooden Door.
            Around the Door are scratches that look like a giant cat made them.
            """)

            look_around = print("""
            In one chest on your right you can see a Gummy Bear laying next to an Apple.
            On the North site of the Room is an old Carpet. the left side of the Carpet is covored in Blood.""")

        def __init__(self, x, y, item):
            self.item = item
            super().__init__(x, y)

        def add_loot(self, player):
            player.inventory.append(self.item)

        def modify_player(self, player):
            self.add_loot(player)
                

class LootRoom2(MapTile):
    def intro_text():
        print("""
        A tiny, square Room. It looks like a Cabin and is filled with wooden Planks that might one time were furniture. A long long time ago.
        The wall in the West is covered with old blood. The wallpaper comes off the walls and you cant even say anymore what colour it once was.
        It is very cold in there and you shiver.""")

        look_around = print("""
        Through some of the plankets you see something shimmering. As you look further you discover a door leading to the North. 
        Moss is growing around it. The way is lightly blocked but you could make it through the plankets.
        """)
    
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
            player.inventory.append(self.item)

        def modify_player(self, player):
            self.add_loot(player)


    class EnemyRoom(MapTile):
        def intro_text():
            print("""
            It is dark in here. You need some time to be able to see clearly. When you begin seeing some silhouettes, you suddenly hear a dull sound as if something heavy had fallen down.
            Your knees begin to shake. Heavy steps are comming closer. Your eyes are searching in the dark.
            It stops. Something is breathing. 
            """)

            if input(prompt) == "hello" or "hi" or "who is there" or "?" or "what":
                print("""A deep voice is softly speaking:
                > You are alone.
                > You have no idea whose home you just entered.
                > Speak. Are you a hero or a chicken?
                """)

        def __init__(self, x, y, enemy):
            self.enemy = enemy
            super().__init__(x, y)

        def modify_player(self, the_player):
            if self.enemy.is_alive():
                the_player.hp = the_player.hp - self.enemy.damage
                print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))


    class Cellar(MapTile):
        def __init__(self, x, y, item):
            self.item = item
            super().__init__(x,y)

        def add_loot(self,player):
            player.inventory.append(self.item)

        def modify_player(self, player):
            self.add_loot(player)


    class EnemyRoom(MapTile):
        def __init__(self, x, y, enemy):
            self.enemy = enemy
            super().__init__(x, y)

        def modify_player(self, the_player):
            if self.enemy.is_alive():
                the_player.hp = the_player.hp - self.enemy.damage
                print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))

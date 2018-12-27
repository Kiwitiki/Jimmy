import items
import textwrap


########################################## Starting tiles ########################################
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


########################################### Rooms #############################################   


    class StartingRoom(MapTile):
        def intro_text(self):
            print("""
            You find yourself in a big, square room.
            It looks abandoned and smells musty.
            """)
            print("""Options: 
            (1) look around 
            (2) hide
            (9) show stats""")
        def Room_description():
            print("""
            halo 
            """)



            
        def modify_player(self, player):
            #Room has no action on player
            pass


    class LootRoom(MapTile):
        def __init__(self, x, y, item):
            self.item = item
            super().__init__(x, y)

        def add_loot(self, player):
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


        def main():
            adventure = Adventure()
            adventure.start()


            if __name__ == '__main__':
                main()

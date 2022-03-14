# Western Wilson
# Te Hiku Media python test

# With more time I would:
#  - Add restart functionality
#  - Add slot class, with row and board classes, so we can make it generic how many rows we add for our board
#  - Create a game state object for state, rather than use a list
#  - Add a Player class that uses player names, player token and their number
#  - control the game state from within the Game class
#  - optimise the win condition loop, to only check current token added

class Game():
    """Tic Tac Toe game
    """

    def __init__(self, state=[0, 0, 0, 0, 0, 0, 0, 0, 0]):
        """create the base state for tic tac toe
        Args:
            state (list): list of length nine, representing the game state
                0 = empty slot
                1 = player one slot
                2 = player two slot

        Raises:
            ValueError: if list is not len nine, return value error
        """

        if len(state) == 9:
            self.state = state
        else:
            raise ValueError("game state has too many values, it should only include list of nine")
        self.completed = False
    
    def get_available_slot_indexes(self):
        result = []
        for i, x in enumerate(self.state):
            if x == 0:
                result.append(i)
        return result

    def check_slot_available(self):
        """Check if we have any 0's left, this means available slots"""
        if 0 in self.state:
            # yes there is a spot left
            return True
        return False

    def insert_token(self, pos, player):
        """Insert a token into the game state

        Args:
            pos (int): position we want to add our value
            player (int): the current player

        Raises:
            ValueError: if player or pos are not numbers
            TypeError: if incorrect type is passed in

        Returns:
            bool: if successful or not
        """

        # validate the player
        if player == 0 or player > 2:
            raise ValueError("incorrect player number given, should be either 1 or 2")
        # validate the position is valid
        if pos < 0 or pos > 8:
            raise ValueError("incorrect pos number given, should be between 0 and 8 respectively")

        # check what how we are inserting it
        if self.state[pos] == 0:
            self.state[pos] = player
            return True
        elif self.state[pos] == 1 or self.state[pos] == 2:
            print("player token already exists in that spot, try a valid spot")
            print()
            return False
        else:
            print("that position is invalid, please use a valid spot")
            print()
            return False

    def check_game_won(self):
        """checks if our player has won"""

        # check all win conditions
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]        
        for condition in win_conditions:
            pos1 = self.state[condition[0]]
            pos2 = self.state[condition[1]]
            pos3 = self.state[condition[2]]

            # if any value is zero, then check next condition
            if pos1 == 0 or pos2 == 0 or pos3 == 0:
                continue
            # if all three contain same value, we have a winner
            if (pos1 == pos2 == pos3):
                return True
        
        return False

    def __get_out_str(self, value, index):
        """return a list to help with output string"""
        if value == 1:
            return f"{index}, O"
        if value == 2:
            return f"{index}, X"
        
        return f"{index}, _"

    def print_game_board(self):
        """outputs the board to text
        """
        print(f'[ {self.__get_out_str(self.state[0], 0)} ] [ {self.__get_out_str(self.state[1],1)} ] [ {self.__get_out_str(self.state[2],2)} ]')
        print(f'[ {self.__get_out_str(self.state[3],3)} ] [ {self.__get_out_str(self.state[4],4)} ] [ {self.__get_out_str(self.state[5],5)} ]')
        print(f'[ {self.__get_out_str(self.state[6],6)} ] [ {self.__get_out_str(self.state[7],7)} ] [ {self.__get_out_str(self.state[8],8)} ]')

    def restart(self):
        # with more time I would implement a restart feature
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.completed = False
    

def start():
    # create the blank state game
    game = Game()

    # while the game is running flip between our players
    # Game flow:
    # 1. check user input
    # 2. use that input to add to slots on board
    # 3. check if the game has been won
    # 4. Finish if game won, all spots filled, or player types exit
    is_player_one = True
    while (True):
        if is_player_one:
            player = 1
            token = "O"
        else:
            player = 2
            token = "X"
        
        player_wants_out = False
        # 1. check that the user enters proper data
        while (True):
            game.print_game_board()
            value = input(f"Player {player} = {token}, where would you like to put your token? ")
            # check value is not restart or exit
            if value.strip().lower() == 'exit':
                print(f"Player {player} has given up, I'll allow it...")
                player_wants_out = True
                break
            if value.strip().lower() == 'restart':
                print(f"Player {player} asked to restart... declined as not implemented yet! Sorry :)")
                break
            try:
                pos = int(value.strip())
                # 2. try insert into board
                success = game.insert_token(pos, player)
                if success:
                    game.print_game_board()
                    print()
                    print()
                    break
            except ValueError:
                print(f"the token value you are entering is invalid, must be a number between 0 and 8. Try again?")
        # exit the game if player wants out
        if player_wants_out:
            break

        # 4. double check that the slots are available
        if not game.check_slot_available():
            print("No slots left so game ends in a DRAW!!")
            break

        # 3. check if the game is won
        is_game_won = game.check_game_won()
        if is_game_won:
            print(f"Winner is Player {player} with token {token}, congrats!")
            break
        
        # flip the player boolean
        is_player_one = not is_player_one


def usage():
    print('Welcome to tic tac toe:')
    print(' > Player One goes first followed by Player Two')
    print(' > Type and enter the number where you want to add your token')
    print(' > You will see the board in text representation after each entry,')
    print("   if a value already exists, you'll get an error and be asked to try again.")
    print(' > Winner is the first person to match 3 in a row, can be horizontal, vertical or diagonally')
    print()
    print("The board will show each available position and what is currently there. i.e.")
    print(" [ 0,_ ] <- first entry is position, second is your tokens")
    print()
    print("Useful commands:")

    print(" > exit - exits the game")
    print(" > restart - restarts the game once implemented ;)")
    print()

def fin():
    print("Game Over!!!")

if __name__ == "__main__":
    # This is the entry point
    print("Starting tic tac toe!")
    # print out our usage
    usage()
    # start our game
    start()
    # finish the game
    fin()

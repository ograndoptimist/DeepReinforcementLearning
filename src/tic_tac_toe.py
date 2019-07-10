"""
    The TicTacToe Game.
"""
import time


TABLE = \
        """
               {0} |   {1}    |  {2}     
          -------+--------+--------
               {3} |   {4}    |  {5}      
          -------+--------+--------
               {6} |   {7}    |  {8}
        """


class TicTacToe(object):
    def __init__(self):
        self.table_configuration = [' ' for _ in range(9)]
        self.player_one = 'X'
        self.player_two = 'O'

    def print_table(self):
        print(TABLE.format(self.table_configuration[0], self.table_configuration[1],
                           self.table_configuration[2], self.table_configuration[3],
                           self.table_configuration[4], self.table_configuration[5],
                           self.table_configuration[6], self.table_configuration[7],
                           self.table_configuration[8]))

    def check_end_game(self):
        for position in self.table_configuration:
            if position not in ['X', 'O']:
                return False
        return True

    def player_turn(self):
        turn = False
        while not turn:
            turn = int(input('Enter a position number: '))
            if self.table_configuration[turn] != ' ':
                turn = False
            else:
                self.table_configuration[turn] = 'X'
                break

    def play_game(self):
        while not self.check_end_game():
            self.print_table()
            self.player_turn()
            time.sleep(2)


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()

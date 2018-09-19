# Abrar Rouf
# CS 100 2017F Section H01
# HW 17, Nov 29, 2017


class TTTGame:
    """Creates a game of Tic Tac Toe with two players."""
    def __init__(self, grid_size):
        print('Welcome to Tic Tac Toe! The rules are simple: get three in a row of your team shape before your opponent'
              ' does. The grid is numbered a la Battleship style with rows labeled with numbers and columns\nlabeled as'
              ' letters. For example, the center square is 2B and the top-left grid is 1A. Please use this format when '
              'entering move commands.')
        import turtle
        self.turt = turtle.Turtle()
        self.screen = turtle.Screen()
        self.size = grid_size
        self.player1_name = input('Player 1, what is your name?\n')
        self.player2_name = input('Player 2, what is your name?\n')
        self.player1_turn_count = 0
        self.player2_turn_count = 0
        self.total_turn_count = 0
        team_choice = ['X', 'O']
        self.player1_team = input('%s, please choose either X or O.\n' % self.player1_name)
        print('%s has chosen team %s.\n' % (self.player1_name, self.player1_team))
        for choice in team_choice:
            if choice == self.player1_team:
                team_choice.remove(self.player1_team)
        self.player2_team = team_choice[0]
        print('%s is on team %s.\n' % (self.player2_name, self.player2_team))
        self.player_turn = 1
        self.player1_turn_prompt = ''
        self.player2_turn_prompt = ''
        self.player1_move_list = []
        self.player2_move_list = []
        self.win_condition = False
        self.win_conditions = [['1A', '1B', '1C'], ['2A', '2B', '2C'], ['3A', '3B', '3C'], ['1A', '2A', '3A'], ['1B',
                               '2B', '3B'], ['1C', '2C', '3C'], ['1A', '2B', '3C'], ['3A', '2B', '1C']]

    def grid(self):
        print('Drawing grid, please wait...')
        self.turt.speed(10)
        self.turt.pu()
        self.turt.lt(90)
        self.turt.fd((1/6)*self.size)
        self.turt.rt(90)
        self.turt.back(0.5*self.size)
        self.turt.pd()
        for i in range(1):
            self.turt.fd(self.size)
            self.turt.pu()
            self.turt.back(self.size)
            self.turt.rt(90)
            self.turt.fd((1/3)*self.size)
            self.turt.lt(90)
            self.turt.pd()
            self.turt.fd(self.size)
        self.turt.back((1/3)*self.size)
        self.turt.lt(90)
        self.turt.back((1/3)*self.size)
        self.turt.fd(self.size)
        self.turt.lt(90)
        self.turt.pu()
        self.turt.fd((1/3)*self.size)
        self.turt.lt(90)
        self.turt.pd()
        self.turt.fd(self.size)
        self.turt.pu()
        self.turt.home()
        self.turt.back((0.5*self.size)+50)
        self.turt.write('2', font=('Arial', 16, 'normal'))
        self.turt.rt(90)
        self.turt.fd((1/3)*self.size)
        self.turt.write('1', font=('Arial', 16, 'normal'))
        self.turt.back((2/3)*self.size)
        self.turt.write('3', font=('Arial', 16, 'normal'))
        self.turt.back((1/6)*self.size)
        self.turt.lt(90)
        self.turt.fd(((1/6)*self.size)+40)
        self.turt.write('A', font=('Arial', 16, 'normal'))
        self.turt.fd((1/3)*self.size)
        self.turt.write('B', font=('Arial', 16, 'normal'))
        self.turt.fd((1/3)*self.size)
        self.turt.write('C', font=('Arial', 16, 'normal'))
        self.turt.home()
        self.turt.back((0.5*self.size)+50)
        print('Done! NOTE: Clicking on the grid itself will cause it to close.')

    def game_state(self):
        self.total_turn_count = (self.player1_turn_count + self.player2_turn_count)
        if self.total_turn_count != 9:
            if self.player_turn == 1:
                self.player1_turn_count += 1
                Game.get_player_move()
            elif self.player_turn == 2:
                self.player2_turn_count += 1
                Game.get_player_move()
        elif self.total_turn_count == 9:
            return print('Maximum amount of possible turns reached.\nGame will now exit.')

    def draw_X(self):
        self.turt.pd()
        self.turt.lt(45)
        self.turt.back((1/6)*self.size)
        self.turt.fd((1/3)*self.size)
        self.turt.back((1/6)*self.size)
        self.turt.rt(90)
        self.turt.back((1/6)*self.size)
        self.turt.fd((1/3)*self.size)
        self.turt.pu()
        self.turt.back((1/6)*self.size)
        self.turt.lt(45)

    def draw_O(self):
        self.turt.fd((1/6)*self.size)
        self.turt.pd()
        self.turt.lt(90)
        self.turt.circle((1/6)*self.size)
        self.turt.rt(90)
        self.turt.pu()
        self.turt.back((1/6)*self.size)

    def get_player_move(self):
        if self.player_turn == 1:
            self.player_turn += 1
            self.player1_turn_prompt = input('%s, it is your turn - what is your move? (Enter a coordinate. For example'
                                             ' "1A".)\n' % self.player1_name)
            for i in range(len(self.player1_turn_prompt)):
                if self.player1_turn_prompt[0] == '1':
                    self.turt.rt(90)
                    self.turt.fd((1/3*self.size))
                    self.turt.lt(90)
                    break
                elif self.player1_turn_prompt[0] == '2':
                    break
                elif self.player1_turn_prompt[0] == '3':
                    self.turt.lt(90)
                    self.turt.fd((1/3)*self.size)
                    self.turt.rt(90)
                    break
            for i in range(len(self.player1_turn_prompt)):
                if self.player1_turn_prompt[1] == 'A':
                    self.turt.fd(((1/6)*self.size)+40)
                    if self.player1_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player1_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
                elif self.player1_turn_prompt[1] == 'B':
                    self.turt.fd(((1/2)*self.size)+50)
                    if self.player1_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player1_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
                elif self.player1_turn_prompt[1] == 'C':
                    self.turt.fd(self.size-50)
                    if self.player1_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player1_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
            self.player1_move_list += [self.player1_turn_prompt]
            Game.game_state()
        elif self.player_turn == 2:
            self.player_turn -= 1
            self.player2_turn_prompt = input('%s, it is your turn - what is your move? (Enter a coordinate. For example' 
                                             ' "2B".)\n' % self.player2_name)
            for i in range(len(self.player2_turn_prompt)):
                if self.player2_turn_prompt[0] == '1':
                    self.turt.rt(90)
                    self.turt.fd((1 / 3 * self.size))
                    self.turt.lt(90)
                    break
                elif self.player2_turn_prompt[0] == '2':
                    break
                elif self.player2_turn_prompt[0] == '3':
                    self.turt.lt(90)
                    self.turt.fd((1/3)*self.size)
                    self.turt.rt(90)
                    break
            for i in range(len(self.player2_turn_prompt)):
                if self.player2_turn_prompt[1] == 'A':
                    self.turt.fd(((1/6)*self.size)+40)
                    if self.player2_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player2_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
                elif self.player2_turn_prompt[1] == 'B':
                    self.turt.fd(((1/2)*self.size)+50)
                    if self.player2_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player2_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
                elif self.player2_turn_prompt[1] == 'C':
                    self.turt.fd(self.size - 50)
                    if self.player2_team == 'X':
                        Game.draw_X()
                        self.turt.goto(-350, 0)
                        break
                    elif self.player2_team == 'O':
                        Game.draw_O()
                        self.turt.goto(-350, 0)
                        break
                    break
            self.player2_move_list += [self.player2_turn_prompt]
            Game.game_state()


Game = TTTGame(600)
Game.grid()
Game.game_state()

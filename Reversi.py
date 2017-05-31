import random
import sys


def gameBoard(tile):
      print("       1   2   3   4   5   6   7   8")
      print("     +---+---+---+---+---+---+---+---+")

      for col in range (1,9):
            print("     |   |   |   |   |   |   |   |   |")
            print("  %s  |" %col, end=' ')
            for row in range(1,9):
                  print(tile[col][row], end=' ')
                  print("|", end=' ')

            print()            
            print("     |   |   |   |   |   |   |   |   |")
            print("     +---+---+---+---+---+---+---+---+")

def ChoosePlayer():
      print("Do you want to be X or O?")
      player = input()
      while player != 'x' and player != 'o' and player != 'X' and player !='O':
            print("Plase choose one or the following letters: X or O")
            player = input()

      return player

def FirstTurn():
      turn = random.randint(1,2)
      if turn == 1:
            turn = True
            print("You will go first")
      elif turn ==2:
            turn = False
            print("The computer will go first.")
      return turn

def PickColumn():
      print("Pick a column for your next move: (1-8)")
      col = input()
      while col not in '12345678':
            print("Please enter a number between 1-8")
            col = input()

      col = int(index)
      return col

def PickRow():
      print("Pick a column for your next move: (1-8)")
      row = input()
      while row not in '12345678':
            print("Please enter a number between 1-8")
            row = input()

      row = int(index)
      return row

def CheckValidMove(tile, row, col, turn, player, computer):
      if turn == true:
            

      elif turn == false

      if validmove == False
      return 


def Scores(tile, Player, Computer):
      PlayerScore = 0
      ComputerSCore = 0

      for col in range(1,9):
            for row in range(1,9):
                  if tile[col][row] == Player:
                        PlayerScore += 1
                  if tile[col][row] == Computer:
                        ComputerScore += 1
      print("You have " +PlayerScore," points. The computer has " +ComputerScore," points")
      
      


play_again = 'yes'
while play_again == 'yes':

      print("R E V E R S I")
      tile = []
      for i in range(9):
            tile.append([' '] * 9)
      
      tile[4][4] = tile[5][5] = 'X'
      tile[5][4] = tile[4][5] = 'O'
      gameBoard(tile)

      player = ChoosePlayer()
      player = player.upper()
      if player == 'X':
            computer = 'O'
      else:
            computer = 'X'

      turn = FirstTurn()

      game_over = False
      while game_over == False:

            if turn == True:
                  col = PickColumn()
                  row = PickRow()
                  while tile[col][row] != ' ':
                        print("Please enter a free tile number.")
                        col = PickColumn()
                        row = PickRow()
                  move = CheckValidMove(tile,row_move,col_move)
                  while move == False:
                        col = PickColumn()
                        row = PickRow()
                        while tile[col][row] != ' ':
                              print("Please enter a free tile number.")
                              col = PickColumn()
                              row = PickRow()
                        move = CheckValidMove(tile ,row ,col, turn, player, computer)
                        
                  gameBoard(tile)





      print("Do you want to play again?")
      play_again = input()
      if play_again != 'yes':
            print("Goodbye.")

                  
                  



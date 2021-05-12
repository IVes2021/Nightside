from ramdon import radient

def computer_number(max,min):
  return radient(min,max)

def player_number(max,min):
    usr_input=int(input(f'guess a number between {max} and {min}: '))
    return usr_input

def paly():
  low=0
  high=10
  
  
  computer_choice=computer_number(high,low)
  player_choice=player_number(high,low)
  
  while player_choice != computer_choice:
      if player_choice > computer_choice:
        player_choice=int(input("The number you guess is too large!! Please try again: "))
      else:
        player_choice=int(input("The number you guess is too small!! Please try again: "))
        
  print(f'congratulations! You managed to guess the number {computer_choice}')
  
  
play()

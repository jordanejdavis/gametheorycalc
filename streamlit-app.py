import streamlit as st
import numpy as np


st.header("Enter payoffs from left to right, top to bottom (of the matrix)")
game_dict = {}

def msne(first, second, third, fourth):
  x = np.round((fourth - second) / (first - second - third + fourth), 2)
  return [x, (1 - x)]

def twobytwo():
# Collecting the payoffs - most likely by a user input box per payoff
  game_list = [[[], []], [[], []]]
  for i in range(0, 8):
      game_dict[i] = st.number_input(f"Enter payoff {i+1}", value=1)
  game_list[0][0] = [game_dict[0], game_dict[1]]
  game_list[0][1] = [game_dict[2], game_dict[3]]
  game_list[1][0] = [game_dict[4], game_dict[5]]
  game_list[1][1] = [game_dict[6], game_dict[7]]
  check_dominant = 0
  # Checking strictly dominated strategy for player 1:
  if game_dict[0] > game_dict[4] and game_dict[2] > game_dict[6]:
      print("Choice T is the dominant strategy for player 1")
      check_dominant += 1
  elif game_dict[0] < game_dict[4] and game_dict[2] < game_dict[6]:
      print("Choice B is the dominant strategy for player 1")
      check_dominant += 1

  # Checking strictly dominated strategy for player 2:
  if game_dict[1] > game_dict[3] and game_dict[5] > game_dict[7]:
      print("Choice L is the dominant strategy for player 2")
      check_dominant += 1
  elif game_dict[1] < game_dict[3] and game_dict[5] < game_dict[7]:
      print("Choice L is the dominant strategy for player 2")
      check_dominant += 1

  # If check doesn't equal 2, the game does not have a dominant equilbrium and must be solved via nash
  if check_dominant != 2:
      check_psne = 0
      if game_dict[0] > game_dict[4] and game_dict[1] > game_dict[3]:
          print("PSNE is (T,L)")
          check_psne += 1
      if game_dict[4] > game_dict[0] and game_dict[5] > game_dict[7]:
          print("PSNE is (B,L)")
          check_psne += 1
      if game_dict[2] > game_dict[6] and game_dict[3] > game_dict[1]:
          print("PSNE is (T,R)")
          check_psne += 1
      if game_dict[6] > game_dict[2] and game_dict[7] > game_dict[5]:
          print("PSNE is (B,R)")
          check_psne += 1
      if check_psne == 0 or check_psne > 1:
          p = msne(game_dict[1], game_dict[5], game_dict[3], game_dict[7])[0]
          oneMinusP = msne(game_dict[1], game_dict[5], game_dict[3], game_dict[7])[1]
          q = msne(game_dict[0], game_dict[2], game_dict[4], game_dict[6])[0]
          oneMinusQ = msne(game_dict[0], game_dict[2], game_dict[4], game_dict[6])[1]
          print("MSNE solution")
          print(
              f"P1 plays mixed strategy of (T, B) = {msne(game_dict[1], game_dict[5], game_dict[3], game_dict[7])} "
              f"with expected payoff {np.round((game_dict[0] * q) + (game_dict[2] * oneMinusQ), 2)}")

          print(
              f"P2 plays mixed strategy of (L, R) = {msne(game_dict[0], game_dict[2], game_dict[4], game_dict[6])} "
              f"with expected payoff {np.round((game_dict[1] * p) + (game_dict[5] * oneMinusP), 2)}")
twobytwo()




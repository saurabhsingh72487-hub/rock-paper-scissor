from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Test against all bots

print("Playing against Quincy...")
play(player, quincy, 1000, verbose=False)

print("Playing against Abbey...")
play(player, abbey, 1000, verbose=False)

print("Playing against Kris...")
play(player, kris, 1000, verbose=False)

print("Playing against Mrugesh...")
play(player, mrugesh, 1000, verbose=False)

# Uncomment to run tests
# import test_module

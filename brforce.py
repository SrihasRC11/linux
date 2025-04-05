import subprocess
from itertools import product

def try_path(moves):
    result = subprocess.run(["./glade"], input=moves.encode(), capture_output=True)
    out = result.stdout.decode()
    if "flag" in out:
        print("Found flag with moves:", moves)
        print(out)
        return True
    return False

# Try all combinations up to 10 moves
for length in range(1, 11):
    for moves in product("wasd", repeat=length):
        path = ''.join(moves)
        if try_path(path):
            exit()

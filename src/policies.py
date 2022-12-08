import numpy as np

def get_reward(state: np.ndarray, action: int) -> float:
    if action == 0:  # move left
        if state[0, 1] == 2:  # water
            return -1.0
        elif state[0, 1] == 5:  # mountain
            return -0.5
        else:
            return 0.0
    elif action == 1:  # move right
        if state[0, 1] == 2:  # water
            return -1.0
        elif state[0, 1] == 5:  # mountain
            return -0.5
        else:
            return 0.0
    elif action == 2:  # move up
        if state[0, 1] == 2:  # water
            return -1.0
        elif state[0, 1] == 5:  # mountain
            return -0.5
        else:
            return 0.0
    elif action == 3:  # move down
        if state[0, 1] == 2:  # water
            return -1.0
        elif state[0, 1] == 5:  # mountain
            return -0.5
        else:
            return 0.0

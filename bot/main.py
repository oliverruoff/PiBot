import math

import motor_controls as mc
from usdar import detection

if __name__ == "__main__":
    env_map = detection.scan_360()
    distances = [(x, y, math.sqrt(x*x+y*y)) for x, y in env_map]
    max_dist = distances[[i[2]
                          for i in distances].index(max([i[2]
                                                         for i in distances]))]
    angle_to_turn = math.degrees(math.atan2(max_dist[0], max_dist[1]))
    if angle_to_turn < 0:
        angle_to_turn = 360 + angle_to_turn
    print('I should turn now:', angle_to_turn, '°.')

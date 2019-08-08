import math

import motor_controls as mc
from usdar import detection


def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


if __name__ == "__main__":
    env_map = detection.scan_360()
    distances = [(x, y, math.sqrt(x*x+y*y)) for x, y in env_map]
    max_dist = distances[[i[2]
                          for i in distances].index(max([i[2]
                                                         for i in distances]))]
    angle_to_turn = angle((0, 1), (max_dist[0], max_dist[1]))
    print('I should turn now:', angle_to_turn, '°.')

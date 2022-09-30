from operator import contains

def normalize(key, value):
    match key:
        case contains('d'):  # distance
            return value / 128

        case contains('v'):  # velocity
            return value / 256

        case contains('a'):  # acceleration
            return value / 2048

        case contains('y'):  # yaw
            return value / 16384

        case contains('p'):  # probability
            return value / 128

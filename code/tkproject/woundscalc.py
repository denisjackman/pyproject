'''
This takes the total hit points for a pathfinder creature
and calculates the severity of wounds based on the following

Light - 10% ot total hit points lost
Moderate - 30% of total hit points lost
Severe - 60% of total hit points lost

This will allow the game master to quickly determine
the next action of the creature
based on the severity of the wounds
'''


def calc_wounds(cw_hit_points):
    ''' calculate the severity of wounds '''
    cw_light = cw_hit_points * 0.10
    cw_moderate = cw_hit_points * 0.30
    cw_severe = cw_hit_points * 0.60
    print(f"The total hit points of the creature are: {cw_hit_points}")
    print("The severity of the wounds are as follows:")
    print(f"Light wounds: {cw_light}")
    print(f"Moderate wounds: {cw_moderate}")
    print(f"Severe wounds: {cw_severe}")


def main():
    ''' main function '''
    print("Enter the total hit points of the creature")
    hit_points = int(input())
    calc_wounds(hit_points)


if __name__ == '__main__':
    main()

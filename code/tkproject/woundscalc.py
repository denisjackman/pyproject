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


def calc_wounds(cw_hit_points, cw_name="Default Creature"):
    ''' calculate the severity of wounds '''
    cw_light = cw_hit_points * 0.10
    cw_moderate = cw_hit_points * 0.30
    cw_severe = cw_hit_points * 0.60
    print(f"\t[=] The total hit points of the {cw_name} are: {cw_hit_points}")
    print("\t[=] The severity of the wounds are as follows:")
    print(f"\t[=] Light wounds: {int(cw_light)}")
    print(f"\t[=] Moderate wounds: {int(cw_moderate)}")
    print(f"\t[=] Severe wounds: {int(cw_severe)}")


def main():
    ''' main function '''
    main_loop = True
    print("[+] Pathfinder Creature Wounds Calculator started")
    while main_loop:
        print("[-] Enter the total hit points of the creature (q to quit):")
        main_name = input("[-] Creature name: ")
        main_input = input("[-] Number of hit points: ")
        if main_input[0].lower() == 'q':
            main_loop = False
            break
        if not main_input.isnumeric():
            print("[+] Please enter a number")
            continue
        main_hit_points = int(main_input)
        if main_name == "":
            calc_wounds(main_hit_points)
        else:
            calc_wounds(main_hit_points, main_name)
    print("[+] Exiting Pathfinder Creature Wounds Calculator")


if __name__ == '__main__':
    main()

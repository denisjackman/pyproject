def direction(player_input):
    check = player_input[0].upper()
    if check == 'N':
        result = "Go North!"
    elif check == 'S':
        result = "Go South!"
    elif check == 'E':
        result = "Go East!"
    elif check == 'W':
        result = "Go West!"
    else:
        result = "Invalid action!"
    return result


print direction("North")
print direction("s")
print direction("eastern")
print direction("WWWW")
print direction("xxx")
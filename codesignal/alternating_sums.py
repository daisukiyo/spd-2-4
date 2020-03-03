# You are given an array of positive integers - the weights of the people.
# Return an array of two integers, where the first element is the total weight of team 1
# and the second element is the total weight of team 2 after the division is complete.

def alternatingSums(a):
    team_1 = 0
    team_2 = 0
    for i in range(len(a)):
        if i % 2 == 0:
            team_1 += a[i]
        else:
            team_2 += a[i]

    return [team_1, team_2]
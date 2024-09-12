import random
print("These are main six players=")
players = ["kamlesh","samarth","ankush","kaple","dhale"]
print(players)
x=int(input(" if you want to add players press 1 ,for removing press -1 , if want to do both press 0, press any button if you want to do nothing\n"))
if(x==1):
     number_new=print("how many players you want to add?")
     number_new1 = int((input("")))
     print("Enter names of new players=")
     for i in range(number_new1):
         new_players = input("")
         players.append(new_players)
     print("All players playing the game=",players)
elif(x==-1):
    rem = int(input("Enter how many players you want to remove="))
    print("Enter names of players to remove=")
    for j in range(rem):
        rem_players = input("")
        players.remove(rem_players)
    print("All players playing the game=",players)
elif(x==0):
    rem = int(input("Enter how many players you want to remove="))
    print("Enter names of players to remove=")
    for j in range(rem):
        rem_players = input("")
        players.remove(rem_players)
    number_new = print("how many players you want to add?")
    number_new1 = int((input("")))
    print("Enter names of new players=")
    for i in range(number_new1):
        new_players = input("")
        players.append(new_players)
    print("All players playing the game=", players)
else:
    print("All players playing the game=",players)
t=int(input("Enter how many teams you want to form="))
k=int(input("Enter how players you want in team="))
#players[2] = players[4]
if(t==2):
    team_form1 = random.sample(players, k)
    print("1_st team=", set(team_form1))
    team_form2 = set(players) - set(team_form1)
    print("2_nd team=", set(team_form2))
elif(t==3):
    team_form1 = random.sample(players, k)
    print("1_st team=", team_form1)
    team_form2j = set(players) - set(team_form1)
    team_form2  = random.sample(list(team_form2j), k)
    print("2_nd team=", team_form2)
    team_form3 = set(players) - set(team_form1).union(set(team_form2))
    print("3_rd team-", team_form3)

else:
    print("error!")


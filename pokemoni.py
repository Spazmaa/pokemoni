import json
#2 skupiny pokemonov - 1 zlozkove a 2 zlozkove

#  I -> I
# I -> II # vynasobi
# II - > I #vybere si silnejsi utok
# II -> II # kombinacia 2 a 3

# dict in dict:
#{
#   fire:{grass:1, water:0.5,...},
#   water
#}
file = json.load(open("effectiveness.json"))
attackDict = {}
efftoNum = {"super effective":2,"normal effective":1,"not very effective":0.5,"no effect":0}

for strength in file: # iteruje strength
    for attacker in file[strength]: # iteruje typy attackerov v strength
        if attacker not in attackDict.keys(): # ak nieje attacker v nasom dict
            attackDict[attacker] = {} # urobi novy kluc nasho attackera
        for defender in file[strength][attacker]: #iteruje pre kazdeho defendera v attackeri
            attackDict[attacker][defender] = efftoNum[strength] # priradi pre kluc defendera v kluci attackera s hodnotou strengthu

def attack(p1:int,p2:int,pokemon:str)->str:
    temp = pokemon.split(",")
    team1 = temp[:p1]
    team2 = temp[p1:]
    atk1 = 0
    atk2 = 0
    for p in team1:
        types = p.split()
        for e in team2:
            enemy = e.split(" ")
            if len(types)==1:
                if len(enemy)==1:
                    atk1 += attackDict[types[0]][enemy[0]]
                    atk2 += attackDict[enemy[0]][types[0]]
                else:
                    atk1 += (attackDict[types[0]][enemy[0]]*attackDict[types[0]][enemy[1]])
                    atk2 += max(attackDict[enemy[0]][types[0]],attackDict[enemy[1]][types[0]])
            else:
                if len(enemy)==1:
                    atk1+=max(attackDict[types[0]][enemy[0]],attackDict[types[1]][enemy[0]])
                    atk2 += (attackDict[enemy[0]][types[0]]*attackDict[enemy[0]][types[1]])
                else:
                    atk1+= max(attackDict[types[0]][enemy[0]],attackDict[types[1]][enemy[0]])* max(attackDict[types[0]][enemy[1]],attackDict[types[1]][enemy[1]])
                    atk2 += max(attackDict[enemy[0]][types[0]],attackDict[enemy[1]][types[0]])*max(attackDict[enemy[1]][types[0]],attackDict[enemy[1]][types[1]])

    if atk1>atk2:
        return(str(atk1)+","+str(atk2)+",ME")
    elif atk1<atk2:
        return (str(atk1) + "," + str(atk2) + ",FOE")
    else:
        return (str(atk1) + "," + str(atk2) + ",EQUAL")

print(attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))

#print(attackDict)
#print(attackDict["Fire"]["Grass"])

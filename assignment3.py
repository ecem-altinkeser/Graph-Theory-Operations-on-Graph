import sys

smn_path = sys.argv[1]
commands_path = sys.argv[2]

f_smn = open(smn_path, "r")
smn = {}
for line in f_smn:
    key, value = line.split(":", 1)
    smn[key] = value.split()
f_smn.close()

f_commands = open(commands_path, "r")
commands = []
for line in f_commands:
    commands.append(line.strip().split())
f_commands.close()

f_output = open("output.txt", "w")
f_output.write("Welcome to Assignment 3\n"
               "-------------------------------\n")


def add_new_user(x):  # ANU
    global smn, f_output, smn
    if x[1] in smn.keys():
        f_output.write("ERROR: Wrong input type! for 'ANU'!--This user already exists!!\n")
    else:
        smn[x[1]] = []
        f_output.write("User " + "'" + str(x[1]) + "'" + " has been added to the social network successfully\n")


def delete_existing_user(x):  # DEU
    global smn, f_output
    if x[1] not in smn.keys():
        f_output.write("ERROR: Wrong input type! for 'DEU'!--There is no user named " + "'" + str(x[1]) + "'" + "!!\n")
    else:
        for i in smn.values():
            if x[1] in i:
                i.remove(x[1])
            else:
                continue
        del smn[x[1]]
        f_output.write("User " + "'" + str(x[1]) + "'" + " and his/her all relations have been deleted successfully\n")


def add_new_friend(x):  # ANF
    global smn, f_output
    if x[1] not in smn and x[2] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'ANF'!--No user named " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "'" + " found!!\n")
    elif x[1] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'ANF'!--No user named " + "'" + str(x[1]) + "'" + " found!!\n")
    elif x[2] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'ANF'!--No user named " + "'" + str(x[2]) + "'" + " found!!\n")
    elif x[1] in smn[x[2]]:
        f_output.write(
            "ERROR: A relation between " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "'" + " already exists!!\n")
    else:
        smn[x[1]].append(x[2])
        smn[x[2]].append(x[1])
        f_output.write(
            "Relation between " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "'" + " has been added successfully\n")


def delete_existing_friend(x):  # DEF
    global smn, f_output
    if x[1] not in smn and x[2] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'DEF'!--No user named " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "' " + "found!!\n")
    elif x[1] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'DEF'!--No user named " + "'" + str(x[1]) + "'" + " found!!\n")
    elif x[2] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'DEF'!--No user named " + "'" + str(x[2]) + "'" + " found!!\n")
    elif x[1] not in smn[x[2]]:
        f_output.write(
            "ERROR: No relation between " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "'" + " found!!\n")
    else:
        smn[x[1]].remove(x[2])
        smn[x[2]].remove(x[1])
        f_output.write(
            "Relation between " + "'" + str(x[1]) + "'" + " and " + "'" + str(
                x[2]) + "'" + " has been deleted successfully\n")


def count_friend(x):  # CF
    global smn, f_output
    if x[1] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'CF'!--No user named " + "'" + str(x[1]) + "'" + " found!\n")
    else:
        f_output.write(
            "User " + "'" + str(x[1]) + "'" + " has " + str(
                len(smn[x[1]])) + " friends\n")


def find_possible_friends(x):  # FPF
    global f_output, smn
    max_distance = int(x[2])
    if x[1] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'FPF'!--No user named " + "'" + str(x[1]) + "'" + " found!\n")
    elif max_distance < 1 or max_distance > 3:
        f_output.write(
            "ERROR: Maximum distance is out of range!!\n")
    elif max_distance == 1:
        count = len(smn[x[1]])
        f_output.write(
            "User " + "'" + str(x[1]) + "'" + " has " + str(count) + " possible friends when maximum distance is " +
            str(max_distance) + "\nThese possible friends: {" + str(smn[x[1]])[1:-1] + "}\n")
    elif max_distance == 2:
        friends = set(smn[x[1]])
        for i in smn[x[1]]:
            friends.update(smn[i])
        friends = sorted(friends)
        friends.remove(x[1])
        count = len(friends)
        f_output.write(
            "User " + "'" + str(x[1]) + "'" + " has " + str(count) + " possible friends when maximum distance is " +
            str(max_distance) + "\nThese possible friends: {" + str(friends)[1:-1] + "}\n")
    elif max_distance == 3:
        friends = set(smn[x[1]])
        for i in smn[x[1]]:
            friends.update(smn[i])
        for i in smn[x[1]]:
            for j in smn[i]:
                friends.update(smn[j])
        friends = sorted(friends)
        friends.remove(x[1])
        count = len(friends)
        f_output.write(
            "User " + "'" + str(x[1]) + "'" + " has " + str(count) + " possible friends when maximum distance is " +
            str(max_distance) + "\nThese possible friends: {" + str(friends)[1:-1] + "}\n")


def suggest_friend(x):  # Sf
    global smn, f_output
    mutuality_degree = int(x[2])
    friend_dict = {}
    if x[1] not in smn:
        f_output.write(
            "ERROR: Wrong input type! for 'SF'!--No user named " + "'" + str(x[1]) + "'" + " found!\n")
    elif mutuality_degree <= 1 or mutuality_degree > len(smn[x[1]]):
        f_output.write(
            "Error: Mutuality Degree cannot be less than 1 or greater than " + str(len(smn[x[1]])) + "\n")
    elif mutuality_degree > 3:
        f_output.write(
            "Error: Mutuality Degree cannot be less than 1 or greater than 4\n")
    else:
        f_output.write(
            "Suggestion List for " + "'" + str(x[1]) + "'" + " (when MD is " + str(mutuality_degree) + "):\n")
        friends = []
        for user in smn.keys():
            count = 0
            for friend in smn[x[1]]:
                if user in smn[friend]:
                    count += 1
            if user == x[1]:
                continue
            elif count >= mutuality_degree:
                friends.append(user)
                friend_dict[user] = count
        if x[1] in friends:
            friends.remove(x[1])
        if x[1] in friend_dict:
            friend_dict.pop(x[1])
        friend_dict = {k: v for k, v in sorted(friend_dict.items(), key=lambda item: item[1])}
        for i in friend_dict:
            f_output.write(
                "'" + str(x[1]) + "' has " + str(friend_dict[i]) + " mutual friends with " + "'" + str(i) + "'\n")
        friends = sorted(friends)
        f_output.write("The suggested friends for " + "'" + str(x[1]) + "': " + str(friends)[1:-1] + "\n")


def main():
    global commands
    for i in commands:
        if i[0] == "ANU":
            add_new_user(i)
        elif i[0] == "DEU":
            delete_existing_user(i)
        elif i[0] == "ANF":
            add_new_friend(i)
        elif i[0] == "DEF":
            delete_existing_friend(i)
        elif i[0] == "CF":
            count_friend(i)
        elif i[0] == "FPF":
            find_possible_friends(i)
        elif i[0] == "SF":
            suggest_friend(i)


main()
f_output.close()

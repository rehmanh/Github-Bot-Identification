import pandas as pd
import re

if __name__ == "__main__":
    data = pd.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/experiments-data-output/8_disable_window_size.csv")

    user_list = []

    users = data['bot_name'].unique()
    print("Total unique users without removing NamedUser: {}".format(len(users)))
    for user in users:
        if user.startswith("NamedUser"):
            match = re.findall('"([^"]*)"', user)
            user_list.append(match[0])
        else:
            user_list.append(user)
    print("Total unique users with removing NamedUser: {}".format(len(user_list)))
    print("Total unique users after filtering dupes: {}".format(len(set(user_list))))
    set_a = set(user_list)
    print(set_a)


    # compare with original data
    original_data = pd.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Github-Bot-Identification/data/results/bot_identification_MS200_Habib.csv")

    original_user_list = []
    original_users = original_data['bot_name'].unique()
    print("Total unique users without removing NamedUser: {}".format(len(original_users)))
    for user in original_users:
        if user.startswith("NamedUser"):
            match = re.findall('"([^"]*)"', user)
            original_user_list.append(match[0])
        else:
            original_user_list.append(user)
    print("Total unique users with removing NamedUser: {}".format(len(original_user_list)))
    print("Total unique users after filtering dupes: {}".format(len(set(original_user_list))))
    set_b = set(original_user_list)
    #print(set_b)

    print(set_a.difference(set_b))
    print(len(set_a.difference(set_b)))
    print("\n")
    print(set_b.difference(set_a))
    print(len(set_b.difference(set_a)))
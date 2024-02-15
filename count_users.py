import pandas as pd
import re

if __name__ == "__main__":
    data = pd.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv")

    user_list = []

    users = data['user'].unique()
    for user in users:
        if user.startswith("NamedUser"):
            match = re.findall('"([^"]*)"', user)
            user_list.append(match[0])
        else:
            user_list.append(user)
    print(len(user_list))
    print(len(set(user_list)))
import pandas as panda

def add_pr_link_to_row(rows):
    for index, row in rows.iterrows():
        link = "https://github.com/" + row["repo_name"] + "/pull/" + str(row["pull_number"])
        rows.at[index, 'PR_Link'] = link
    return rows

if __name__ == '__main__':
    data = panda.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv")
    data['PR_Link'] = ''

    # get all the non-bot, zero PRs
    data = data.query('Bot == 0', inplace=False)

    # group the data by repo name and pull number
    data = data.groupby(['repo_name', 'pull_number'], as_index=False).first()
    data = panda.DataFrame(data)
    data.head()

    # initialize result DataFrame
    result = panda.DataFrame(columns=data.columns)

    # get the unique repository names available
    repo_names = data['repo_name'].unique()
    
    for repo in repo_names:
        rows = data.loc[data['repo_name'] == repo]
        # if there are more than 10 unique 
        # repos, then sample 10 of them
        # otherwise sample all of them
        if len(rows) >= 10:
            sample = rows.sample(10)
        else:
            sample = rows.sample(len(rows))
        
        sample = add_pr_link_to_row(sample)
        result = result._append(sample)

    result = result.groupby(['repo_name'], as_index=False).count()
    result.to_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/200_Repos_Stats.csv", index=False)
    #result.to_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/200_Repos_Sampled.csv", index=False)


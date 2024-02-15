import pandas as pd
import re

quality_bots_ms = [
    "dependabot",
    "check-spelling-bot",
    "renovate",
    "review-notebook-app",
    "codecov-commenter",
    "fabricteam",
    "size-auditor",
    "github-code-scanning",
    "coveralls",
    "CBL-Mariner-Bot",
    "sonarcloud",
    "codecov",
    "acrolinxatmsft1",
    "changeset-bot",
    "Megalinter"
]

quality_bots_apache = [
    # "dependabot",
    "github-code-scanning",
    "lgtm-com",
    "sonarcloud",
    "step-security-bot",
    "ursabot",
    "sonatype-lift"
]

if __name__ == '__main__':
    raw_data = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv', index_col=False)
    raw_data = pd.DataFrame(raw_data)

    num_qf_activities = 0


    for index, row in raw_data.iterrows():
        user = row['user']
        
        if user.startswith("NamedUser"):
            user = re.findall('"([^"]*)"', user)
            user = user[0]
        
        if user.endswith('[bot]'):
            user = user.removesuffix('[bot]')

        if user in quality_bots_ms:
            num_qf_activities += 1

    print('Number of Quality Facilitating Activities Apache: {}'.format(num_qf_activities))
    
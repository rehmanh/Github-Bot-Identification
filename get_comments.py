import pandas as pd
import re

# we have a list of all the bots that are in the PRs
confirmed_bots = [
    "VSCodeTriageBot",
    "dependabot",
    "github-actions",
    "check-spelling-bot",
    "azure-pipelines",
    "microsoft-github-policy-service",
    "typescript-bot",
    "github-pages",
    "kodiakhq",
    "renovate",
    "bors",
    "microsoft-cla-retired",
    "msftbot",
    "facebook-github-bot",
    "review-notebook-app",
    "codecov-commenter",
    "codesandbox-ci",
    "msft-fluent-ui-bot",
    "fabricteam",
    "size-auditor",
    "github-code-scanning",
    "github-merge-queue",
    "pull",
    "PylanceBot",
    "coveralls",
    "llvmbot",
    "wingetbot",
    "apecloud-bot",
    "dotnet-winget-bot",
    "Rust-Winget-Bot",
    "dotnet-maestro",
    "msfluid-bot",
    "CBL-Mariner-Bot",
    "reunion-maestro",
    "pull-bot",
    "analysis-bot",
    "AppVeyorBot",
    "sonarcloud",
    "codecov",
    "BrewTestBot",
    "acrolinxatmsft1",
    "changeset-bot",
    "msftclas",
    "playwrightmachine",
    "PrismAutomata",
    "Megalinter",
    "FluentService",
    "MetalMonkey-GSD",
    "csigs"
]

apache_bots = [
    "dependabot",
    "github-code-scanning",
    "lgtm-com",
    "sonarcloud",
    "step-security-bot",
    "ursabot",
    "sonartype-lift",
    "acs-robot",
    "mxnet-bot",
    "hudi-bot",
    "CarbonDataQA2",
    "flinkbot",
    "netlify",
    "blueorangutan",
    "Apache-HBase",
    "tez-yetus",
    "codecov",
    "codecov-commenter",
    "coveralls",
    "helix-bot",
    "bot-gradle",
    "github-actions",
    "stale",
    "boring-cyborg",
    "echarts-bot",
    "request-info",
    "check-spelling-bot",
    "superset-github-bot",
    "pull-request-size"
]


if __name__ == '__main__':
    # get all the raw data into a DataFrame
    # df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv', index_col=False)
    df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_ap_fixed.csv', index_col=False)
    
    prs = df.groupby(['repo_name', 'pull_number'], as_index=False).first()
    prs = pd.DataFrame(prs)

    result = pd.DataFrame(columns=['Repo Name', 'Pull Number', 'Bot Present?', 'Comment Count'])

    for index, row in prs.iterrows():   
        repo_name = row['repo_name']
        pull_number = row['pull_number']
        bot_present = False

        #user = row['user']

        sample = df.query("repo_name == @repo_name & pull_number == @pull_number", inplace=False)
        sample = pd.DataFrame(sample)

        user_list = sample['user'].tolist()
        for user in user_list:
            if user.startswith("NamedUser"):
                user = re.findall('"([^"]*)"', user)
                user = user[0]
            
            if user.endswith('[bot]'):
                user = user.removesuffix('[bot]')
        
            if user in apache_bots:
                # bot is present
                bot_present = True
            
        comments = sample.query("activity_body == \"0\"", inplace=False)
        comment_quantity = len(comments)
                
        new_row = {'Repo Name': repo_name, 'Pull Number': pull_number, 'Bot Present?': bot_present, 'Comment Count': comment_quantity}
        result.loc[len(result)] = new_row
            
    result.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Comments_Apache.csv', index=False)


    
    
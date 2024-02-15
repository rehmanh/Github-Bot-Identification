import pandas as pd
import re

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
    bots = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/RQ4_fix_bot_apache.csv', index_col=False)
    
    raw = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_ap_fixed.csv', index_col=False)
    raw = pd.DataFrame(raw)

    # initialize result Dataframe
    result = pd.DataFrame(columns=['Repo Name', 'Pull Number', 'Bot Activity Rate'])

    for index, row in bots.iterrows():
        repo_name = row['Repo Name']
        pull_number = row['Pull Number']

        sample = raw.query("repo_name == @repo_name & pull_number == @pull_number", inplace=False)
        sample = pd.DataFrame(sample)

        num_total_activities = len(sample)
        num_bot_activities = 0

        users = sample['user'].tolist()
        for u in users:
            if u.startswith("NamedUser"):
                user = re.findall('"([^"]*)"', u)
                u = user[0]

            if u.endswith('[bot]'):
                u = u.removesuffix('[bot]')

            if u in apache_bots:
                num_bot_activities += 1

        bot_activity_rate = num_bot_activities / num_total_activities

        new_row = {'Repo Name': repo_name, 'Pull Number': pull_number, 'Bot Activity Rate': bot_activity_rate}
        result.loc[len(result)] = new_row
    
    result.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/APACHE_RQ4WithBotsActivityRates_Fixed.csv', index=False)
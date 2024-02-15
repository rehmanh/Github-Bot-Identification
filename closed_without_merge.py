import pandas as pd
import re

confirmed_bots_ms = [
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

confirmed_bots_apache = [
    "dependabot",
    "github-code-scanning",
    "lgtm-com",
    "sonarcloud",
    "step-security-bot",
    "ursabot",
    "sonatype-lift",
    "acs-robot",
    "mxnet-bot",
    "hudi-bot",
    "carbondataqa2",
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
    "echarts",
    "request-info",
    "check-spelling-bot",
    "superset-github-bot",
    "pull-request-size"
]

if __name__ == '__main__':
    # get all the raw data into a DataFrame
    df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_ap_fixed.csv', index_col=False)

    # sort by Repo Name and PR number; should be 35,070 unique Pulls
    prs = df.groupby(['repo_name', 'pull_number'], as_index=False).first()
    prs = pd.DataFrame(prs)

    closed_without_merge = 0
    closed_by_bot = 0
    closed_by_dev = 0

    for index, row in prs.iterrows():
        repo_name = row['repo_name']
        pull_number = row['pull_number']

        sample = df.query("repo_name == @repo_name & pull_number == @pull_number", inplace=False)
        sample = pd.DataFrame(sample)

        activity_bodies = sample['activity_body'].tolist()
        # pr was closed
        if 'closed' in activity_bodies:
            # check if it's not merged
            if 'merged' not in activity_bodies:
                closed_without_merge += 1

                i = activity_bodies.index('closed')
                user = sample.iloc[i]['user']
                if user.startswith("NamedUser"):
                    user = re.findall('"([^"]*)"', user)
                    user = user[0]
                
                if user.endswith('[bot]'):
                    user = user.removesuffix('[bot]')
            
                if user.lower() in confirmed_bots_apache:
                    closed_by_bot += 1
                else:
                    closed_by_dev += 1

    print("Total number of closed PRs without being merged: {}. {} were closed by devs, {} were closed by bots".format(closed_without_merge, closed_by_dev, closed_by_bot))
    
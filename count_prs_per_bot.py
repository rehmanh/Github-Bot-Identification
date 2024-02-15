import pandas as pd

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
    "pull[bot]",
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

if __name__ == '__main__':
    # get all the raw data into a DataFrame
    df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv', index_col=False)
    prs = pd.DataFrame(df)

    for bot in confirmed_bots:
        sample = prs[prs['user'].str.contains(bot)]
        sample = sample.groupby(['repo_name', 'pull_number'], as_index=False)
        print("{}: with total number of PRs: {}".format(bot, len(sample)))




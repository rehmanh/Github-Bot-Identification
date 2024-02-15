import pandas as pd
import matplotlib.pyplot as plt
import re
# list of confirmed 50 bots
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
df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv')
# Filter out Dependabot
# df = df[df['user'] != 'dependabot']
result = pd.DataFrame(df)

num_bot_activities = 0

for index, row in df.iterrows():
    user = row['user']
    if user.startswith("NamedUser"):
        user = re.findall('"([^"]*)"', user)
        user = user[0]
    
    if user.endswith('[bot]'):
        user = user.removesuffix('[bot]')

    if user in confirmed_bots:
        num_bot_activities += 1
    # if row['user'].startswith("NamedUser"):
    #     user = re.findall('"([^"]*)"', row['user'])
    #     user = user[0]
    
    # if user in confirmed_bots:
    #     result = result._append(row)
print(num_bot_activities)
# #projects_with_bot = df[df['Bot'].isin([2])]['repo_name'].nunique()
# projects_with_bot = result['repo_name'].nunique()
# print('number of projects with bot =', projects_with_bot)
# #print('length total project with bot:',projects_with_bot)
# PAR = (projects_with_bot / 180) * 100
# print('PAR rate:',PAR)
# # Calculate the total number of unique PRs
# total_prs =  35070 #df['pull_number'].nunique()
# # total number of PRs involve bots
# #total_prs_with_bot = df[df['Bot'].isin([2])]['pull_number'].nunique()
# total_prs_with_bot = result['pull_number'].nunique()
# # Display the results
# print('Total number of PRs involving bots:', total_prs_with_bot)
# percentage_prs_with_bot = (total_prs_with_bot / total_prs) * 100
# print('Percentage of PRs involving bots:', percentage_prs_with_bot)
# #total number of PRs for each project
# total_prs_each_project = df.groupby('repo_name')['pull_number'].nunique()
# #print(total_prs_each_project)
# # Number of PRs involving a bot for each project
# #number_prs_with_bot_each_project = df[df['Bot'].isin([2])].groupby('repo_name')['pull_number'].nunique()
# number_prs_with_bot_each_project = result.groupby('repo_name')['pull_number'].nunique()
# #print(prs_with_bot)
# # Calculate the Involvement Rate (IR) for each project
# IR = (number_prs_with_bot_each_project / total_prs_each_project).fillna(0) * 100
# # Print the Involvement Rate (IR) for each project
# #IR = IR.dropna()
# print('IR rate, total number of PRs involving a bot for each project:',IR)
# # Create a DataFrame to hold the results
# result_df = pd.DataFrame({'repo_name': IR.index, 'Involvement_Rate': IR.values})
# # Save the results to a CSV file
# result_df.to_csv('involvement_rate.csv', index=False)
# # Display the contents of the DataFrame (optional)
# print(result_df)
# # Calculate the total number of activities per PR
# total_activities_pr = df.groupby('repo_name')['pull_number'].count()
# print('total_activities_pr', total_activities_pr)
# # Calculate the number of activities taken by a bot per PR
# #bot_activities_pr = df[df['Bot'].isin([2])].groupby('pull_number').size()
# bot_activities_pr = result.groupby('repo_name')['pull_number'].size()
# # Calculate the Activity Rate per PR (ARPR) for each PR
# ARPR = (bot_activities_pr / total_activities_pr).fillna(0) * 100
# ARPR = ARPR.round(2)
# #ARPR = ARPR.dropna()
# print("ARPR IS:")
# print(ARPR)
# # Convert the Series to a DataFrame
# ARPR_df = ARPR.reset_index()
# # Rename the columns for clarity
# ARPR_df.columns = ['pull_number', 'ARPR']
# # Write the DataFrame to a CSV file
# ARPR_df.to_csv('ARPR_results.csv', index=False)
# sorted_IR = IR.sort_values(ascending=False)
# # Calculate the number of projects reaching each threshold
# thresholds = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 0]
# y_values = [len(sorted_IR[sorted_IR > threshold]) for threshold in thresholds]
# # Create the line diagram
# plt.plot(thresholds, y_values, marker='o')
# plt.xlabel('PR Involvement Rate (IR)')
# plt.ylabel('# of Projects')
# plt.title('Distribution of IRPi over Projects')
# plt.gca().invert_xaxis()  # Reverse the x-axis
# plt.xticks(thresholds, ['>90%', '>80%', '>70%', '>60%', '>50%', '>40%', '>30%', '>20%', '>10%', '>5%', '>0%'])
# plt.yticks(y_values)
# plt.grid(False)
# for i,j in zip(thresholds,y_values):
#     plt.annotate(str(int(j)),xy=(i+3,j+3))
# plt.show()
# # Sort the ARPR values from high to low
# sorted_ARPR = ARPR.sort_values(ascending=False)
# # Set the thresholds for the x-axis
# thresholds = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5]
# # Calculate the percentage of PRs above each threshold
# y_values_ARPR = [len(sorted_ARPR[sorted_ARPR > threshold]) / len(sorted_ARPR) * 100 for threshold in thresholds]
# # Create the line diagram
# # plt.plot(sorted_ARPR.values, range(1, len(sorted_ARPR) + 1))
# plt.plot(thresholds,y_values_ARPR,marker='o')
# plt.xlabel('ARP R')
# plt.ylabel('Percentage of PRs')
# plt.title('Bot Activity Rate Distribution Overall All PRs')
# plt.gca().invert_xaxis()
# plt.xticks(thresholds, ['>90%', '>80%', '>70%', '>60%', '>50%', '>40%', '>30%', '>20%', '>10%', '>5%'])
# plt.yticks([])  # Remove y-axis ticks
# plt.grid(False)
# for i,j in zip(thresholds,y_values_ARPR):
#     plt.annotate(str(int(j))+'%',xy=(i+2,j+2))
# plt.show()
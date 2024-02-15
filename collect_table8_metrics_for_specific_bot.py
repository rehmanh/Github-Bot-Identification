import pandas as pd
from scipy.stats import mannwhitneyu, pearsonr, spearmanr, norm, kstest, ks_2samp, kendalltau
import numpy as np
import re

from typing import List

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

def collect_activity_rates_for_bot(bot: str) -> pd.DataFrame:
    raw_data = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv', index_col=False)
    raw_data = pd.DataFrame(raw_data)

    prs = raw_data.groupby(['repo_name', 'pull_number'], as_index=False).first()
    prs = pd.DataFrame(prs)

    # initialize result Dataframe
    result = pd.DataFrame(columns=['Repo Name', 'Pull Number', 'Bot Activity Rate', 'Bot Name'])

    for index, row in prs.iterrows():
        repo_name = row['repo_name']
        pull_number = row['pull_number']

        pull_request = raw_data.query("repo_name == @repo_name & pull_number == @pull_number", inplace=False)
        pull_request = pd.DataFrame(pull_request)

        num_total_activities = len(pull_request)
        num_bot_activities = 0

        users = pull_request['user'].tolist()
        for u in users:
            if u.startswith("NamedUser"):
                user = re.findall('"([^"]*)"', u)
                u = user[0]
            
            if u.endswith('[bot]'):
                u = u.removesuffix('[bot]')

            if bot in u:
                num_bot_activities += 1

        bot_activity_rate = num_bot_activities / num_total_activities

        if bot_activity_rate > 0:
            new_row = { 'Repo Name': repo_name, 'Pull Number': pull_number, 'Bot Activity Rate': bot_activity_rate, 'Bot Name': bot }
            result.loc[len(result)] = new_row
    
    return pd.DataFrame(result)

def determine_normality_for_bot_activities(activity_rates: List[float]) -> bool:
    stat, p_value = kstest(activity_rates, 'norm')
    print('KS-Test For Activity Rates: {}. Statistic Value: {}'.format(p_value, stat))
    return p_value > 0.05
        
def collect_metrics_for_bot(bot_activities: pd.DataFrame, activity_rates: List[float]) -> None:
    raw_metrics_for_all_bots = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/RQ4WithBots_F.csv', index_col=False)
    raw_metrics_for_all_bots = pd.DataFrame(raw_metrics_for_all_bots)

    comments_for_all_bots = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Comments_WithBots_F.csv', index_col=False)
    comments_for_all_bots = pd.DataFrame(comments_for_all_bots)

    tt = [] # turnaround time
    mt = [] # merge time
    it = [] # idle time
    ch = [] # churn
    dq = [] # developer quantity
    cq = [] # comment quantity DEVELOPERS!

    for index, row in bot_activites.iterrows():
        repo_name = row['Repo Name']
        pull_number = row['Pull Number']

        sample = raw_metrics_for_all_bots.query("`Repo Name` == @repo_name & `Pull Number` == @pull_number", inplace=False)

        comments = comments_for_all_bots.query("`Repo Name` == @repo_name & `Pull Number` == @pull_number", inplace=False)
        
        # if there is already PRs with that specific Bot's activities, we compile the metrics
        if len(sample) > 0:
            tt.extend(sample['Turnaround Time'].tolist())
            mt.extend(sample['Merge Time'].tolist())
            it.extend(sample['Idle Time'].tolist())
            ch.extend(sample['Churn'].tolist())
            dq.extend(sample['Developer Quantity'].tolist())
        
        if len(comments) > 0:
            cq.extend(comments['Comment Count'].tolist())
    
    # format according to the correct Data format required for statistics
    tt = [(int(re.findall('(\d+)[^\d]days', t)[0]) * 86400) + ( list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[0] * 3600 + list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[1] * 60 + list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[2] ) for t in tt]
    
    mt = [t for t in mt if t != '0']
    mt = [(int(re.findall('(\d+)[^\d]days', t)[0]) * 86400) + ( list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[0] * 3600 + list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[1] * 60 + list(map(int, re.findall('days(,?.*)', t)[0].strip().split(':')))[2] ) for t in mt]

    it = [t for t in it if t != '0']
    for i, t in enumerate(it):
        if ',' in t:
            it[i] = t.replace(',', '')
    for i, t in enumerate(it):
        if 'day' in t and 'days' not in t:
            it[i] = t.replace('day', 'days')
    for i, t in enumerate(it):
        if 'days' not in t:
            it[i] = '0 days ' + t
    it = [(int(re.findall('(\d+)[^\d]days', t)[0]) * 86400) + ( list(map(float, re.findall('days(,?.*)', t)[0].strip().split(':')))[0] * 3600 + list(map(float, re.findall('days(,?.*)', t)[0].strip().split(':')))[1] * 60 + list(map(float, re.findall('days(,?.*)', t)[0].strip().split(':')))[2] ) for t in it]

    
    # tt tests
    ar = activity_rates
    if len(activity_rates) > len(tt):
        ar = activity_rates[0:len(tt)]
    else:
        tt = tt[0:len(ar)]

    spear, _ = spearmanr(ar, tt)
    # kend, _ = kendalltau(ar, tt)
    print('Spearman Correlation for Turnaround Time: %.3f' % spear)
    # print('Kendalls Tau for Turaround Time: %.3f' % kend)
    print('\n')

    # mt tests
    ar = activity_rates
    if len(activity_rates) > len(mt):
        ar = activity_rates[0:len(mt)]
    else:
        mt = mt[0:len(ar)]

    spear, _ = spearmanr(ar, mt)
    # kend, _ = kendalltau(ar, mt)
    print('Spearman Correlation for Merge Time: %.3f' % spear)
    # print('Kendalls Tau for Merge Time: %.3f' % kend)
    print('\n')

    # it tests
    ar = activity_rates
    if len(activity_rates) > len(it):
        ar = activity_rates[0:len(it)]
    else:
        it = it[0:len(ar)]

    spear, _ = spearmanr(ar, it)
    # kend, _ = kendalltau(ar, it)
    print('Spearman Correlation for Idle Time: %.3f' % spear)
    # print('Kendalls Tau for Idle Time: %.3f' % kend)
    print('\n')

    # churn tests
    ar = activity_rates
    if len(activity_rates) > len(ch):
        ar = activity_rates[0:len(ch)]
    else:
        ch = ch[0:len(ar)]

    spear, _ = spearmanr(ar, ch)
    # kend, _ = kendalltau(ar, ch)
    print('Spearman Correlation for Churn: %.3f' % spear)
    # print('Kendalls Tau for Churn: %.3f' % kend)
    print('\n')

    # dq tests
    ar = activity_rates
    if len(activity_rates) > len(dq):
        ar = activity_rates[0:len(dq)]
    else:
        dq = dq[0:len(ar)]

    spear, _ = spearmanr(ar, dq)
    # kend, _ = kendalltau(ar, dq)
    print('Spearman Correlation for Developer Quantity: %.3f' % spear)
    # print('Kendalls Tau for Developer Quantity: %.3f' % kend)
    print('\n')

    # comment quant. tests
    ar = activity_rates
    if len(activity_rates) > len(cq):
        ar = activity_rates[0:len(cq)]
    else:
        cq = cq[0:len(ar)]

    spear, _ = spearmanr(ar, cq)
    # kend, _ = kendalltau(ar, cq)
    print('Spearman Correlation for Comment Quantity: %.3f' % spear)
    # print('Kendalls Tau for Comment Quantity: %.3f' % kend)
    print('\n')
    

if __name__ == '__main__':
    bot_activites = collect_activity_rates_for_bot('Megalinter')
    activity_rates = bot_activites['Bot Activity Rate'].tolist()
    
    # normal = determine_normality_for_bot_activities(activity_rates)

    collect_metrics_for_bot(bot_activites, activity_rates)

    # if not normal:
    #     collect_metrics_for_bot(bot_activites, activity_rates)
    # else:
    #     print('Dataset is normally distributed, but this feature is not ready yet!')

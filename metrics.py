import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/collected_data_one_year_microsoft_May1st-3_fixed.csv")

    pr_per_repos = df.groupby('repo_name')['pull_number'].nunique(dropna=False)
    activity_per_pr = df.groupby("repo_name")["event_time"].count()
    activity_per_pr = pd.DataFrame(activity_per_pr)
    activity_per_pr = activity_per_pr.rename(columns={"event_time":"activity_count"})
    activity_per_pr.head()

    # metrics for PR Quantity per Repo
    min_PR_per_repo = pr_per_repos.min()
    max_PR_per_repo = pr_per_repos.max()
    mean_PR_per_repo = pr_per_repos.mean()
    mode_PR_per_repo = pr_per_repos.mode()
    total_PR = pr_per_repos.sum()

    min_activity_per_pr = activity_per_pr.min()
    max_activity_per_pr = activity_per_pr.max()
    mean_activity_per_repo = activity_per_pr.mean()
    mode_activity_per_repo = activity_per_pr.mode()
    total_activity = activity_per_pr.sum()

    print("""Min PR Per Repo: {}\n
    Max PR Per Repo: {}\n
    Mean PR Per Repo: {}\n
    Mode PR Per Repo: {}\n
    Total PR Per Repo: {}\n
    Min Activity Per PR: {}\n
    Max Activity Per PR: {}\n
    Mean Activity Per PR: {}\n
    Mode Activity Per PR: {}\n
    Total Activity Per PR: {}""".format(min_PR_per_repo, max_PR_per_repo, 
                                        mean_PR_per_repo, mode_PR_per_repo, 
                                        total_PR, min_activity_per_pr, max_activity_per_pr, 
                                        mean_activity_per_repo, mode_activity_per_repo, total_activity))
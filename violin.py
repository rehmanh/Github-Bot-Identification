import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

tt = [
    -0.035,
    -0.047,
    0.024,
    0.321,
    0.122,
    -0.529,
    0.096,
    -0.044,
    0.209,
    0.151,
    0.205,
    0.866,
    0.307,
    0.35,
    0.205,
    0.001,
    0.191,
    -0.047,
    0.304,
    0.447,
    0.218,
    0.071,
    -0.069,
    0.138,
    0.033,
    0.09,
    0.646,
    0.02,
    -0.019,
    0.014,
    0.43,
    0.111,
    -0.062,
    -0.162,
    0.174,
    -0.047,
    -0.272,
    0.418,
    0.062
]
mt = [
    0.15,
    -0.006,
    0.063,
    0.009,
    -0.032,
    -0.208,
    -0.064,
    0.009,
    -0.118,
    -0.042,
    -0.872,
    -0.866,
    0.042,
    0.019,
    0.1,
    0.006,
    -0.105,
    0.013,
    0.123,
    0,
    -0.327,
    -0.474,
    0.036,
    1,
    0.233,
    0.026,
    -0.651,
    0.071,
    0.074,
    -0.472,
    -0.064,
    -0.013,
    0.052,
    -0.718,
    -0.045,
    0.125,
    -0.016,
    -0.03,
    -0.487
]
it = [
    0.2,
    -0.152,
    -0.124,
    -0.262,
    -0.153,
    -0.023,
    -0.289,
    -0.069,
    -0.174,
    -0.272,
    0.872,
    0.866,
    0.107,
    0.365,
    0.3,
    -0.076,
    -0.143,
    -0.021,
    0.126,
    0.5,
    0.206,
    -0.218,
    -0.237,
    0.18,
    -0.277,
    0.365,
    -0.792,
    -0.089,
    0.33,
    -0.309,
    0.172,
    -0.145,
    -0.162,
    -0.765,
    -0.148,
    -0.518,
    -0.123,
    0.123,
    0.068
]
ch = [
    -0.149,
    -0.098,
    0.013,
    0.301,
    -0.009,
    -0.054,
    -0.056,
    0.09,
    0.072,
    -0.053,
    0.359,
    0.866,
    -0.042,
    -0.137,
    -0.3,
    0.084,
    -0.17,
    -0.118,
    0.01,
    0.354,
    0.035,
    -0.419,
    0.063,
    -0.004,
    -0.037,
    -0.055,
    -0.027,
    0.116,
    -0.107,
    0.026,
    -0.137,
    -0.112,
    -0.102,
    0.483,
    -0.086,
    -0.094,
    0.014,
    -0.111,
    -0.226
]
dq = [
    0.194,
    -0.891,
    -0.662,
    -0.005,
    -0.557,
    -0.955,
    -0.376,
    -0.877,
    -0.832,
    0.153,
    -1,
    -1,
    -0.981,
    -0.847,
    -0.975,
    -0.391,
    -0.596,
    -0.115,
    -0.958,
    0.41,
    -0.381,
    -0.51,
    -0.744,
    -0.859,
    -0.964,
    -0.887,
    -0.917,
    -0.597,
    -0.641,
    -0.993,
    -0.75,
    -0.452,
    -0.892,
    -0.997,
    -0.85,
    -0.599,
    -0.893,
    -0.748,
    -0.045
]
cq = [
    -0.186,
    -0.583,
    -0.375,
    0.374,
    -0.36,
    -0.692,
    -0.404,
    0.463,
    0.37,
    0.39,
    -0.918,
    -1,
    -0.718,
    -0.595,
    -0.671,
    0.048,
    -0.346,
    -0.05,
    0.22,
    0.564,
    -0.446,
    -0.445,
    -0.347,
    -0.457,
    -0.298,
    -0.211,
    -0.572,
    -0.203,
    0.027,
    -0.676,
    -0.702,
    0.378,
    -0.577,
    -0.782,
    -0.585,
    -0.309,
    -0.652,
    -0.653,
    0.195
]

bm = [
    -0.035,
    -0.047,
    0.024,
    0.321,
    0.15,
    -0.006,
    0.063,
    0.009,
    0.2,
    -0.152,
    -0.124,
    -0.262,
    -0.149,
    -0.098,
    0.013,
    0.301,
    0.194,
    -0.891,
    -0.662,
    -0.005,
    -0.186,
    -0.583,
    -0.375,
    0.374
]
gf = [
    0.122,
    -0.529,
    -0.032,
    -0.208,
    -0.153,
    -0.023,
    -0.009,
    -0.054,
    -0.557,
    -0.955,
    -0.36,
    -0.692
]
pr = [
    0.096,
    -0.044,
    0.209,
    0.151,
    0.205,
    0.866,
    0.307,
    0.35,
    0.205,
    0.001,
    0.191,
    -0.047,
    0.304,
    0.447,
    0.218,
    0.071,
    -0.069,
    0.138,
    0.033,
    0.09,
    0.646,
    -0.064,
    0.009,
    -0.118,
    -0.042,
    -0.872,
    -0.866,
    0.042,
    0.019,
    0.1,
    0.006,
    -0.105,
    0.013,
    0.123,
    0,
    -0.327,
    -0.474,
    0.036,
    1,
    0.233,
    0.026,
    -0.651,
    -0.289,
    -0.069,
    -0.174,
    -0.272,
    0.872,
    0.866,
    0.107,
    0.365,
    0.3,
    -0.076,
    -0.143,
    -0.021,
    0.126,
    0.5,
    0.206,
    -0.218,
    -0.237,
    0.18,
    -0.277,
    0.365,
    -0.792,
    -0.056,
    0.09,
    0.072,
    -0.053,
    0.359,
    0.866,
    -0.042,
    -0.137,
    -0.3,
    0.084,
    -0.17,
    -0.118,
    0.01,
    0.354,
    0.035,
    -0.419,
    0.063,
    -0.004,
    -0.037,
    -0.055,
    -0.027,
    -0.376,
    -0.877,
    -0.832,
    0.153,
    -1,
    -1,
    -0.981,
    -0.847,
    -0.975,
    -0.391,
    -0.596,
    -0.115,
    -0.958,
    0.41,
    -0.381,
    -0.51,
    -0.744,
    -0.859,
    -0.964,
    -0.887,
    -0.917,
    -0.404,
    0.463,
    0.37,0.39,
    -0.918,
    -1,
    -0.718,
    -0.595,
    -0.671,
    0.048,
    -0.346,
    -0.05,
    0.22,
    0.564,
    -0.446,
    -0.445,
    -0.347,
    -0.457,
    -0.298,
    -0.211,
    -0.572
]
qf = [
    0.02,
    -0.019,
    0.014,
    0.43,
    0.111,
    -0.062,
    -0.162,
    0.174,
    -0.047,
    -0.272,
    0.418,
    0.062,
    0.071,
    0.074,
    -0.472,
    -0.064,
    -0.013,
    0.052,
    -0.718,
    -0.045,
    0.125,
    -0.016,
    -0.03,
    -0.487,
    -0.089,
    0.33,
    -0.309,
    0.172,
    -0.145,
    -0.162,
    -0.765,
    -0.148,
    -0.518,
    -0.123,
    0.123,
    0.068,
    0.116,
    -0.107,
    0.026,
    -0.137,
    -0.112,
    -0.102,
    0.483,
    -0.086,
    -0.094,
    0.014,
    -0.111,
    -0.226,
    -0.597,
    -0.641,
    -0.993,
    -0.75,
    -0.452,
    -0.892,
    -0.997,
    -0.85,
    -0.599,
    -0.893,
    -0.748,
    -0.045,
    -0.597,
    -0.641,
    -0.993,
    -0.75,
    -0.452,
    -0.892,
    -0.997,
    -0.85,
    -0.599,
    -0.893,
    -0.748,
    -0.045
]


ttfbm = [
    -0.035,
    -0.047,
    0.024,
    0.321
]
mtfbm = [
    0.15,
    -0.006,
    0.063,
    0.009
]
itfb = [
    0.2,
    -0.152,
    -0.124,
    -0.262
]
chfbm = [
    -0.149,
    -0.098,
    0.013,
    0.301
]
dqfbm = [
    0.194,
    -0.891,
    -0.662,
    -0.005
]
cqfbm = [
    -0.186,
    -0.583,
    -0.375,
    0.374
]

ttfgf = [
    0.122,
    -0.529
]
mtfgf = [
    -0.032,
    -0.208
]
itfgf = [
    -0.153,
    -0.023
]
chfbgf = [
    -0.009,
    -0.054
]
dqfgf = [
    -0.557,
    -0.955
]
cqfgf = [
    -0.36,
    -0.692
]

ttfpr = [
    0.096,
    -0.044,
    0.209,
    0.151,
    0.205,
    0.866,
    0.307,
    0.35,
    0.205,
    0.001,
    0.191,
    -0.047,
    0.304,
    0.447,
    0.218,
    0.071,
    -0.069,
    0.138,
    0.033,
    0.09,
    0.646
]
mtfpr = [
    -0.064,
    0.009,
    -0.118,
    -0.042,
    -0.872,
    -0.866,
    0.042,
    0.019,
    0.1,
    0.006,
    -0.105,
    0.013,
    0.123,
    0,
    -0.327,
    -0.474,
    0.036,
    0.0238,
    0.233,
    0.026,
    -0.651
]
itfpr = [
    -0.289,
    -0.069,
    -0.174,
    -0.272,
    0.872,
    0.866,
    0.107,
    0.365,
    0.3,
    -0.076,
    -0.143,
    -0.021,
    0.126,
    0.5,
    0.206,
    -0.218,
    -0.237,
    0.18,
    -0.277,
    0.365,
    -0.792
]
chfpr = [
    -0.056,
    0.09,
    0.072,
    -0.053,
    0.359,
    0.866,
    -0.042,
    -0.137,
    -0.3,
    0.084,
    -0.17,
    -0.118,
    0.01,
    0.354,
    0.035,
    -0.419,
    0.063,
    -0.004,
    -0.037,
    -0.055,
    -0.027
]
dqfpr = [
    -0.376,
    -0.877,
    -0.832,
    0.153,
    -0.899,
    -0.899,
    -0.981,
    -0.847,
    -0.975,
    -0.391,
    -0.596,
    -0.115,
    -0.958,
    0.41,
    -0.381,
    -0.51,
    -0.744,
    -0.859,
    -0.964,
    -0.887,
    -0.917
]
cqfpr = [
    -0.404,
    0.463,
    0.37,
    0.39,
    -0.918,
    -0.899,
    -0.718,
    -0.595,
    -0.671,
    0.048,
    -0.346,
    -0.05,
    0.22,
    0.564,
    -0.446,
    -0.445,
    -0.347,
    -0.457,
    -0.298,
    -0.211,
    -0.572
]

ttfqf = [
    0.02,
    -0.019,
    0.014,
    0.43,
    0.111,
    -0.062,
    -0.162,
    0.174,
    -0.047,
    -0.272,
    0.418,
    0.062
]
mtfqf = [
    0.071,
    0.074,
    -0.472,
    -0.064,
    -0.013,
    0.052,
    -0.718,
    -0.045,
    0.125,
    -0.016,
    -0.03,
    -0.487
]
itfqf = [
    -0.089,
    0.33,
    -0.309,
    0.172,
    -0.145,
    -0.162,
    -0.765,
    -0.148,
    -0.518,
    -0.123,
    0.123,
    0.068
]
chfqf = [
    0.116,
    -0.107,
    0.026,
    -0.137,
    -0.112,
    -0.102,
    0.483,
    -0.086,
    -0.094,
    0.014,
    -0.111,
    -0.226
]
dqfqf = [
    -0.597,
    -0.641,
    -0.993,
    -0.75,
    -0.452,
    -0.892,
    -0.997,
    -0.85,
    -0.599,
    -0.893,
    -0.748,
    -0.045
]
cqfqf = [
    -0.203,
    0.027,
    -0.676,
    -0.702,
    0.378,
    -0.577,
    -0.782,
    -0.585,
    -0.309,
    -0.652,
    -0.653,
    0.195
]


def build_violin_for_metrics():
    df = pd.DataFrame({
        'Turnaround Time': tt,
        'Merge Time': mt,
        'Idle Time': it,
        'Churn': ch,
        'Developer Quantity': dq,
        'Comment Quantity': cq
    })
    
    fig = go.Figure()

    turnaround_time = df["Turnaround Time"]
    fig.add_trace(go.Violin(y=turnaround_time, name="Turnaround Time"))

    merge_time = df["Merge Time"]
    fig.add_trace(go.Violin(y=merge_time, name="Merge Time"))

    idle_time = df["Idle Time"]
    fig.add_trace(go.Violin(y=idle_time, name="Idle Time"))

    churn = df["Churn"]
    fig.add_trace(go.Violin(y=churn, name = "Churn"))

    develop = df["Developer Quantity"]
    fig.add_trace(go.Violin(y=develop, name="Developer Quantity"))

    comment = df["Comment Quantity"]
    fig.add_trace(go.Violin(y=comment, name="Comment Quantity"))

    fig.show()

def build_violin_for_categories():
    test = {
        'Build Management': bm,
        'General Function': gf,
        'PR Management': pr,
        'Quality Facilitating': qf
    }

    df = pd.DataFrame.from_dict(test, orient='index')
    df = df.transpose()
    fig = go.Figure()

    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    general = df['General Function']
    fig.add_trace(go.Violin(y=general, name="General Function"))
    
    prm = df['PR Management']
    fig.add_trace(go.Violin(y=prm, name="PR Management"))

    qual = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qual, name="Quality Facilitating"))

    fig.show()

def plot_for_tt_per_category():
    turnaround_times = {
        'Build Management': ttfbm,
        'General Function': ttfgf,
        'PR Management': ttfpr,
        'Quality Facilitating': ttfqf
    }

    df = pd.DataFrame.from_dict(turnaround_times, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Turaround Times per Bot Category")
    fig.show()

def plot_for_mt_per_category():
    merge_times = {
        'Build Management': mtfbm,
        'General Function': mtfgf,
        'PR Management': mtfpr,
        'Quality Facilitating': mtfqf
    }

    df = pd.DataFrame.from_dict(merge_times, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Merge Times per Bot Category")
    fig.show()

def plot_for_it_per_category():
    idle_times = {
        'Build Management': itfb,
        'General Function': itfgf,
        'PR Management': itfpr,
        'Quality Facilitating': itfqf
    }

    df = pd.DataFrame.from_dict(idle_times, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Idle Times per Bot Category")
    fig.show()

def plot_for_churn_per_category():
    churn = {
        'Build Management': chfbm,
        'General Function': chfbgf,
        'PR Management': chfpr,
        'Quality Facilitating': chfqf
    }

    df = pd.DataFrame.from_dict(churn, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Churn per Bot Category")
    fig.show()

def plot_for_dev_per_category():
    dq = {
        'Build Management': dqfbm,
        'General Function': dqfgf,
        'PR Management': dqfpr,
        'Quality Facilitating': dqfqf
    }

    df = pd.DataFrame.from_dict(dq, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Developer Quantity per Bot Category")
    fig.show()

def plot_for_cq_per_category():
    cq = {
        'Build Management': cqfbm,
        'General Function': cqfgf,
        'PR Management': cqfpr,
        'Quality Facilitating': cqfqf
    }

    df = pd.DataFrame.from_dict(cq, orient='index')
    df = df.transpose()
    fig = go.Figure()
    
    build = df['Build Management']
    fig.add_trace(go.Violin(y=build, name="Build Management"))

    gf = df['General Function']
    fig.add_trace(go.Violin(y=gf, name="General Function"))

    pr = df['PR Management']
    fig.add_trace(go.Violin(y=pr, name="PR Management"))

    qf = df['Quality Facilitating']
    fig.add_trace(go.Violin(y=qf, name="Quality Facilitating"))

    fig.update_layout(title="Spearman Correlation of Comment Quantity per Bot Category")
    fig.show()

if __name__ == '__main__':
    plot_for_tt_per_category()
    plot_for_mt_per_category()
    plot_for_it_per_category()

    plot_for_churn_per_category()
    plot_for_dev_per_category()
    plot_for_cq_per_category()
    
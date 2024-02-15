import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Comments_Apache.csv', index_col=False)
    with_bot = df.loc[df['Bot Present?'] == True]
    without_bot = df.loc[df['Bot Present?'] == False]

    with_bot.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Apache_Comments_WithBots_F.csv', index=False)   
    without_bot.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Apache_Comments_WithoutBots_F.csv', index=False)   



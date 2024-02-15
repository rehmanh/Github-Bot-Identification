import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/RQ4_Fixed.csv', index_col=False)
    with_bot = df.loc[df['Bot Present?'] == True]
    without_bot = df.loc[df['Bot Present?'] == False]

    with_bot.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/RQ4WithBots_F.csv', index=False)   
    without_bot.to_csv('/Users/rehmanh/Desktop/Research/Chenhao Bot Study/RQ4WithOutBots_F.csv', index=False)   



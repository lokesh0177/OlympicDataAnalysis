import pandas as pd


def preprocess(df, region_df):
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left', left_on=None, right_on=None)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    df.drop_duplicates(inplace=True)
    return df

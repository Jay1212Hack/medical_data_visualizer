import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 5. Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])\
                   .size().reset_index(name='total')

    # 6. Draw the catplot with sns.catplot()
    plot = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                       data=df_cat, kind='bar')

    # 7. Get the figure
    fig = plot.fig
    return fig


def draw_heat_map():
    # 8. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 9. Calculate the correlation matrix
    corr = df_heat.corr()

    # 10. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 11. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 12. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0,
                square=True, linewidths=.5, cbar_kws={'shrink': .45, 'format': '%.2f'})

    return fig

import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(data, column):
    fig, ax = plt.subplots()
    sns.histplot(data[column].dropna(), bins=30, ax=ax)
    return fig

def create_boxplot(data, column):
    fig, ax = plt.subplots()
    sns.boxplot(y=data[column], ax=ax)
    return fig

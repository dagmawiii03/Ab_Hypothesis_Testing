#importing important libraries

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
    
    '''defined function to do bar plot with the following structure
'''
    plt.figure(figsize=(12, 7))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()

def plot_box(df: pd.DataFrame, x_col: str, title: str) -> None:
    
    '''defined function to do box plot with the following structure
'''
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()
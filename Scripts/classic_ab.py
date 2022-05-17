import pandas as pd
from numpy import std, mean
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint


def get_conversion_rates(df: pd.DataFrame, grouping_column: str, calculation_column: str) -> pd.DataFrame:

    # Grouping the dataframe by the grouping column and getting calculation column
    conversion_rates = df.groupby(grouping_column)[calculation_column]

    # defining methods to generate the standard deviation and standard error of mean
    def std_p(x): return std(x, ddof=0)
    def se_p(x): return stats.sem(x, ddof=0)

    # creating the conversion datagrame
    conversion_rates = conversion_rates.agg([mean, std_p, se_p])
    conversion_rates.columns = [
        'conversion_rate', 'std_deviation', 'std_error']
    return conversion_rates


def get_group_result(df: pd.DataFrame, from_column: str, val_type: str, value_column: str) -> pd.Series:
    # Retrieve the group results
    group_results = df[df[from_column] == val_type][value_column]
    return group_results


def get_count(group_result: pd.Series) -> int:
    return group_result.count()



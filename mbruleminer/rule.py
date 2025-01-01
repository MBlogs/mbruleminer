import pandas as pd
from typing import Callable

class Rule:
    rule_name:str = None
    rule_description:str = None
    rule_function:Callable = None
    
    def __init__(self, 
                 rule_function:Callable,
                 rule_name:str="rulename",
                 rule_description:str="A rule to apply to a dataframe"):
        """
        Creates a rule to apply to a dataframe
        :param rule_function: Function for df row, returning boolean
        :type parameter1:function
        :raises ExceptionType: 
        """
        self.rule_function = rule_function
        self.rule_name = rule_name
        self.rule_description = rule_description

    def apply_to_series(self, df: pd.Series, none_when_error=True) -> bool:
        """
        Applies rule function to df row, represented as a named Series
        none_on_error parameter controls if rule function errors return None or False
        :param df: A pandas dataframe row
        :type df:pandas.DataFrame
        :param none_when_error: If True, errors will return None, otherwise they return False  
        :type strict: boolean
        :return: Returns result of applying rule function if boolean, None otherwise
        :rtype: boolean
        """
        if not isinstance(df, pd.Series):
            raise Exception("Rule function must be applied to a dataframe row")
        rule_evaluation = None
        try:
            rule_evaluation = self.rule_function(df)
        except Exception as e:
            pass
        # TODO: Could give grace to 1, 0 and np.False_ and np.True_
        if not isinstance(rule_evaluation, bool):
            if none_when_error:
                return None
            else:
                return False
        return rule_evaluation
            
    def apply(self, df: pd.DataFrame, none_when_error=False) -> bool:
        """
        Applies this rule to a supplied dataframe
        If the rule errors, or returns a value other than True or False, None is returned
        :param df: A pandas dataframe or Series, with named columns matching this rule
        :type parameter1:function
        :return: Returns Series of boolean (or None) results from applying rule to each row
        :rtype: list
        """
        if isinstance(df, pd.Series):
            return self.apply_to_series(df, none_when_error)
        if not isinstance(df, pd.DataFrame):
            raise Exception("Rule function must be applied to a dataframe")
        # TODO: How to transfer strict parameter to apply
        rule_evaluation = df.apply(
            self.apply_to_series,
            axis=1,
            args=(none_when_error,)
        )
        # TODO: Do we want to return Series or the more general list?
        return rule_evaluation
        




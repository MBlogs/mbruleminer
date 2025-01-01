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
        :param rule_function: Function receiving dataframe, returning boolean
        :type parameter1:function
        :raises ExceptionType: 
        """
        self.rule_function = rule_function
        self.rule_name = rule_name
        self.rule_description = rule_description
    
    def apply(self, df: pd.DataFrame) -> bool:
        """
        Applies this rule to a supplied dataframe
        If the rule errors, or returns a value other than True or False, None is returned
        :param df: A pandas dataframe, with named columns matching this rule
        :type parameter1:function
        :return: Returns result of applying rule function if boolean, None otherwise
        :rtype: boolean
        """
        rule_evaluation = self.rule_function(df)
        if not isinstance(rule_evaluation, bool):
            return None
        return rule_evaluation
        




from collections import OrderedDict
from mbruleminer.rule import Rule

class RuleSet(OrderedDict):

    def __init__(self, rules, *args, **kwargs):
        """
        Accepts a dict or list of Rules
        :param rules: Dictionar or list of Rule objects
        :type parameter1: dict or list
        :raises ExceptionType: Errors if rules is not a dict or list, or any non-Rule object is found
        """
        if isinstance(rules, list):
            # TODO: Handle duplicate rule names
            rules = {rule.rule_name:rule for rule in rules}
        
        if not isinstance(rules, dict):
            raise Exception("Rules must be a list or dict of Rule objects")
        if not all([isinstance(rule, Rule) for rule in rules.values()]):
            raise Exception("Rules must be a list or dict of Rule objects")
        
        super().__init__(rules, *args, **kwargs)


    def apply_to_df(self, df):
        """
        Applies all rules in this RuleSet to a dataframe
        :param df: A pandas dataframe to apply rules to
        :type parameter1: pandas.DataFrame
        :return: Returns a list of boolean results from applying each rule in the RuleSet
        :rtype: boolean
        """
        # TODO: Make sure this is row-wise
        results = [rule.apply_to_df(df) for rule in self.values()]
        return results

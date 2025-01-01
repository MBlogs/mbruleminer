import pandas as pd
from mbruleminer.rule import Rule
from mbruleminer.ruleset import RuleSet

def test_create_ruleset():
    
    def rule_function(df):
        return True
    
    rule1 = Rule(rule_function, "rule1")
    rule2 = Rule(rule_function, "rule2")
    # From list
    ruleset = RuleSet([rule1, rule2])
    # From dict, which ruleset should now be.
    ruleset = RuleSet(ruleset)

    rule_evaluations = ruleset.apply(None)

    assert rule_evaluations == [True, True], f"Ruleset evaluation expected [True, True], got {rule_evaluations}"


from mbruleminer.rule import Rule

def test_rule():
    def rule_function(df):
        return True
    rule = Rule(rule_function)
    assert rule.apply(None), f"Rule should return True, got {rule.apply(None)}"
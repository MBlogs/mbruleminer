from mbruleminer.rule import Rule
import pandas as pd

def test_apply():
    def rule_function_ok(df_row):
        return bool(df_row['a'] == df_row['b'])
    rule = Rule(rule_function_ok)
    df = pd.DataFrame({"a":[1,1], "b":[1,2]})
    # Single row
    rule_evaluation = rule.apply(df.iloc[0])
    assert rule_evaluation, f"Rule evaluation expected True, got {rule_evaluation}"
    # Multiple rows
    rule_evaluation = rule.apply(df)
    assert rule_evaluation.tolist()==[True, False], f"Rule evaluation expected [True, True], got {rule_evaluation}"

def test_apply_badvalue_none_when_error():
    def rule_function_badvalue(df_row):
        return 5 # Not a boolean
    df = pd.DataFrame({"a":[1,1], "b":[1,2]})
    df_row = df.iloc[0]
    # Bad return
    rule = Rule(rule_function_badvalue)
    rule_evaluation = rule.apply(df_row, none_when_error=True)
    assert rule_evaluation is None, f"Bad rule value, none_when_error=True: expect None, got {rule_evaluation}"
    rule_evaluation = rule.apply(df_row, none_when_error=False)
    assert rule_evaluation == False, f"Bad rule value, none_when_error=True: expect False, got {rule_evaluation} "


def test_apply_badname_none_when_error():
    def rule_function_badname(df_row):
        return bool(df_row['c'] == 1) # Column c does not exist
    df = pd.DataFrame({"a":[1,1], "b":[1,2]})
    df_row = df.iloc[0]
    rule = Rule(rule_function_badname)
    rule_evaluation = rule.apply(df_row, none_when_error=True)
    assert rule_evaluation is None, f"Bad rule name, none_when_error=True: expect None, got {rule_evaluation}"
    rule_evaluation = rule.apply(df_row, none_when_error=False)
    assert rule_evaluation == False, f"Bad rule name, none_when_error=True: expect False, got {rule_evaluation}"
    

def test_rule_function():
    df = pd.DataFrame({"a":[1,2], "b":[1,1]})
    rule = Rule(lambda df: bool(df['a'] + df['b'] <= 2))
    rule_evaluation = rule.apply(df)
    assert rule_evaluation.tolist()==[True, False], f"Rule evaluation expected [True, True, False], got {rule_evaluation}"
    


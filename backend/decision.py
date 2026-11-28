# Determine transaction decision based on fraud probability
def make_decision(fraud_probability: float):

    if fraud_probability >= 0.80:
        return "DENY"

    elif fraud_probability >= 0.40:
        return "VERIFY"

    else:
        return "APPROVE"
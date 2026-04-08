def rule_based_detection(packet_rate, drop_rate, energy):
    if drop_rate > 0.3 or energy < 0.3:
        return 1
    return 0


def hybrid_detection(model, sample):
    ml_pred = model.predict([sample])[0]
    rule_pred = rule_based_detection(*sample)

    if ml_pred == 1 or rule_pred == 1:
        return "ATTACK"
    return "NORMAL"

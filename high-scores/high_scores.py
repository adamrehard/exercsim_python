def latest(scores):
    return scores[-1]


def personal_best(scores):
    result = sorted(scores, reverse=True)[:1]
    return int(result[0])

def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]

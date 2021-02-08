def latest(scores):
    return scores[-1]


def personal_best(scores):
    highest_score = 0
    for i in scores:
        if i > highest_score:
            highest_score = i

    return highest_score


def personal_top_three(scores):
    pass

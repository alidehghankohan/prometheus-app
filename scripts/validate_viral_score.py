def viral_score(hook_strength, pacing, twist, loop):
    score = hook_strength + pacing + twist + loop
    return min(score, 10)
import math

lower = 1
upper = 20
factors = set([x for x in range(lower, upper + 1)])

mid = lower + (upper - lower) // 2
bottom_half = [x for x in range(lower, mid + 1)]
top_half = [x for x in range(mid + 1, upper+1)]

candidate = math.prod(top_half)

div_idx = 1
next_candidate_good = True
while div_idx < len(bottom_half):
    next_candidate_good = True
    next_candidate = candidate // bottom_half[div_idx]
    for x in top_half:
        if next_candidate % x != 0:
            div_idx += 1
            next_candidate_good = False
            break
    if next_candidate_good:
        candidate = next_candidate
print(candidate)

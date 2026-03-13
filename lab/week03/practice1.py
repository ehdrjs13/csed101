def calc_score(data) -> tuple: 
    sum = 0
    cnt = 0
    max = data[0]
    for v in data:
        sum += v
        cnt += 1

        if v >= max:
            max = v

    return sum / cnt, max

score_list1 = [85, 90, 78]

ans = calc_score(score_list1)

print(f"avg = {ans[0]}, max = {ans[1]}")
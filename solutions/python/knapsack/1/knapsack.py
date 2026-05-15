def rec(i, rem_wt, items, n):
    if i == n:
        return 0
    ans = rec(i+1, rem_wt, items, n)
    if rem_wt >= items[i]["weight"]:
        ans = max(ans, rec(i+1, rem_wt-items[i]["weight"], items, n) + items[i]["value"])

    return ans

def maximum_value(maximum_weight, items):
    return rec(0, maximum_weight, items, len(items))

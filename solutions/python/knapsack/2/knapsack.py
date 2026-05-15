from functools import lru_cache

def maximum_value(maximum_weight, items):
    n = len(items)

    @lru_cache(maxsize = None)
    def rec(i, rem_wt):
        if i == n:
            return 0
        ans = rec(i+1, rem_wt)
        if rem_wt >= items[i]["weight"]:
            ans = max(ans, rec(i+1, rem_wt-items[i]["weight"]) + items[i]["value"])

        return ans

    return rec(0, maximum_weight)

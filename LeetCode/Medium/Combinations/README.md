# 문제 설명
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

# Backtrack

def backtrack(candiate):
            if find_solution(candidate):
                output(candidate)
                return
        
            for next_candiate in list_of_candidates:
                if is_valid(next_candidate):
                    place(next_candiate)
                    backtrack(next_candiate)
                    remove(next_candiate)

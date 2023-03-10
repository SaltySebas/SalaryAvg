class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        if len(salary)==3:
            sum_avg = float(sum(salary) - min_sal - max_sal)
        else:
            sum_avg = float((sum(salary) - min_sal - max_sal)/(len(salary)-2))
        return(sum_avg)

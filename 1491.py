def average(self, salary: list) -> float:
    return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

"""
To solve job sequencing problems
"""

jobs = ["J4", "J3", "J1", "J2", "J5", "J6", "J7", "J8", "J9", "J10"]
profits = [5, 10, 20, 15, 1, 4, 5, 2, 3, 4]
deadlines = [3, 1, 2, 2, 3, 4, 5, 2, 3, 4]

def job_sequencing(jobs, profits, deadlines):
    # jobs: profits, deadlines
    dict_of_jobs = {}
    number_of_jobs = len(jobs)
    if number_of_jobs == len(profits) == len(deadlines):
        for i in range(number_of_jobs):
            dict_of_jobs[jobs[i]] = (profits[i], deadlines[i])
        print(dict_of_jobs)
    else:
        print("Lengths of lists are different.")
        return False
    max_time = max(deadlines)
    
    job_sequence = [None] * max_time
    total_profit = 0
    
    # Check for highest number
    while dict_of_jobs:
        highest_profit_job = max(dict_of_jobs.keys(), key=lambda k: dict_of_jobs[k][0])
        highest_profit_job_profit = dict_of_jobs[highest_profit_job][0]
        highest_profit_job_deadline = dict_of_jobs[highest_profit_job][1]
        dict_of_jobs.pop(highest_profit_job)

        index = highest_profit_job_deadline - 1

        while index >= 0:
            if job_sequence[index] == None:
                job_sequence[index] = (highest_profit_job, highest_profit_job_profit, highest_profit_job_deadline)
                total_profit += highest_profit_job_profit
                break
            else:
                index -= 1
    print(job_sequence)

    for i in range(max_time):
        print(f"{i + 1}. {job_sequence[i][0]} for profit of ${job_sequence[i][1]:0.2f} and original deadline of {job_sequence[i][2]}")
    print(f"Total profit: ${total_profit:0.2f}")


job_sequencing(jobs, profits, deadlines)



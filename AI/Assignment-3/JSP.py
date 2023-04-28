def schedule_jobs(jobs):
   
    jobs = sorted(jobs, key=lambda x: x[1])  # sort by end time
    schedule = []
    prev_end_time = 0
    for job in jobs:
        start_time, end_time, profit = job
        if start_time >= prev_end_time:
            schedule.append(job)
            prev_end_time = end_time
    return schedule
jobs = [(0, 6, 50), (1, 4, 30), (3, 5, 10), (5, 7, 20), (7, 8, 5)]
schedule = schedule_jobs(jobs)
print("Scheduled jobs:")
for job in schedule:
    print(f"Start time: {job[0]}, End time: {job[1]}, Profit: {job[2]}")



#Implement job  Scheduling  with deadlines using a greedy method.
def job_scheduling(jobs):
    # Sort the jobs by their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    n = len(jobs)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    
    # Initialize a list to represent time slots
    time_slots = [False] * (max_deadline + 1)
    
    # Initialize variables to keep track of the selected jobs and total profit
    selected_jobs = []
    total_profit = 0
    
    # Iterate through the sorted jobs
    for job in jobs:
        deadline, profit = job[1], job[0]
        
        # Find the next available time slot
        while deadline > 0 and time_slots[deadline]:
            deadline -= 1
        
        # If a time slot is available, schedule the job
        if deadline > 0:
            time_slots[deadline] = True
            selected_jobs.append(job)
            total_profit += profit
    
    return selected_jobs, total_profit

# Example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
selected_jobs, total_profit = job_scheduling(jobs)

print("Selected Jobs:")
for job in selected_jobs:
    print(f"Job {job[0]} (Profit: {job[2]})")

print(f"Total Profit: {total_profit}")

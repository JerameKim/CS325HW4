def merge_sort(my_list, sort_func: lambda x, y: x < y):

    # 1. Exit Statement
    #   only gets called n number of times
    if len(my_list) <= 1:
        return my_list

    middle_idx = len(my_list) // 2

    # 2. Recurse
    # left = merge_sort(my_list[0:middle_idx])
    # will return a sorted list from "left side"
    left = merge_sort(my_list[:middle_idx], sort_func)

    # right = merge_sort(my_list[middle_idx:len(my_list)-1])
    # will return a sorted list from "right side"
    right = merge_sort(my_list[middle_idx:], sort_func)

    # 3. Resolve Recursion
    sorted_list = merge(left, right, sort_func)
    return sorted_list


def merge(left, right, sort_func) -> []:

    combined = []

    left_idx = 0
    right_idx = 0

    # Run while there's uncompared values in both lists
    while left_idx < len(left) and right_idx < len(right):

        # if left's value smaller than right's value
        if sort_func(left[left_idx], right[right_idx]):
            # add the left value in
            combined.append(left[left_idx])

            # increment to compare to next left element
            left_idx += 1

        else:
            combined.append(right[right_idx])
            right_idx += 1

    # If there's uncompared values in right list, add the uncompaed values into combined
    while right_idx < len(right):
        combined.append(right[right_idx])
        right_idx += 1

    # if there's uncompared values values in left list, add the uncompared values into combined
    while left_idx < len(left):
        combined.append(left[left_idx])
        left_idx += 1
    return combined
# ------------------------------------------------------------------------------------------------------------
#   all jobs take 1 minute 
# finish all tasks, minimize toal penalty cost 
# choose job with the highest penalty/deadline ratio


def schedulingProblem(jobs): 
    # append each job we've completed in order 
    jobs_done = []
    jobs_with_costs=[]
    current_time = 0 
    penalty_cost = 0 
    # create array of cost penalties
    for job_idx, job_value in enumerate(jobs): 

        #   higher penalty, higher cost ratio/priority 
        #   higher deadline, lower priority
        cost_ratio = job_value[1]/job_value[0]
        
        new_job = (cost_ratio, jobs[job_idx])

        # new jobs array with the cost and eveyrthing else 
        jobs_with_costs.append(new_job)
    sorted_list = merge_sort(jobs_with_costs, lambda x, y: x[0] > y[0])
    # print(sorted_list)
    
    # Go through array of job_costs
    for job in sorted_list: 
        # if deadline is after current_time, penalty 
        if current_time < job[1][0]: 
            # add penalty if greater
            penalty_cost+= job[1][1]

        # else deadline is before current_time, do nothing 

        # increase day 
        jobs_done.append(job[1])
        current_time += 1

    return jobs_done

jobs = [(1, 2), (1, 3), (5, 10), (2, 13), (12, 8)]
print(schedulingProblem(jobs))

jobs = [(1, 10), (2, 5), (3, 4), (4, 2), (5, 1)]
print(schedulingProblem(jobs))
#jobs scheduled([0, 1, 2, 3, 4], [])

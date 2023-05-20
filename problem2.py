#!/usr/bin/env python
# coding: utf-8

# In[5]:


def job_seq(jobs):
    # Sort jobs by their end times
    jobs = sorted(jobs, key=lambda x: x[1])
    print(jobs)
    b = len(jobs)
    
    # dp array to store the maximum profit
    dp = [0] * b
    dp[0] = jobs[0][2] #maximum profit of first job 
    
    #dynamic programing to avoide recomputing the same values multiple time and break down complex problem into 
    
    # the maximum profit for each job
    for i in range(1, b): #start from the second job
        # Find  last job  doesn't overlap with the current job
        j = i - 1 #from the first job again
        while j >= 0 and jobs[j][1] > jobs[i][0]:
            # end time of job in index j & start time of current job
            j -= 1
        
        # Compute maximum profit for the current job
        #dp[i-1]-->profit of job already exist in dp list
        #dp[j]-->job on the work
        #jobs[i][2]-->profit of jth job
        dp[i] = max(dp[i-1], dp[j]+jobs[i][2])
    
    # Return maximum profit
    #dp is a list of integers and b is an integer indicating the length of the dp list
    #dp[b-1] represents the last element of the list
    return dp[b-1]


# In[6]:


jobs = [(1, 6, 6), (2, 5, 5), (5, 7, 5), (6, 8, 3)]
max_profit = job_seq(jobs)
print("Maximum profit:", max_profit)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


def job_sequence(jobs):
    # Sort the jobs of their profits
    #decresing order
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    a = len(jobs)
    print(jobs)
    # time and the profit
    time = [False] * a
    profit = 0
    
    #  the jobs
    for i in range(a):
        # Find  slot for the job
        for j in range(min(a, jobs[i][1])-1, -1, -1):#-1 end value loop stops before reaching 0     # -1 step(count down)
            #min(a, jobs[i][1]) is subtracted by 1 to give the maximum value for the range.
            if not time[j]:
                time[j] = True
                profit += jobs[i][2]
                break
                
    # Count  number of jobs done
    count = sum(time)
    
    return count, profit


# In[4]:


jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
count, profit = job_sequence(jobs)
print(" jobs done:", count)
print("Maximum profit:", profit)


# In[7]:






# In[ ]:





# In[ ]:





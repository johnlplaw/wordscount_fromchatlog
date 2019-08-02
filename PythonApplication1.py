# This is for demostrate the steps to calculate the words count of the users from a chat log file.
# The dataframe is used for demostrate a table usage in a database when processing a chat log which is in huge file size.
# The purpose to doing so is for minimizing the memory usage to handle big file size of chat log.
# An instant of the the dataframe would be representing a table in database.

import numpy as np
import pandas as pd

#Step 1 - collect data from the log

# Read the contents from the file
with open("TextFile1.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# dataframe is used for demotrate the storage
df = pd.DataFrame(columns=['user', 'words'])
loglist = [];

for line in lines:
    print(line)
    #seperate the user and words
    content = line.split(":")
    #keep the content into array
    loglist.append(content)
    
#Store the log content into dataframe
df = df.append(pd.DataFrame(loglist,columns=df.columns))

# view the log content in data frame    
print(df)

#Step 2 - split the words for each rows
df['wordsplited'] = df['words'].str.split(" ")

#Step 3 - split the words for each rows
df['wordcount'] = df['wordsplited'].str.len()

print(df)

#Step 4 - aggregate / counting
all_together = df.groupby(['user']).agg({'wordcount':[np.sum]})

print(all_together)

#Step 5 - expoert to json format
all_together.to_json(r'result.json')

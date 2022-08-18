
## Problem 2

## Import the required libraries
import pandas as pd
import numpy as np
import regex as re
import csv
import json

## Define the function solution

def solution(jsonData):

  df = pd.read_json(jsonData)

  for index,row in df.iterrows():

    txt = df['description'].iloc[index]
    #print(txt)

    #removing sysmbols
    pattern = re.compile('[^-\w]')
    txt = re.sub(pattern,' ',txt)
    # print(txt)

    # if len(txt) == 0:
    #   return df['num_bedrooms'].iloc[index]

    #lowercase
    txt = [i.lower() for i in txt.split()]
    txt = ' '.join(txt)
    # print(txt)

    #remving extra spaces
    txt = re.sub('\s+',' ',txt)
    # print(txt)

    # word studio 
    pattern = re.compile('(\w+ studio)')
    words_list = re.findall(pattern,txt)
    words_set = set(words_list)
    # print(words_set)

    orignal_list = set(['yoga studio','art studio','dance studio'])

    remover_set = orignal_list.intersection(words_set)
    # print('remover_set = ', remover_set)

    # print('text=',txt)
    for word in remover_set:
      txt = re.sub(word,' ',txt)

    #print(txt)
    #print(df['num_bedrooms'].iloc[index])

    if '1-bedroom' in txt.split():
      df['num_bedrooms'].iloc[index] = 1
    if 'studio' in txt.split():
      df['num_bedrooms'].iloc[index] = 0

  return np.array(df['num_bedrooms'].tolist())




## Test cases:

print("Output of test file file1.json")
op1 = solution('file1.json')
print(op1)
print()

print("Output of test file file2.json")
op2 = solution('file2.json')
print(op2)
print()


"""
## Output:

Output of test file file1.json
[0 1 1 0]

Output of test file file2.json
[0 1 0 1 1]



"""


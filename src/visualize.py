#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items[0:11]:
#    print(k,':',v)
# Get the top 11 items sorted by y-value in descending order
sorted_data = sorted(items[0:10], key=lambda item: item[1], reverse=False)
#sorted_data = sorted(sorted_data, key=lambda item: item[1])
#print("sorted_data=", sorted_data)

## Extract the x and y values
#x = [item[0] for item in sorted_data]
#y = [item[1] for item in sorted_data]
#print("y=", y)
x = range(len(sorted_data)) 
y = [item[1] for item in sorted_data]
label = [item[0] for item in sorted_data] 
print("x,y=", x,y)
plt.bar(x, y)

print("(x,y)=", (x,y))
# Create the bar plot

plt.xticks(x,label)

# Set the x-axis label and y-axis label
plt.xlabel("Country")
plt.ylabel("Volume of Tweets")

# Set the font family for the plot title
plt.rcParams['font.family'] = 'NanumGothic'

## Set the title of the plot
#plt.title("#Coronavirus Occurrences in each Language on Twitter")

plt.savefig("covid_country_ko")

# Display the plot
plt.show()

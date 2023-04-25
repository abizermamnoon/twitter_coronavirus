#!/usr/bin/env python3

import matplotlib.pyplot as plt
import glob
from datetime import datetime

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

file_paths = glob.glob('outputs/geoTwitter*.country')
results = {}

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in file_paths:
    # extract the date from the file name
    date_str = os.path.splitext(os.path.basename(path))[0][10:18]
    date = datetime.strptime(date_str, '%y-%m-%d')
    try:
        with open(path) as f:
            data = json.load(f)
            # search for the keys in the data
            for key in args.key.split(','):
                if key in data:
                    if date not in results:
                        results[date] = defaultdict(int)
                    results[date][key] += sum(data[key].values())
    except json.decoder.JSONDecodeError:
        print(f"Skipping invalid JSON file: {path}")

# sort the results by date
results = dict(sorted(results.items()))
print("results=", results)

# extract the keys from the dictionary
keys = set()
for date, data in results.items():
    keys.update(data.keys())
keys = list(keys)
print("keys=", keys)
# plot the data
for key in keys:
    print("key =", key )
    x = list(results.keys())
    y = [results[date][key] for date in x]
    x = [date.date() for date in x]  # convert to date objec
    plt.plot(x,y,label = key)
print("x=", x)
print("y=", y)

# set the labels and legend
plt.xlabel('Day of the Year')
plt.ylabel('# of tweets that use hashtag')
# plt.title('Number of Tweets that use the # during the Year')

plt.legend()
# Save the plot as a png file
plt.savefig("sickvhosp.png")


## show the plot
plt.show()

# Coronavirus twitter analysis

In this project, I scanned all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

# Background

## About the Data

Approximately 500 million tweets are sent everyday. Of those tweets, about 2% are geotagged. That is, the user's device includes location information about where the tweets were sent from. My twitter dataset folder contains all geotagged tweets that were sent in 2020. In total, there are about 1.1 billion tweets in my dataset.

# Clean the Data
I followed the MapReduce procedure to analyze these tweets. I started by creating files that analyze each day of tweets and create individual files that that track the usage of the hashtags on a both a language and a county level. I then concatenate all the data in the files into two files based on language and country

```
$ ./src/reduce.py --input_paths outputs_1/geoTwitter*.lang --output_path=reduced.lang_1
```

```
$ ./src/reduce.py --input_paths outputs_1/geoTwitter*.country --output_path=reduced.country_1
```

# Visualize the Data

I wanted to visualize the usage of `#coronavirus` by language and country. If I were to visualize this data for all languages and all countries, the data would look messy so I filter down to the top 10 languages and countries that used `#coronavirus`. 

```
$ ./src/visualize.py --input_path=reduced.lang_1 --key='#coronavirus'
```

# Volume of Tweets with #coronavirus in 2020 (Top 10 Languages)

<img src=covid_1.png width=100% />

```
$ ./src/visualize.py --input_path=reduced.country_1 --key='#coronavirus'
```

# Volume of Tweets with #coronavirus in 2020 (Top 10 Countries)

<img src=covid_country_en.png width=100% />

I then wanted to visualize the usage of `#코로나바이러스` by language and country.If I were to visualize this data for all languages and all countries, the data would look messy so I filter down to the top 10 languages and countries that used `#코로나바이러스`.

```
$ ./src/visualize.py --input_path=reduced.lang_1 --key='#코로나바이러스'
```

# Volume of Tweets with #코로나바이러스 in 2020 (Top 10 Languages)

<img src=covid_2.png width=100% />

```
$ ./src/visualize.py --input_path=reduced.country_1 --key='#코로나바이러스'
```

# Volume of Tweets with #코로나바이러스 in 2020 (Top 10 Countries)

<img src=covid_country_ko.png width=100% />

# Time Series Data for Volume of Tweets

I wanted to be able to choose any number of hashtags and track its usage every day of 2020. For this reason, I wrote a python script that scans all the data andconstructs a dictionary of the tweet volume of the hashtag every day of the year. Using the bash script below, one can visualize the tweet volume for any random assortment of hashtags every day of the year.

```
$./alternative_reduce.py --key '#hospital,#sick'
```

# Number of Tweets that use the # during the Year

<img src=sickvhosp.png width=100% />

# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
![image](https://user-images.githubusercontent.com/88013297/132141531-528c702d-21a2-4b55-a26b-9f3b519515c7.png)

The results of the audit show that:
- There were 369,711 votes cast in the election.
- The county results were:
  - Jefferson county received 10.5% of the vote and 38,855 number of votes.
  - Denver county received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe county received 6.7% of the vote and 24,801 number of votes.
- Denver county had the largest number of votes with 306,055 votes.
- The candidate results were:
  - Charles Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election Audit Summary
This election poll python script can be used with more board of elections going forward. It is truly dynamic in that it can be modified for any similar election. A few modifications that could take place in order to be used for other elections are:

1. Importing a different election results data csv file which contains more details.
2. Referencing a different column within the data set to pulls different values outside of candidates and county votes.

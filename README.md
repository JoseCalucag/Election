# Election Analysis

<p align = "center">
<img src = "https://upload.wikimedia.org/wikipedia/commons/0/00/Seal_of_Colorado.svg" width = "200" height = "200">
 </p>

## Project Overview

I was tasked by the Colorado Board of Elections committee to complete an election audit of a recent local congressional election. With the collected data, they wanted certain data points to be reported:

 1) Determine the total number of votes casted.
 2) Create a list of candidates who received votes.
 3) Determine the total number of votes each candidate received.
 4) Calculate the percentage of votes each candidate won.
 5) Determine the winner of the election based on popular vote.
 6) Determine the number of votes that were casted from each county.
 7) Calculate the percentage of votes each county contributed to the election.
 8) Determine the county with the highest voter turnout.

## Resources 
- Data Source: [election_results.csv](https://raw.githubusercontent.com/JoseCalucag/Election-Analysis/master/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio code, 1.49

# Election Audit Results

<p align = "center">
<img src ="https://github.com/JoseCalucag/Election-Analysis/blob/master/Resources/PrintOut.png" width = "200" height = "250">
</p>

To answer the committee's data points:

- There were 369,711 votes cast in the election.

- The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
  
- The candidate results were:
  * Charles Casper Stockham recieved 23.0% of the vote with 85,213 votes.
  * Diana DeGette recieved 73.8% of the vote with 272,892 votes.
  * Raymon Anthony Doane recieved 3.1% of the vote with 11,606 votes.
  
- The winner of the election was:
    
    Diana DeGette
  
- The number of votes based on county are:
  * Jefferson County had 38,855 voters with 10.5% of the total voter turnout
  * Denver County had 306,055 voters with 82.8% of the total voter turnout
  * Araphoe County had 24,801 voters with 6.7% of the total voter turnout  

- The county with the highest voter turnout was:

  Denver County

# Audit Summary
Even though this code was created for tallying the votes for the state of Colorado election, you will be able to use this freely for future elections; and not just for Colorado. As long as the csv follows the same tabular format, you can use this for other counties, states, even countries. Just be sure to rename your data ccordingly in the python code. Also, you can try different methods of leveraging the data. For instance, when looking at the county code, consider looking at the counties that have the least amount of votes. That way, candidates can reconsider campaigning strategies.

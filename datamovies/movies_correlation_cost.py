import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import seaborn as sns
import numpy as np
%matplotlib inline
import math

movies = pd.read_csv("movies_2010_2015.csv", sep=';')

# clean data
movies_without_10_theaters = movies[movies['Theaters'] > 10]
movies = movies_without_10_theaters[movies_without_10_theaters['Budget'] != 'NaN']

# Production cost
budgets = movies.sort_values(by=['Budget'], ascending=False)['Budget']
y = range(0, len(budgets))

fig = plt.figure(figsize=(14, 10))
plt.scatter(y, budgets)
plt.xlabel('Ranked movies')
plt.ylabel('Cost of production (M€)')
plt.title("Cost of production movies 2010-2015 France")
plt.axis([-10, 1800, -10, 300])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,10))

average = sum(movies['Budget']) / len(movies['Budget'])
median = movies['Budget'].median()
average_line = plt.axhline(average, color='r', linestyle='dashed', linewidth=2, label='Average cost')
median_line = plt.axhline(median, color='g', linestyle='dashed', linewidth=2, label='Median cost')
plt.legend(handles=[average_line, median_line], loc = 'best')

plt.savefig('CostMovies.png')
plt.show()

# Production cost correlation
plt.figure(figsize=(14, 10))
plt.scatter(movies["Budget"], movies["Tickets"])
plt.xlabel('Production Cost (M€)')
plt.ylabel('Tickets sold')
plt.title("Tickets sold by production cost 2010-2015 France")
plt.axis([-10, 300, -10, 20000000])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,10))
plt.annotate('INTOUCHABLES', xy=(12, 19400000), xytext=(35, 17000000), arrowprops=dict(facecolor='green', shrink=4),)
plt.annotate("TRON L'HERITAGE", xy=(273, 1350000), xytext=(260, 8000000), arrowprops=dict(facecolor='red', shrink=4),)
plt.savefig('TicketsSoldByCost.png')
plt.show()
r, p_value = pearsonr(movies["Budget"], movies["Tickets"])

# Production cost correlation by sort
def generate_correlation_cost(genre):
    plt.figure(figsize=(14, 10))
    movies_genre = movies[movies['Genre'] == genre]
    plt.scatter(movies_genre["Budget"], movies_genre["Tickets"])
    plt.xlabel('Production Cost (M€)')
    plt.ylabel('Tickets sold')
    plt.title("Tickets sold by production cost for "+genre+" movies")
    plt.axis([-10, 300, -10, 20000000])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,10))

    r, p_value = pearsonr(movies_genre["Budget"], movies_genre["Tickets"])
    plt.text(210, 17000000, 'r = '+str(r), style='italic', fontsize=15, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    plt.savefig('TicketsByCost'+genre+'.png')
    plt.show()

movies_genre = ['Science-fiction', 'Comedy', 'Action', 'Drama', 'Comedy drama', 'Horror', 'Animation']
for genre in movies_genre:
    generate_correlation_cost(genre)
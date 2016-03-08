import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
%matplotlib inline

movies = pd.read_csv("movies_2010_2015.csv", sep=';')

def sum_per_column(column, year):
    return movies[movies['Year']==year][column].sum()

def count_per_year(year):
    return movies[movies['Year']==year].shape[0]

years = [2010, 2011, 2012, 2013, 2014, 2015]

tickets = []
for year in years:
    tickets.append(sum_per_column('Tickets', year))
    
x_axe = np.arange(6)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
width = 0.5

ax.bar(x_axe, tickets, width)

ax.set_ylabel('Tickets sold')
ax.set_xlabel('Year')
ax.set_title('Tickets sold per year')
ax.set_yticks(range(0, 240000000, 50000000))
ax.set_xticklabels(years)
ax.ticklabel_format(axis='y', style='sci', scilimits=(0,12))

sns.plt.show()


total_movies = []
for year in years:
    total_movies.append(count_per_year(year))
        
x_axe = np.arange(6)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.bar(x_axe, total_movies, width)

ax.set_ylabel('Movies')
ax.set_xlabel('Year')
ax.set_title('Movies released per year')
ax.set_yticks(range(0, 750, 100))
ax.set_xticklabels(years)
ax.ticklabel_format(axis='y', style='sci', scilimits=(0,12))

sns.plt.show()

average_tickets = []
for year in years:
    average_tickets.append(int(sum_per_column('Tickets', year)/count_per_year(year)))
        
x_axe = np.arange(6)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.plot(x_axe, average_tickets)

ax.set_ylabel('Movies')
ax.set_xlabel('Year')
ax.set_title('Average tickets sold per movie released per year')
ax.set_yticks(range(0, 400000, 50000))
ax.set_xticklabels(years)
ax.ticklabel_format(axis='y', style='sci', scilimits=(0,12))

sns.plt.show()


entrees = movies.sort_values(by=['Tickets'], ascending=False)['Tickets']
y = range(0, len(entrees))

fig = plt.figure(figsize=(14, 10))
plt.scatter(y, entrees)
plt.xlabel('Movies')
plt.ylabel('Tickets')
plt.title("Tickets by movies 2010-2015 France")
plt.axis([-10, 3900, 0, 20000000])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,10))

average = sum(movies['Tickets']) / len(movies['Tickets'])
plt.axhline(average, color='r', linestyle='dashed', linewidth=2)
plt.show()


entrees = movies.sort_values(by=['Tickets'], ascending=False)['Tickets']
y = range(0, len(entrees))

fig = plt.figure(figsize=(14, 10))
plt.plot(y, entrees)
plt.xlabel('Movies')
plt.ylabel('Tickets')
plt.title("Tickets by movies 2010-2015 France")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,10))

average = sum(movies['Tickets']) / len(movies['Tickets'])
plt.axhline(average, color='r', linestyle='dashed', linewidth=2)
plt.yscale('log')

plt.show()



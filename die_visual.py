from die import Die
import plotly.express as px

# Create a D6.
die = Die()

"""Roll the die, and store the results in a list."""
results = []
for n in range(1000):
    result = die.roll()
    results.append(result)
    
"""Analyze the results."""
frequencies = []
poss_results = list(range(1, die.num_sides + 1))
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
"""Visualize the results."""
fig = px.bar(x=poss_results, y=frequencies)
fig.show()

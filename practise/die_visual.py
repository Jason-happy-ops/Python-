from die import Die
import plotly.express as px

die=Die()
i=0
results=[]
while True:
    result = die.roll()
    results.append(result)
    i+=1
    if i>=100:
        break

frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = 'Results of Rolling One D6 100 Times'
labels = {'x':'Result','y':'Frequency of Result'}

fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.write_html('dice.html')
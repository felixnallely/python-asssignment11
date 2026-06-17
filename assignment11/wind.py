import plotly.express as px
import plotly.data as pldata
import pandas as pd 

df = pldata.wind(return_type='pandas')

#print first/last 10 rows 
print("First 10 Rows:")
print(df.head(10), "\n")

print("Last 10 Rows")
print(df.tail(10), "\n")

#Clean data: convert 'strength' column and type conversion
df['strength'] = (
    df['strength'].astype(str).str.replace(r'[^0-9\.]', '', regex=True).astype(float)
)

#Interactive scatterplot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency",
    labels={"strength": "Wind Strength", "frequency": "Frequency"},
)

#Save HTML file
fig.write_html("wind.html")
fig.show()
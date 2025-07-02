import pandas as pd
import plotly.express as px

# === Step 1: Load the dataset ===
try:
    df = pd.read_csv("top_10_population_2020.csv")
except FileNotFoundError:
    print("❌ Error: 'top_10_population_2020.csv' not found.")
    exit()

# === Step 2: Sort data by population ===
df_sorted = df.sort_values(by='Population', ascending=False)

# === Step 3: Create bar chart ===
fig = px.bar(
    df_sorted,
    x='Country Name',
    y='Population',
    title='Top 10 Most Populated Countries in 2020',
    labels={'Population': 'Population Count', 'Country Name': 'Country'},
    template='plotly_dark'
)

# === Step 4: Save the chart as HTML ===
output_file = "top_10_population_chart.html"
fig.write_html(output_file)

print(f"✅ Chart successfully saved as '{output_file}'")

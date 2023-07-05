import plotly.graph_objects as px
import pandas as pd

# reading the database
data = pd.read_csv("Module-5\\file2.csv")


plot = px.Figure(data=[px.Scatter(
	x=data['day'],
	y=data['tip'],
	mode='markers',)
])

# Add dropdown
plot.update_layout(
	updatemenus=[
		dict(
			type="buttons",
			direction="left",
			buttons=list([
				dict(
					args=["type", "scatter"],
					label="Scatter Plot",
					method="restyle"
				),
                dict(
					args=["type", "bar"],
					label="Bar Chart",
					method="restyle"
				)
			]),
		),
	]
)

plot.show()
# and check your default web browser
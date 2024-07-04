import pandas as pd
import plotly.express as px

def generate_interactive_plot(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Create an interactive scatter plot using Plotly Express
    fig = px.scatter(df, x='x', y='y', title='Interactive Scatter Plot')

    # Update layout for better visualization (optional)
    fig.update_layout(
        title='Interactive Scatter Plot',
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        hovermode='closest'
    )

    # Show the plot
    fig.show()

if __name__ == "__main__":
    file_path = 'texting.csv'  # Replace with your dataset file path
    generate_interactive_plot(file_path)

# Python Candlestick Chart and EMA Calculation

This project is aimed at creating a Candlestick Chart and calculating the Exponential Moving Average (EMA) from trade data. It reads trade data from a CSV file, forms candlesticks based on a given time period, and calculates the EMA for a given length. It is implemented in Python using libraries like Pandas, Dask, and Plotly.

## Getting Started

### Prerequisites

To run the project, you need to have Python installed on your system. The project also requires the following Python libraries:
- pandas
- dask
- plotly

Install the required libraries using pip:

```sh
pip install pandas dask plotly

Running the Project
Clone this repository to your local machine.
Navigate to the project directory in your terminal.
Run the main file:

python main.py

Follow the prompts to enter the desired timeframe and EMA period.

Running Tests
Navigate to the project directory and run the tests using the following command:

sh
Copy code
python -m unittest tests.py
Usage
When you run the main file, you will be prompted to enter the timeframe and the EMA period. Enter the timeframe in minutes (e.g., 5m for 5 minutes, 1H for 1 hour), and the EMA period as a positive integer (e.g., 14).

The project will read the trades from the provided CSV file, form candlesticks based on the provided timeframe, calculate the EMA for the given length, and plot the candlestick chart along with the EMA line.

Built With
Pandas - For data manipulation and analysis.
Dask - For parallel computing and optimizing data frame computations.
Plotly - For plotting the candlestick chart.

5m TF EMA 50
![image](https://github.com/instateofgrace/test_assignment/assets/78905325/fe803460-79b5-473c-aefd-4b6fb3951aa2)
![image](https://github.com/instateofgrace/test_assignment/assets/78905325/9c5f9acb-430e-48b1-9f1e-80c36c3bebd4)
1H TF EMA 50
![image](https://github.com/instateofgrace/test_assignment/assets/78905325/7c473bc5-eab3-4432-9920-646bc4e876b2)
![image](https://github.com/instateofgrace/test_assignment/assets/78905325/b0bc3c3f-086b-4f53-8ee8-881baac0e651)

Running tests
![image](https://github.com/instateofgrace/test_assignment/assets/78905325/82aeb6a2-711c-4412-a0c0-2e5708695e61)

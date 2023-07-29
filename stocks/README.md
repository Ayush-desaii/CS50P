
# Stocks






# Hi, I'm Ayush desai! 👋


## 🚀 About Me
I'm 19 and I'm a software engineering student at sarvajanik university surat, india.


## About Project

This Python project aims to provide data analysis and long-term investment recommendations for stocks. It retrieves stock information using the `yfinance` library, analyzes various metrics such as P/E ratio, debt-to-equity ratio, market capitalization, beta, and alpha, and makes a determination on whether the stock might be suitable for long-term investment.

### Prerequisites

To run this project, you need to have the following dependencies installed:

- Python 3.x
- pandas
- yfinance
- yahoo_fin

You can install these dependencies using `pip` by running the following command:


pip install pandas yfinance yahoo_fin

#### Usage

1. Clone the project repository or download the source code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the main.py file, passing the desired stock symbols as command-line arguments. For example:

```shell
python main.py AAPL MSFT GOOGL
```

- Replace AAPL, MSFT, GOOGL, etc., with the stock symbols you want to analyze.

- The program will provide information such as the stock's name, business summary, P/E ratio, debt-to-equity ratio, market capitalization, beta, and alpha. It will also make a recommendation on whether the stock might be suitable for long-term investment.

## Explanation

- The main() function serves as the entry point of the program. It verifies the command-line arguments, retrieves historical stock price data using yfinance, calculates the overall market return, and calls the fetch() function for each stock symbol.

- The fetch() function fetches additional stock information and metrics such as P/E ratio, debt-to-equity ratio, market capitalization, beta, and alpha. It also calls the alpha() function to calculate the alpha value based on the stock's historical returns compared to the market return. Finally, it makes a recommendation using the decision() function.

- The alpha() function calculates the alpha value, which represents the excess return of a stock compared to its expected return based on the index returns which is calculated in main() function.

- The decision() function determines whether a stock might be suitable for long-term investment based on predefined criteria for metrics such as P/E ratio(should be less then 15), debt-to-equity ratio(should be less then 1), market capitalization(should be greater then 10 billion), beta(should be less then 1), and alpha(should be greater then 5).

## Disclaimer

- The analysis and recommendations provided by this project are based on historical data and predefined criteria based on my knowledge. They should not be considered as financial advice. Always perform your own research and consult with a professional financial advisor before making investment decisions.







## 🔗 Links
[![video demo](https://img.shields.io/badge/video_demo-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://youtu.be/cSBXQU4fDEI)





import requests
import sys

if len(sys.argv) != 2:
    sys.exit("missing command-line argument")

try:
    n = float(sys.argv[1])
    a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    b = a.json()
    b = b["bpi"]["USD"]["rate_float"]
    b = b*n
    print(f"${b:,.4f}")

except requests.RequestException:
    print()

except ValueError :
    sys.exit("invalid command-line argument")
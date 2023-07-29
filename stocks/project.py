import datetime
import yfinance as yf
import pandas as pd
from yahoo_fin import stock_info as si
import sys

def main():

    if len(sys.argv) == 1 :
        sys.exit("too few arguments!")
    else :

        a = pd.DataFrame(si.tickers_dow())
        b = set( symbol for symbol in a[0].values.tolist() )
        my_list = ['W', 'R', 'P', 'Q']
        del_set = set()
        sav_set = set()

        for symbol in b:
            if len( symbol ) > 4 and symbol[-1] in my_list:
                del_set.add( symbol )
            else:
                sav_set.add( symbol )

        for tic in sys.argv[1:] :

            t = verify(sav_set,tic)
            if not t:
                sys.exit(f"{tic} does not exixt")

        i = "DIA"
        e = datetime.datetime.now()
        s = e - datetime.timedelta(days=5*365)
        data = yf.download(i, start=s, end=e)
        sv = data['Adj Close'].iloc[0]
        ev = data['Adj Close'].iloc[-1]
        r = ((ev - sv) / sv)*100

        data = []

        for tic in sys.argv[1:]:

            data.append(fetch(tic, r))



def verify(tickers,tic):

    tic = tic.upper()
    if tic in tickers :
        return True
    else :
        return False


def fetch(tic, r):

    tic = tic.upper()
    a = yf.Ticker(tic)
    b = (a.info["longBusinessSummary"]).split(";")
    print(a.info["shortName"])
    for i in b:
        print(f"--> {i}")
    print()

    c = []
    try :
        c.append(a.info["trailingPE"])
        print("P/E ratio : ",c[0])
    except KeyError:
        c.append("NA")
        print("P/E ratio : NA")

    try:
        c.append((a.info["debtToEquity"])/100)
        print("debt to equity ratio : ",c[1])
    except KeyError:
        c.append("NA")
        print("debt to equity ratio : NA")

    try :
        c.append(a.info["marketCap"])
        print("market capitalization : ",c[2])
    except KeyError:
        c.append("NA")
        print("market capitalization : NA")

    try :
        c.append(a.info["beta"])
        print("beta : ",c[3])
    except KeyError:
        c.append("NA")
        print("beta : NA")

    try :
        c.append(alpha(tic, r))
        print("alpha : ",c[4])
    except KeyError:
        c.append("NA")
        print("alpha : NA")

    print(c)

    if decision(c) == 1:
        print(f"{a.info['shortName']} might good for long-term investment")
    elif decision(c) == 0 :
        print(f"{a.info['shortName']} might not good for long-term investment")
    else :
        print(f"not have enough data about {a.info['shortName']}")

    print()

def alpha(tic, r):

    i = tic
    e = datetime.datetime.now()
    s = e - datetime.timedelta(days=5*365)
    data = yf.download(i, start=s, end=e)
    sv = data['Adj Close'].iloc[0]
    ev = data['Adj Close'].iloc[-1]
    re = ((ev - sv) / sv)*100

    return (re - r)

def decision(an):

    try:
        if an[0] < 15 and an[1] < 1 and an[2] > 10000000000 and an[3] < 1 and an[4] > 0:
            return 1
        else :
            return 0
    except TypeError:
        return 404

if __name__ == "__main__":
    main()
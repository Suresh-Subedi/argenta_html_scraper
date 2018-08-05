#!/usr/bin/python3
from bs4 import BeautifulSoup

raw_html = open(r'c:\argenta.htm').read()
html = BeautifulSoup(raw_html, 'html.parser')
x = []
for li in html.select('li'):
    y = li.find('span', attrs={'class':'ag-transactions-date-year'}).text
    m = li.find('span', attrs={'class':'ag-transactions-date-month'}).text
    d = li.find('span', attrs={'class':'ag-transactions-date-day'}).text

    counterparty = li.find('div', attrs={'class':'counterparty-name'}).find('strong').text

    typecontainer = li.find('div', attrs={'class':'transaction-type'}).find_all('span', recursive=False);
    typ = ''
    for span in typecontainer:
        if 'sr-only' not in span.attrs['class']:
            typ = span.find('span').text

    amount = li.find('span', attrs={'class':['ag-amount-negative', 'ag-amount-positive']}).text.split('\n')[0]
    amount = amount.replace(',', '.')
    currency = li.find('span', attrs={'class':'ag-currency-small'}).text

    class a:
        date = y + '-' + m + '-' + d
        counterparty = counterparty
        typ = typ
        amount = amount
        currency = currency
    x.append(a)

f = open(r"c:\argent.csv","w+")
for t in x:
    f.write("t.date + ", " + t.counterparty + ", " + t.typ + ', ' + t.amount + ', ' + t.currency + "\n")
f.close()

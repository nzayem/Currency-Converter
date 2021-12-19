# Currency-Converter based on data from flowRates website

Simple currency converter, based on json data from the website http://www.floatrates.com/json-feeds.html

The script initializes a dictionary with rates of US dollars and Euros, and in case of new currency, the json data are added to the dictionary allowing the data to be reused. The converted amount is then printed with the rate date.

I didn't used Python Json module, imported only requests in this script.

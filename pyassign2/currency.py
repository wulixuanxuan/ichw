#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
__author__ = "YuQi Xuan"
__pkuid__  = "1800011787"
__email__  = "1800011787@pku.edu.cn
__the data the python was last editted__="2018.12.3"

"""

from urllib.request import urlopen

def exchange (currency_from,currency_to,amount_from):
    
    """amount of currency received in the given exchange."""

    url_inf = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?"
    url_inf += "from=" + currency_from + "&to=" + currency_to + "&amt="+ str(amount_from)
    
    doc=urlopen(url_inf)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii') # to get a string
    jstr=jstr.replace("true","True") # to get a dictionary
    jstr = eval(jstr)
    return jstr["to"] 

def test_exchange():
    
    """test some cases"""
    
    assert("2.1589225 Euros"==exchange("USD","EUR",2.5))
    assert("2356.765097755 Argentine Pesos"==exchange("AED","ARS",220))
    assert("0.0040493227104313 Bitcoins"==exchange("BZD","BTC",60))    ,"the value is false"
    print("the test passed")
    
def main ():
    
    """Module for currency exchange"""
    
    currency_from = input("Please input the currency on hand: ")
    currency_to = input("Please input the currency to convert to: ")
    amount_from = input("Please input the amount of currency to convert: ")
    test_exchange()
    print(exchange(currency_from,currency_to,amount_from))
    
if __name__ == "__main__":
    main()


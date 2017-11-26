
import time 
from datetime import datetime
import urllib2
import ast  
import mechanize 
from bs4  import BeautifulSoup 


t1=time.time() 



mbc_historical="https://www.mercadobitcoin.net/api/trades/1420070400/"
mbc_url="http://www.mercadobitcoin.com.br/api/ticker/" 
ltc_url="http://www.mercadobitcoin.com.br/api/ticker_litecoin/"
bch_url="http://www.mercadobitcoin.com.br/api/BCH/ticker/"
coin_url="https://coinbase.com/api/v1/currencies/exchange_rates" 
spot_url="https://coinbase.com/api/v1/prices/spot_rate"
exch_rate="http://rate-exchange.appspot.com/currency?from=USD&to=BRL" 
exch_rate="https://www.google.com/search?q=1+usd+in+brl" 
order_book="http://www.mercadobitcoin.com.br/api/orderbook/" 
kraken_url="http://api.kraken.com/0/public/Ticker?pair=BCHUSD,XXBTZUSD"

#br.set_headers = [(':authority','www.google.com'),(':method','GET'),(':path','/search?q=1+usd+in+brl'),(':scheme','https'),('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('accept-encoding','gzip, deflate, sdch, br'),('accept-language','en-US,en;q=0.8,pt-BR;q=0.6,pt;q=0.4,zh;q=0.2'),('avail-dictionary','ghM1Vvtn'),('cookie','OGPC=765334528-4:278279168-2:560575488-4:976493568-6:946258944-4:908000256-6:864812032-6:391792640-8:193170432-3:699960320-1:448059392-2:1049715712-1:412595200-6:811773952-4:531737600-2:604273664-4:928362496-4:355367936-1:783732736-4:; _ga=GA1.1.1691645100.1493469457; OTZ=3877991_72_76_104100_72_446760; SID=yQSWvHZppeURE-psndA---tKtmp2oy3KwWClkrI36Zf5mv-7XTcgsokxcaNZ9hcNLVF27A.; HSID=AcHvyNI989otpJaUM; SSID=A3rLznVkBAeyv2-pJ; APISID=2-sinx15wzLGBQ5z/Ai5QOIN4CSde2B9JC; SAPISID=s_3XPrvbo_XW4W9g/A7igZuckMp6orZzQu; NID=105=Q7s7Zc3PaRnLLPkyraT2FI5sv3fJDE8Bzs8aSs4t20W10F9seEVwfOvHmZWSCVJghA8i314-TShk9qF3VrikcN9FO67T1tEjUkjw-gViHD_G1HAmsXmtOVhdC0jb-rNtrU2loqpwbzXE4HsQ9TbAoi1SRN4Byu-xAcasX8kH3GAYORsXa4y7uUAyHawkjxBh_NL0pCCqPpbgaHQ4TIeMeAN_kmtq4SX0NdPvblgYbTAHHV6vjv0MJtFjNKWUVRnrZLq0Zj2IbQop8qlexaUs2fPK5Ou4OgCK2CLZTSIFPbRM6JbFWnAMJ5UFqBx8S9mmAjBqDwYzbg0; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTQ5NzA5Mjc3MjIwMjAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6NDEwMzU3NjE1IGxvbmdpdHVkZV9lNzotNzM2ODIzNDY4fSByYWRpdXM6NTIwODA=;DV=k2LIO6TzJx9HINXQWGYfNuAqQncbydX9wZ9baRZHcAAAAEBTPR0m8SveeAEAADhOCcNpe3xCXwAAAA'),('upgrade-insecure-requests','1'),('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]


def fetch_data(url):
    br= mechanize.Browser() 
    br.set_handle_equiv(False) 
    br.set_handle_robots (False) 
    #br.set_headers = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'), ('Accept', '*/*')]
    br.set_headers = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'), ('Accept', '*/*')] #, ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), ('Accept-Encoding', 'none'), ('Accept-Language', 'en-US,en;q=0.8'), ('Connection', 'keep-alive')]
    resultado=[] 
#    print '-'*10
#    print "fetching "+url 
    res=br.open (url) 
    data=res.read() 
    return data




def getCoinbaseData(url):   
    data=fetch_data(url)
    coin=ast.literal_eval(data) 
    idx=('btc_to_usd', 'btc_to_brl', 'usd_to_brl','eth_to_usd','ltc_to_usd') 
    for i in idx:
        print "%s - %s"%(i, coin[i])

    return (float (coin['btc_to_usd']), float (coin["btc_to_brl"]), float (coin["usd_to_brl"]), float (coin["eth_to_usd"]), float (coin["ltc_to_usd"]))


def getKrakenData(url):
    data=fetch_data(url)
    data=ast.literal_eval(data)
    data=data["result"]

    return (float(data["XXBTZUSD"]["b"][0]), float(data["BCHUSD"]["b"][0]))

def getMBitcoinData(url):
    data=fetch_data (url)
    return float(ast.literal_eval(data)["ticker"]["last"])

def getGoogleFX(url):

    content=fetch_data(exch_rate)
    soup=BeautifulSoup(content)
    d=soup.find('div', attrs={'class':'vk_ans vk_bk curtgt'})
    data=d.find('span', attrs={'style':'word-break:break-all'}).string
    rate=float(ast.literal_eval(data))
    print "google rate usd-brl %f"%rate
    return rate

def getRealValue(url, pos, fx):
    data=ast.literal_eval(fetch_data(url))
    qty=cash=net=total=0
    fee=.993 #Brazil Execution Fee
    fx_spread=0.01 #fx spread by bank
    for ask in data["asks"]:
        qt=ask[1]
        pr=ask[0]
        if qt+qty>pos:
            qt=pos-qty
        qty+=qt
        net=qt*pr*fee
        total+=net

    print "btc-fees(%.2f) in BR - %.2f"%(qty,total)
    to_bank=total-2.99-(0.0199*total)
    transfer_us=to_bank-115-0.011*to_bank
    #fx=3.27
    in_us=transfer_us/fx-(fx*fx_spread)
    coinbase=in_us-0.0149*in_us
    print "total:%.2f, in_itau:%.2f, transfer:%.2f, in_us:%.2f, coinbase:%.2f"%(total, to_bank, transfer_us, in_us, coinbase)
    return coinbase



#Get kraken Data
(kraken_btc, bch) = getKrakenData(kraken_url)
print "kraken BTC - %.2f"%(kraken_btc)
print "kraken BCH - %.2f"%(bch)

#Get Coinbase Data
(btc_to_usd, btc_to_brl, usd_to_brl, eth_to_usd, ltc_to_usd)=getCoinbaseData(coin_url)

#get bitcoin from mbc
mbc_rate=getMBitcoinData(mbc_url)

#get litecoin data
ltc_rate=getMBitcoinData(ltc_url)

#get bcash data
bch_rate=getMBitcoinData(bch_url)

pos=1
rate=usd_to_brl
arbitrage=mbc_rate-btc_to_brl
ltc_arb=(ltc_rate/rate)-ltc_to_usd
bch_arb=(bch_rate/rate)-bch
real_value=getRealValue(order_book, pos, rate)
real_arbitrage=real_value-pos*btc_to_usd

print ' --- Bitcoin'
print'......... arbitrage (br-us):%.2f BRL, %.2f USD'%(arbitrage, arbitrage/rate)
print'......... arbitrage ltc:%.2f USD, bch:%.2f'%(ltc_arb, bch_arb)
print "Opportunity %f btc: %.2fBRL, %.2f USD"%(pos, arbitrage*pos, arbitrage/rate*pos)
print 'Arbitrage ratio (arb/mbc):%.2f%%(btc), %.2f%%(ltc), %.2f%%(bch)'%(arbitrage/mbc_rate*100, ltc_arb/ltc_rate*100, bch_arb/bch_rate*100)
print "After fees %.2f btc: %.2f USD, %.2f USD"%(pos, real_value, real_arbitrage)
print "Arbitrage ratio (arb/mbc):%.2f%%"%(real_arbitrage/btc_to_usd*100)
#print ' for position:%f , %f BRL, %f USD,  (%f bitcoins)'%(pos, arbitrage*pos, arbitrage/rate*pos, arbitrage/rate*pos/btc_to_usd)

#bitcoin position
pos=1.875
eth_pos=8
btc_pr=2660.6027
eth_pr=252.1787

eth_pnl=(eth_pos*eth_to_usd)-(eth_pos*eth_pr)
btc_pnl=(pos*btc_to_usd)-(pos*btc_pr)
bch_pnl=pos*bch
print ""
print " BTC=%.2f, ETH=%.2f, BCH=%.2f, ltc=%.2f, "%(btc_to_usd, eth_to_usd, bch, ltc_to_usd)
print " BTC=%.2f, ETH=%.2f, BCH=%.2f, Total=%.2f"%(pos*btc_to_usd, eth_pos*eth_to_usd, pos*bch, (pos*btc_to_usd+ eth_pos*eth_to_usd+ pos*bch))
print " Partial pnl: %.2f(btc), %.2f(eth), %.2f(bch): Total:%.2f"%(btc_pnl, eth_pnl, bch_pnl, eth_pnl+btc_pnl+bch_pnl)




import time 
from datetime import datetime
import urllib2
import ast  
import mechanize 
from bs4  import BeautifulSoup 
import thread

t1=time.time() 

mbc_historical="https://www.mercadobitcoin.net/api/trades/1420070400/"
mbc_url="http://www.mercadobitcoin.com.br/api/ticker/" 
ltc_url="http://www.mercadobitcoin.com.br/api/ticker_litecoin/"
coin_url="https://coinbase.com/api/v1/currencies/exchange_rates" 
spot_url="https://coinbase.com/api/v1/prices/spot_rate"
exch_rate="http://rate-exchange.appspot.com/currency?from=USD&to=BRL" 
exch_rate="https://www.google.com/search?q=1+usd+in+brl" 
order_book="http://www.mercadobitcoin.com.br/api/orderbook/" 
#br.set_headers = [(':authority','www.google.com'),(':method','GET'),(':path','/search?q=1+usd+in+brl'),(':scheme','https'),('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('accept-encoding','gzip, deflate, sdch, br'),('accept-language','en-US,en;q=0.8,pt-BR;q=0.6,pt;q=0.4,zh;q=0.2'),('avail-dictionary','ghM1Vvtn'),('cookie','OGPC=765334528-4:278279168-2:560575488-4:976493568-6:946258944-4:908000256-6:864812032-6:391792640-8:193170432-3:699960320-1:448059392-2:1049715712-1:412595200-6:811773952-4:531737600-2:604273664-4:928362496-4:355367936-1:783732736-4:; _ga=GA1.1.1691645100.1493469457; OTZ=3877991_72_76_104100_72_446760; SID=yQSWvHZppeURE-psndA---tKtmp2oy3KwWClkrI36Zf5mv-7XTcgsokxcaNZ9hcNLVF27A.; HSID=AcHvyNI989otpJaUM; SSID=A3rLznVkBAeyv2-pJ; APISID=2-sinx15wzLGBQ5z/Ai5QOIN4CSde2B9JC; SAPISID=s_3XPrvbo_XW4W9g/A7igZuckMp6orZzQu; NID=105=Q7s7Zc3PaRnLLPkyraT2FI5sv3fJDE8Bzs8aSs4t20W10F9seEVwfOvHmZWSCVJghA8i314-TShk9qF3VrikcN9FO67T1tEjUkjw-gViHD_G1HAmsXmtOVhdC0jb-rNtrU2loqpwbzXE4HsQ9TbAoi1SRN4Byu-xAcasX8kH3GAYORsXa4y7uUAyHawkjxBh_NL0pCCqPpbgaHQ4TIeMeAN_kmtq4SX0NdPvblgYbTAHHV6vjv0MJtFjNKWUVRnrZLq0Zj2IbQop8qlexaUs2fPK5Ou4OgCK2CLZTSIFPbRM6JbFWnAMJ5UFqBx8S9mmAjBqDwYzbg0; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTQ5NzA5Mjc3MjIwMjAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6NDEwMzU3NjE1IGxvbmdpdHVkZV9lNzotNzM2ODIzNDY4fSByYWRpdXM6NTIwODA=;DV=k2LIO6TzJx9HINXQWGYfNuAqQncbydX9wZ9baRZHcAAAAEBTPR0m8SveeAEAADhOCcNpe3xCXwAAAA'),('upgrade-insecure-requests','1'),('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]

def fetch_data(url):
    br= mechanize.Browser() 
    br.set_handle_equiv(False) 
    br.set_handle_robots (False) 
    #br.set_headers = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'), ('Accept', '*/*')]
    br.set_headers = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'), ('Accept', '*/*')] #, ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), ('Accept-Encoding', 'none'), ('Accept-Language', 'en-US,en;q=0.8'), ('Connection', 'keep-alive')]
    resultado=[] 
    print '-'*10
    print "fetching "+url 
    res=br.open (url) 
    data=res.read() 
    return data




def getCoinbaseData(url):   
    data=fetch_data(url)
    coin=ast.literal_eval(data) 
    idx=('btc_to_usd', 'btc_to_brl', 'usd_to_brl','eth_to_usd') 
    for i in idx:
        print "%s - %s"%(i, coin[i])

    return (float (coin['btc_to_usd']), float (coin["btc_to_brl"]), float (coin["usd_to_brl"]), float (coin["eth_to_usd"]))

def getMBitcoinData(url):
    data=fetch_data (url)
    return ast.literal_eval(data)["ticker"]["last"] 


def applyRates(btc_to_usd, btc_to_brl, usd_to_brl, pos):
    #btc execution fee = 0.7 forced, 0.3 being executed
    arbitrage = pos 

    #btc_cash out 2.99


def getMBOrderBook(url):
    return ast.literal_eval(fetch_data(url))

def getValueForPosition(order_book,pos,fx):
    data=order_book   
    qty=cash=net=total=0
    mb_ex_fee=.993 #Brazil Execution Fee
    fx_spread=0.01 #fx spread by the bank

    for ask in data["asks"]:
        qt=ask[1]
        pr=ask[0]
        if qt+qty>pos:
            qt=pos-qty
        qty+=qt
        net=qt*pr*mb_ex_fee
        total+=net
        #print "qty:%f, pr:%f, g:%f, net:%f total:(%f,%f)"%(qt,pr,pr*qt,net,qty,total)
    #print "%f\t%f"%(qty,total)
    to_bank = total- 2.99-(0.0199*total) #mb cash fee R$2.99 + 1.99%
    transfer_us = to_bank - 115-0.011 * to_bank
    in_us=transfer_us/(fx+(fx*fx_spread))
    coinbase=in_us-0.0149*in_us
    #print "total:%f, in_itau:%f, transfer:%f, in_us:%f, coin:%f/(%f)"%(total, to_bank, transfer_us, in_us, coinbase, coinbase/pos)

    return coinbase



def run_it_all():
    #Get Coinbase Data
    (btc_to_usd, btc_to_brl, usd_to_brl, eth_to_usd)=getCoinbaseData(coin_url) 

    #get bitcoin from mbc
    mbc_rate=getMBitcoinData(mbc_url)

    #get litecoin data
    #ltc_rate=getMBitcoinData(ltc_url)

    print "mbc_rate:%f"%(mbc_rate)
    pos=1.875
    rate=usd_to_brl
    arbitrage=mbc_rate-btc_to_brl

    mb_ob=getMBOrderBook(order_book)

    real_value=getValueForPosition(mb_ob, pos, rate)
    real_arbitrage=real_value-pos*btc_to_usd

    print ' --- Bitcoin'
    print'......... arbitrage (br-us):%f BRL, %f USD'%(arbitrage, arbitrage/rate)
    print 'Arbitrage ratio (arb/mbc):%f%%'%(arbitrage/mbc_rate*100)
    print "Opportunity %f btc: %fBRL, %f USD"%(pos, arbitrage*pos, arbitrage/rate*pos)
    print "After fees %f btc: %f USD, %f USD"%(pos, real_value, real_arbitrage)
    print "Arbitrage ratio (arb/mbc):%f%%"%(real_arbitrage/btc_to_usd*100)
    #print ' for position:%f , %f BRL, %f USD,  (%f bitcoins)'%(pos, arbitrage*pos, arbitrage/rate*pos, arbitrage/rate*pos/btc_to_usd)
    #bitcoin position
    pos=1.879
    eth_pos=8
    btc_pr=2661
    eth_pr=252.18


    #print"%s - %s"%(i, coin(i)) btc. to usd=float(coin ("btc. to usd')

    eth_pnl=(eth_pos*eth_to_usd)-(eth_pos*eth_pr)
    btc_pnl=(pos*btc_to_usd)-(pos*btc_pr)
    print 'PNL: %f (btc), %f (eth), Total:%f usd'%(btc_pnl, eth_pnl, btc_pnl+eth_pnl)

    with open("btc.out","a") as fh:
        fh.write("\n%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f"%(str(datetime.now()),btc_to_usd, btc_to_brl, mbc_rate, mbc_rate/rate, rate, arbitrage, arbitrage, rate, pos, arbitrage*pos, arbitrage/rate*pos, real_value, real_arbitrage, btc_pnl, eth_pnl, btc_pnl+eth_pnl))

    fh.close 

while True:
    run_it_all()
    time.sleep(30)


# print "*"*10
# print "----+++-------+++--------+++"
# print "Pos\tBTC(US)\tBr\tFX\tARB\t+Fee\tPNL"

# po=[1,1.875]
# for p in po:
#     rv=getValueForPosition(mb_ob,p,rate)
#     ra=rv - pos*btc_to_usd
#     print "%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t"%(p,p*btc_to_usd,p*mbc_rate,rate,p*(mbc_rate-btc_to_brl),rv-p*btc_to_usd,0)

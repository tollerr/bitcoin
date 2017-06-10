
import time 
import urllib2
import ast  
import mechanize 
from bs4  import BeautifulSoup 

t1=time.time() 

mbc_historical="https://www.mercadobitcoin.net/api/trades/1420070400/"
mbc_url="http://www.mercadobitcoin.com.br/api/ticker/" 
ltc_url="http://www.mercadobitcoin.com.br/api/ticker_litecoin/"
coin_url="https://coinbase.com/api/v1/currencies/exchange_rates" 
spot_url="https://coinbase.com/api/v1/prices/spot_rate"
exch_rate="http://rate-exchange.appspot.com/currency?from=USD&to=BRL" 
exch_rate="https://www.google.com/search?q=1+usd+in+brl" 
br= mechanize.Browser() 
br.set_handle_equiv(False) 
br.set_handle_robots (False) 
#br.set_headers = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'), ('Accept', '*/*')]
br.set_headers = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'), ('Accept', '*/*')] #, ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), ('Accept-Encoding', 'none'), ('Accept-Language', 'en-US,en;q=0.8'), ('Connection', 'keep-alive')]

#br.set_headers = [(':authority','www.google.com'),(':method','GET'),(':path','/search?q=1+usd+in+brl'),(':scheme','https'),('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('accept-encoding','gzip, deflate, sdch, br'),('accept-language','en-US,en;q=0.8,pt-BR;q=0.6,pt;q=0.4,zh;q=0.2'),('avail-dictionary','ghM1Vvtn'),('cookie','OGPC=765334528-4:278279168-2:560575488-4:976493568-6:946258944-4:908000256-6:864812032-6:391792640-8:193170432-3:699960320-1:448059392-2:1049715712-1:412595200-6:811773952-4:531737600-2:604273664-4:928362496-4:355367936-1:783732736-4:; _ga=GA1.1.1691645100.1493469457; OTZ=3877991_72_76_104100_72_446760; SID=yQSWvHZppeURE-psndA---tKtmp2oy3KwWClkrI36Zf5mv-7XTcgsokxcaNZ9hcNLVF27A.; HSID=AcHvyNI989otpJaUM; SSID=A3rLznVkBAeyv2-pJ; APISID=2-sinx15wzLGBQ5z/Ai5QOIN4CSde2B9JC; SAPISID=s_3XPrvbo_XW4W9g/A7igZuckMp6orZzQu; NID=105=Q7s7Zc3PaRnLLPkyraT2FI5sv3fJDE8Bzs8aSs4t20W10F9seEVwfOvHmZWSCVJghA8i314-TShk9qF3VrikcN9FO67T1tEjUkjw-gViHD_G1HAmsXmtOVhdC0jb-rNtrU2loqpwbzXE4HsQ9TbAoi1SRN4Byu-xAcasX8kH3GAYORsXa4y7uUAyHawkjxBh_NL0pCCqPpbgaHQ4TIeMeAN_kmtq4SX0NdPvblgYbTAHHV6vjv0MJtFjNKWUVRnrZLq0Zj2IbQop8qlexaUs2fPK5Ou4OgCK2CLZTSIFPbRM6JbFWnAMJ5UFqBx8S9mmAjBqDwYzbg0; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTQ5NzA5Mjc3MjIwMjAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6NDEwMzU3NjE1IGxvbmdpdHVkZV9lNzotNzM2ODIzNDY4fSByYWRpdXM6NTIwODA=;DV=k2LIO6TzJx9HINXQWGYfNuAqQncbydX9wZ9baRZHcAAAAEBTPR0m8SveeAEAADhOCcNpe3xCXwAAAA'),('upgrade-insecure-requests','1'),('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]









resultado=[] 
print '-'*100 
print "fetching "+coin_url 
res=br.open (coin_url) 
data=res.read() 
coin=ast.literal_eval(data) 
idx=('btc_to_usd', 'btc_to_brl', 'usd_to_brl','eth_to_usd') 
for i in idx:
    print "%s - %s"%(i, coin[i])
btc_to_usd = float (coin['btc_to_usd'])
btc_to_brl = float (coin["btc_to_brl"])
usd_to_brl = float (coin["usd_to_brl"]) 
print'-'*100 
print "fetching "+mbc_url 
res=br.open(mbc_url) 
data=res.read() 
mbc=ast.literal_eval(data)["ticker"] 
mbc_rate=mbc["last"]

#print mbc print"btc-mbc- %s"%(mbc"last") print'-' 100
print "fetching "+ltc_url

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]


res=br.open(ltc_url)
data=res.read()
ltc=ast.literal_eval(data)["ticker"]
ltc_rate=ltc['last'] 
print "ltc-mbc- %s"%(ltc["last"]) 

print '-' * 100 
print "fetching: "+exch_rate
#content=br.open(exch_rate).read().decode('UTF-8')


#print content
#soup=BeautifulSoup(content) 
#d=soup.find('div', attrs= {'class':'vk_ans vk_bk curtgt'}) 
#data=d.find ('span', attrs={'style':'word-break:break-all'}).string 
#rate=float(ast.literal_eval(data))
#print"google rate usd->brl %f"%rate
rate=usd_to_brl
arbitrage=mbc_rate-btc_to_brl

print'......... arbitrage (br-us):%f BRL, %f USD'%(arbitrage, arbitrage/rate)
print 'Arbitrage ratio (arb/mbc):%f%%'%(arbitrage/mbc["last"]*100)

#print"%s - %s"%(i, coin(i)) btc. to usd=float(coin ("btc. to usd')

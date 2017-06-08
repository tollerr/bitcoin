
#!/ms/dist/python/PROJ/core/2.7.3/bin/python 
import time 
import urlib2 
import ast 
import ms.version 

import mechanize 
from BeautifulSoup  import BeautifulSoup 
t1=time.time() 
mbc_url="http://www.mercadobitcoin.com.br/api/ticker/" 
itc_url="http://www.mercadobitcoin.com.br/api/ticker_litecoin/"
coin_url="https://coinbase.com/api/v1/currencies/exchange_rates" 
spot_url="https://coinbase.com/api/v1/prices/spot_rate"
ex"ch_rate="http://rate-exchange.appspot.com/currency?from=USD&to=BRL' 
exch_rate="https://www.google.com/search?q=1+usd+in+brl" 
br= mechanize.Browser() 
br.set_handle_equiv(False) 
br.set_handle_robots (False) 
br.ddheaders = ("User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)"), ("Accept', '*/*') 
#br.set_proxies("http":"fIbagw01:8080","https":"flbcgw01:8080") r
esultado=[]) 
print '-' 100 
print "fetching"+coin url 
res=br.open (coin_url) 
data=res.read() 
coin-ast.literal_eval(data) 
idx=['btc_to_used', 'btc_to_bri', 'used_to_brl') 
for in idx:
    bitc. to bri=float (coin ("btc. to bri")) usd to bri=float(coin"usd to bri") print'-' 100 print "fetching"+mbo url res=br.open (mbcurl) data=res.read() mbc=ast. literal eval (data) ("ticker) mbc rate=mbc"last")
#print mbc print"btc-mbc- %s"%(mbc"last") print'-' 100
print "fetching"+itc url res=br.open (tc uri) data=res.read() Itc=ast. literal eval (data) ("ticker") to rate=|tc'last") print "itc-mbc- %s"%(itc."last") print'-' 100 print "fetching"+exch rate Content=br.open (exch_rate).read() soup=BeautifulSoup(Content) d=soup.find('div', attrs= {'class":'vk ans vk_bk Curtigt''}) data=d.find ('span, attrs='style':'word-break:break-all").string rate=float(ast. literal eval(data)) print"google rate usd->bri%f"%rate
arbitrage=mbc rate-btic to bri arbitrage2=
print'......... arbitrage (br-us):%f BRL, %f USD'%(arbitrage, arbitrage/rate)
print 'Arbitrage ratio (arb/mbc):%f%%"%(arbitrage/mbc("last")*100)

print"%s - %s"%(i, coin(i)) btc. to usd=float(coin ("btc. to usd')

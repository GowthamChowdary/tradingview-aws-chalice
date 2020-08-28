# tradingview-aws-chalice
serverless trading with aws chalice from tradingview web-hook alerts
# what it does for now?
place buy/sell market orders automatically on binance from tradingview webhook alerts
# how to use?
install chalice, then do a "chalice new-project "name""(will create a chalice project named "name") open the app.py and replace it with the app.py in this repository.
replace the api_key and api_secret with yours
give it a symbol(ETHBTC/BTCUSD etc..) and quantity
use "chalice local" to deploy it locally, use "chalice deploy" to deploy it to the cloud.
deploy on chalice, give tradingview the aws chalice webhook. 
The tradingview alert has to be in a json format for eg: {"order":buy}
# ADDING SOON.....
more exchanges,
limit orders,
(well, make it more effificent...)


use it at your own risk, this is just me documenting my projects.

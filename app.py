from chalice import Chalice
from binance.client import Client
client = Client("api_key", "api_secret")
app = Chalice(app_name='#name of the chalice app')
@app.route('/order',methods=['POST'])
def index():
    request=app.current_request
    msg=request.json_body
    if msg["order"]=="buy":
        return(client.order_market_buy(symbol='#symbol',quantity=#quantity))
    elif msg["order"]=="sell":
        return(client.order_market_sell(symbol='#symbol',quantity=#quantity)) 


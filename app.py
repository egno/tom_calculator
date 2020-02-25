from aiohttp import web
from decimal import Decimal as D

from tom_calc import calculate


async def main_form(request):
    quantity = D(request.query.get('quantity', '1'))
    price = D(request.query.get('price', '0'))
    state = request.query.get('state', 'UT')

    amount = calculate(quantity, price, state)

    html = f'''<form action="/" method="get" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

    <label for="quantity">Quantity</label>
    <input id="quantity" name="quantity" value="{quantity}" />
    <label for="price">Price</label>
    <input id="price" name="price" value="{price}"/>
    <label for="state">State</label>
    <input id="state" name="state" value="{state}"/>

    <input type="submit" value="calc"/>
</form>
<br>
Amount: {str(amount)}'''
    return web.Response(text=html, content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', main_form)])

web.run_app(app)

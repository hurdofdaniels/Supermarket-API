# Supermarket API
This is a API that collects data from all the New Zealand supermarkets, It's built in python 3.7.3.
I'm making this product because in the future I'm going to make a shopping list that grabs the best price for the same item.

------

## How it works?
Some supermarkets have API and some call a database onload, so it will use Beautiful Soup to scrap the database websites and it will use the built-in requests library to call the API.

------

## Notes:
### Countdown:
* Type: API
* URL: [https://shop.countdown.co.nz/api/v1/products?target=search&search=sauce&search_type=ShopOnline](https://shop.countdown.co.nz/api/v1/products?target=search&search=sauce&search_type=ShopOnline)
 * Params:
> Target: search (Default)

> Search: Item (Sauce is currently searched)

> Search_Type: ShopOnline (Default)
* Online Shop URL: [https://shop.countdown.co.nz/](https://shop.countdown.co.nz/)

### Pak N Save:
* Type: Database
* URL: [https://www.paknsaveonline.co.nz/Search?q=sauce](https://www.paknsaveonline.co.nz/Search?q=sauce)
 * Params:
 
> Q (Query): Item (Sauce is currently searched)

* Online Shop URL: [https://www.paknsaveonline.co.nz/](https://www.paknsaveonline.co.nz/)

### New World:
* Type: Database
* URL: [https://www.ishopnewworld.co.nz/Search?q=sauce](https://www.ishopnewworld.co.nz/Search?q=sauce)
 * Params:
 
> Q (Query): Item (Sauce is currently searched)

* Online Shop URL: [https://www.ishopnewworld.co.nz/](https://www.ishopnewworld.co.nz/)

### FreshChoice:
* Type: Database
* URL: [https://barrington.store.freshchoice.co.nz/search?q=sauce](https://barrington.store.freshchoice.co.nz/search?q=sauce)
 * Params:

> The store (Not really a param): The store location (Barrington is currently chosen)

> Q (Query): Item (Sauce is currently searched)

* Online Shop URL: [https://barrington.store.freshchoice.co.nz/](https://barrington.store.freshchoice.co.nz/)

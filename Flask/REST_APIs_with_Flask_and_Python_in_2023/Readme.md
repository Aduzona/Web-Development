status=200 means ok, everything went well,
status= 201 means that I have accepted the that and create the store.

## Create Stores in our REST API


`app.py`
```python
from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {"name": "Chair",
             "price": 15.99
             }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
```

```shell
flask run
```
POST: http://127.0.0.1:5000/store

```json
{
	"name":"My Store 2"
}
```

POST: http://127.0.0.1:5000/store/My Store 2/item

```json
{
	"name": "Laptop",
	"price": 17.99
}
```
GET: http://127.0.0.1:5000/store
```json
{
	"stores": [
		{
			"items": [
				{
					"name": "Chair",
					"price": 15.99
				},
				{
					"name": "Table",
					"price": 17.99
				}
			],
			"name": "My Store"
		},
		{
			"items": [
				{
					"name": "Laptop",
					"price": 17.99
				}
			],
			"name": "My Store 2"
		}
	]
}
```

## Get a specific store and its Items

store/<name>: Gets the stores
GET: http://127.0.0.1:5000/store/My Store

```python
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404
```
Returns:
```json
{
	"items": [
		{
			"name": "Chair",
			"price": 15.99
		}
	],
	"name": "My Store"
}
```



store/<name>/item: Gets just the store item, thus items of a specific store.
GET: http://127.0.0.1:5000/store/My Store/item
```python
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
```
```json
{
	"items": [
		{
			"name": "Chair",
			"price": 15.99
		}
	]
}
```

## Docker

[How to run Docker container](https://rest-apis-flask.teclado.com/docs/docker_intro/run_docker_container/)

```shell
docker build -t rest-apis-flask-python .
docker run -d -p 5005:5000 rest-apis-flask-python
```

send a request: `http://127.0.0.1:5005/store/My Store`
Returned:
```json
{
	"items": [
		{
			"name": "Chair",
			"price": 15.99
		}
	],
	"name": "My Store"
}
```

## Flask-Smorest for More Efficient Development

Go through [Data model improvements for our APIs](https://rest-apis-flask.teclado.com/docs/flask_smorest/data_model_improvements/)
for better understanding.
We are going to change how we store data so that we can reference items and stores by there unique
identifiers instead of by their names.

This helps us to simplify our code. 
I used universally unique Identifiers(uuid) because no database yet.

```python
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store
```
This syntax `**store_data` is for parsing keyword arguments to a constructor.
This will unpack the values in the `store_data` and include them in this new dictionary
`{**store_data, "id": store_id}`
# References

1. [Rest_API_FLASK](https://rest-apis-flask.teclado.com/docs/course_intro/)
2. [Code Changes for Data model improvements for our APIs](https://diff-store.com/diff/05_flask_smorest__02_data_model_improvements)
3. 
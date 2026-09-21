# Notes

## FastAPI Intro

* **FastAPI Overview**: FastAPI is a web framework designed for creating APIs with high throughput, making it ideal for data and machine learning transactions. It uses Python annotations and type hints to simplify coding.

* **Key Features**:

    * **Performance**: One of the fastest Python frameworks available.
    * **Ease of Use**: Low code and easy to learn.
    * **Robustness**: Produces production-ready code with automatic interactive documentation.
    * **Standards-Based**: Compatible with OpenAPI and JSON Schema.

* **Comparison with Other Frameworks**: Unlike Flask and Django, FastAPI is specifically designed for APIs and does not include a built-in ORM, which can enhance API performance.

---

## HTTP Status Code 204 No Content

204 No Content  
It can be used in case of DELETE endpoint, when a resource is deleted successfully,  
and we have nothing to return in the response.  

---

## FastAPI CRUD Example

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# define model Item
class Item(BaseModel):
    name: str
    quantity: Optional[int] = 0

app = FastAPI()

items = {}


@app.post("/items")
def create(item: Item):
    name = item.name
    if name in items:
        raise HTTPException(status_code=409, detail="Item exists")
    items[name] = item
    return {"message": f"Added {name} to items."}
  
@app.get("/items")
def read(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]  
  
@app.put("/items")
def update(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[name] = item
    return {"message": f"Updated {name}."}
  
@app.delete("/items")
def delete(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[name]
    return {"message": f"Deleted {name}."}
```

Test using the following `curl` commands in terminal:  

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock"}' \
  http://localhost:8000/items

curl http://localhost:8000/items?name=rock

curl -X PUT \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock", "quantity": 100}' \
  http://localhost:8000/items

curl -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock"}' \
  http://localhost:8000/items

curl http://localhost:8000/items?name=rock
```

---

## System Tests vs Functional Tests

**System Tests**: These tests focus on validating isolated functionalities, such as individual endpoints. You used tools like pytest and TestClient to perform these tests.

**Functional Tests**: These tests ensure that multiple endpoints work together as expected, covering the entire workflow of your application. You wrote scripts using requests to perform these tests.

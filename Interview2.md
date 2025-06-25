
# API Basics – Questions and Answers

## ❓ What is an API?

**Answer**:  
API stands for **Application Programming Interface**. It is a set of rules and protocols that allow different software applications to communicate with each other.

---

## ❓ What are API Error Codes?

**Answer**:  
API error codes are standardized numeric codes that indicate the **status or result** of an API request. These help the client understand whether a request was successful or if an error occurred.

### Common HTTP Status Codes:

| Code | Meaning                   | Description                                              |
|------|---------------------------|----------------------------------------------------------|
| 200  | OK                        | Request succeeded.                                       |
| 201  | Created                   | Resource created successfully.                           |
| 204  | No Content                | Request successful but no content returned.              |
| 400  | Bad Request               | The request is invalid or cannot be processed.           |
| 401  | Unauthorized              | Authentication is required or failed.                   |
| 403  | Forbidden                 | User does not have permission.                          |
| 404  | Not Found                 | The requested resource doesn’t exist.                   |
| 405  | Method Not Allowed        | The HTTP method is not supported for this route.         |
| 409  | Conflict                  | Conflict with the current state of the resource.         |
| 422  | Unprocessable Entity      | Validation error (often in FastAPI).                     |
| 500  | Internal Server Error     | A generic server error.                                  |
| 502  | Bad Gateway               | Invalid response from upstream server.                   |
| 503  | Service Unavailable       | Server is temporarily overloaded or down.                |

---

## ❓ What are the types of requests in APIs and FastAPI?

**Answer**:  
Here are the most common types of HTTP requests:

| Method   | Purpose                         | FastAPI Example                    | Use Case                           |
|----------|----------------------------------|------------------------------------|------------------------------------|
| `GET`    | Retrieve data                    | `@app.get("/items/")`             | Fetch an item or list              |
| `POST`   | Create new data                  | `@app.post("/items/")`            | Create a new record                |
| `PUT`    | Update data completely           | `@app.put("/items/{id}")`         | Replace a record                   |
| `PATCH`  | Update data partially            | `@app.patch("/items/{id}")`       | Modify part of a record            |
| `DELETE` | Delete data                      | `@app.delete("/items/{id}")`      | Delete a record                    |
| `OPTIONS`| Get communication options        | *(rarely used manually)*          | Discover allowed methods           |
| `HEAD`   | Same as GET but without body     | *(rarely used manually)*          | Check existence without response body |

---

## ❓ In which API request is data visible in the URL?

**Answer**:  
Data is visible in the URL when using a **GET request**, and sometimes in `DELETE`, `HEAD`, or `OPTIONS` if query parameters are used.

### Example:
```http
GET /search?query=shoes&category=men
````

📌 This shows up as:
`https://example.com/search?query=shoes&category=men`

### Summary:

| Method | Data in URL? | Data Location    | Safe for sensitive data? |
| ------ | ------------ | ---------------- | ------------------------ |
| GET    | ✅ Yes        | URL (query/path) | ❌ No                     |
| POST   | ❌ No         | Request Body     | ✅ Yes                    |
| PUT    | ❌ No         | Request Body     | ✅ Yes                    |
| PATCH  | ❌ No         | Request Body     | ✅ Yes                    |
| DELETE | ⚠️ Sometimes | URL (path param) | ❌ No                     |

---


A


# FastAPI Developer Interview Questions and Answers

---

## ❓ What is FastAPI?

**Answer**:  
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on **standard Python type hints**. It is built on top of **Starlette** and **Pydantic**.

---

## ❓ What are the key features of FastAPI?

**Answer**:
- High performance (comparable to NodeJS and Go)
- Automatic data validation using Pydantic
- Built-in API documentation using Swagger and ReDoc
- Type hint support for better development experience
- Dependency Injection support
- Asynchronous support using `async/await`

---

## ❓ How is FastAPI different from Flask?

**Answer**:

| Feature          | Flask               | FastAPI                            |
|------------------|---------------------|------------------------------------|
| Performance      | Slower              | Faster (async & Starlette-based)   |
| Type Hints       | Limited             | Full support                       |
| Validation       | Manual              | Automatic with Pydantic            |
| API Docs         | Manual/OpenAPI lib  | Built-in Swagger/ReDoc             |
| Async Support    | Limited             | Full `async/await` support         |

---

## ❓ What is Pydantic and how is it used in FastAPI?

**Answer**:  
Pydantic is a data validation and settings management library using Python type annotations. In FastAPI, it's used to define request and response schemas.

### Example:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
````

---

## ❓ How do you handle form data and file uploads in FastAPI?

**Answer**:

* Use `Form()` for form fields
* Use `File()` for file uploads

### Example:

```python
from fastapi import Form, File, UploadFile

@app.post("/upload/")
def upload_file(name: str = Form(...), file: UploadFile = File(...)):
    return {"filename": file.filename}
```

---

## ❓ What are path parameters and query parameters in FastAPI?

**Answer**:

* **Path parameters** are part of the URL path.
* **Query parameters** are optional parameters provided after `?`.

### Example:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

---

## ❓ What is the use of `Depends()` in FastAPI?

**Answer**:
`Depends()` is used for **dependency injection** — letting you define reusable functions for things like authentication, DB sessions, etc.

### Example:

```python
from fastapi import Depends

def get_token_header(token: str = Header(...)):
    if token != "secret":
        raise HTTPException(status_code=400, detail="Invalid Token")

@app.get("/protected/")
def read_protected_data(dep=Depends(get_token_header)):
    return {"message": "Secure data"}
```

---

## ❓ How to create a response model in FastAPI?

**Answer**:
Use `response_model` parameter in route decorator to define the output format.

### Example:

```python
class ItemOut(BaseModel):
    name: str

@app.get("/items/", response_model=ItemOut)
def get_item():
    return {"name": "Book", "price": 100}  # price is omitted in response
```

---

## ❓ How do you handle exceptions in FastAPI?

**Answer**:
Use `HTTPException` or custom exception handlers.

### Example:

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
```

---

## ❓ How do you connect FastAPI with a database?

**Answer**:
Common approach:

* Use **SQLAlchemy** or **Tortoise ORM**
* Create DB session dependency with `Depends()`

---

## ❓ How do you run a FastAPI application?

**Answer**:
Using **uvicorn**:

```bash
uvicorn main:app --reload
```

---

## ❓ What is OpenAPI and how does FastAPI use it?

**Answer**:
FastAPI auto-generates API docs using the OpenAPI standard. You get:

* Swagger UI: `/docs`
* ReDoc: `/redoc`

---

## ❓ How do you test FastAPI routes?

**Answer**:
Use `TestClient` from `fastapi.testclient`.

### Example:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```

---

## ❓ What is middleware in FastAPI?

**Answer**:
Middleware is code that runs before and after each request.

### Example:

```python
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    return response
```

---

## ❓ How do you handle CORS in FastAPI?

**Answer**:
Use the `CORSMiddleware` from `starlette.middleware.cors`.

### Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ❓ What is the difference between `PUT` and `PATCH`?

**Answer**:

* `PUT`: Full update (replaces the entire resource).
* `PATCH`: Partial update (modifies specific fields).

---

## ❓ Can you make async API calls in FastAPI?

**Answer**:
Yes, FastAPI supports async/await natively.

```python
@app.get("/async-task")
async def async_task():
    await some_async_function()
    return {"status": "done"}
```

---

## ❓ What tools can you use to document and test FastAPI APIs?

**Answer**:

* Swagger UI (`/docs`)
* ReDoc (`/redoc`)
* Postman (manual testing)
* Pytest (unit testing)

---

## ❓ How do you secure APIs in FastAPI?

**Answer**:

* Use `Depends()` for auth
* Implement OAuth2/JWT
* Use `HTTPS`, CORS, headers

---

## ❓ How can you create background tasks in FastAPI?

**Answer**:
Use the `BackgroundTasks` class.

### Example:

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message)

@app.post("/log/")
def log_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Logged"}
```

---


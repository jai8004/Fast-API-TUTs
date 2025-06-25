## 📘 FastAPI Interview Questions & Answers for Freshers (with Project-Based Context)

This list covers important FastAPI interview questions (with explanations and answers), tailored around the CRUD + Auth project you built.

---

### 1. **What is FastAPI? How is it different from Flask or Django?**

**Answer:** FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Why it matters:**

* Uses Pydantic for data validation
* Async support out of the box
* Automatic Swagger/OpenAPI docs
* Faster performance than Flask

---

### 2. **What are Pydantic models used for in FastAPI?**

**Answer:** Pydantic models are used for request validation and response serialization. In your project:

* `UserCreate` validates input for user registration.
* `UserOut` ensures passwords aren’t returned in responses.

**Why it matters:** Keeps your data clean and safe from user input errors.

---

### 3. **What is SQLAlchemy and how is it used in FastAPI?**

**Answer:** SQLAlchemy is an ORM (Object Relational Mapper). It maps Python classes to DB tables.

In the project:

* `User` model in `models.py` is a SQLAlchemy class mapped to the `users` table.
* You use `SessionLocal` from `database.py` to run DB operations.

---

### 4. **How is the database connected in FastAPI?**

**Answer:**

* Use `create_engine()` to connect to SQLite in `database.py`
* Use `SessionLocal()` to handle DB sessions
* Use `Base.metadata.create_all()` to create tables

---

### 5. **What is dependency injection in FastAPI?**

**Answer:** It allows you to define reusable components (like DB sessions) and inject them into routes.

Example:

```python
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
```

---

### 6. **How does FastAPI handle authentication?**

**Answer:** FastAPI supports OAuth2 and JWT-based auth. In the project:

* Login endpoint verifies credentials
* Returns a JWT access token
* Uses `python-jose` to generate and decode tokens

---

### 7. **How do you hash and verify passwords in FastAPI?**

**Answer:**

* Use `passlib` with `bcrypt`
* `hash_password()` to store securely
* `verify_password()` during login

---

### 8. **What is JWT and why is it used?**

**Answer:** JWT (JSON Web Token) is a compact way to securely transmit user identity.

In the project:

* Issued upon login
* Stored in frontend/localstorage and sent in header as `Authorization: Bearer <token>`

---

### 9. **How are tables created in SQLAlchemy?**

**Answer:**

* Define model class with `Base` as parent
* Call `Base.metadata.create_all(bind=engine)` to create tables

---

### 10. **What does `@router.post()` mean in FastAPI?**

**Answer:** It's used to define a POST endpoint in a router module.

In `users.py`, this decorates the function that creates a new user.

---

### 11. **How do you serve docs in FastAPI?**

**Answer:** Automatically at:

* Swagger: `http://localhost:8000/docs`
* Redoc: `http://localhost:8000/redoc`

---

### 12. **How do you handle errors or status codes in FastAPI?**

**Answer:**

```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="User not found")
```

Used in `get_user()` and `delete_user()` when the ID doesn’t exist.

---

### 13. **What are some advantages of FastAPI for modern web dev?**

* Fast performance (Starlette + Uvicorn)
* Easy validation (Pydantic)
* Async/await support
* Swagger docs without extra work

---

### 14. **What are middlewares in FastAPI?**

**Answer:** Code that runs before or after each request.

Example use cases:

* Logging
* CORS
* Security headers

---

### 15. **What is `Depends()` in FastAPI?**

**Answer:** It is used to inject dependencies like DB sessions or current user into endpoints.

```python
def get_user(db: Session = Depends(get_db)):
```

---

### 16. **What is async programming and how is it supported in FastAPI?**

**Answer:** Async programming allows you to write non-blocking code using `async def` and `await`. This is useful when handling I/O-bound operations like database calls or network requests.

FastAPI is built on Starlette, which supports async natively. You can define route functions like:

```python
@app.get("/items")
async def get_items():
    return ["item1", "item2"]
```

**Why it matters:**

* Improves performance under high load
* Reduces wait time for I/O operations

---

### 17. **When should you use async vs regular def functions in FastAPI?**

**Answer:**

* Use `async def` when you are calling async-compatible functions (e.g., async DB drivers, HTTP calls).
* Use regular `def` when you're working with synchronous libraries (e.g., SQLAlchemy ORM).

**In your project:** Since SQLAlchemy is synchronous, route handlers use `def`, not `async def`.

---

# FastAPI

Install fastapi  
`uv add fastapi`

Install uvicorn  
`uv add uvicorn`

Simple API which returns a random joke from a list of jokes.

main.py file  

```python
from fastapi import FastAPI
from random import choice

app = FastAPI()

JOKES = [
  "JOKE #1",
  "JOKE #2",
  "JOKE #3",
  "JOKE #4",
  "JOKE #5",
]

@app.get('/joke')
def get_joke():
    return {
        "joke": choice(JOKES)
    }
```

How to run this?  

Run it with this command in your project directory:

```bash
uv run uvicorn main:app --reload
```

- `main` → your filename (`main.py`)
- `app` → the FastAPI instance (`app = FastAPI()`)
- `--reload` → auto-restarts server when you change code (useful during development)

---

**Then open your browser and visit:**

```
http://127.0.0.1:8000/joke
```

You should see a random joke response like:
```json
{
  "joke": "JOKE #3"
}
```

---

**Bonus — FastAPI gives you free interactive API docs:**

```
http://127.0.0.1:8000/docs      ← Swagger UI
http://127.0.0.1:8000/redoc     ← ReDoc UI
```

You can test your `/joke` endpoint directly from the browser there without writing any extra code — very handy during development!

---

> 💡 `--reload` is for **development only**. When deploying to production, drop it:
> ```bash
> uv run uvicorn main:app
> ```

Reference:  
[FastAPI > Learn](https://fastapi.tiangolo.com/learn/)

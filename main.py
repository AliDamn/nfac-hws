from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BOOKS = [
    {"id": i, "title": f"Book {i}", "author": f"Author {i}"} for i in range(1, 51)
]

ITEMS_PER_PAGE = 10


@app.get("/books", response_class=HTMLResponse)
async def read_books(request: Request, page: int = 1):
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    books = BOOKS[start:end]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "books": books,
            "page": page,
            "has_next": end < len(BOOKS),
            "has_previous": start > 0
        }
    )


@app.get("/books/{id}", response_class=HTMLResponse)
async def get_books(request: Request, id: int):
    book = None
    for b in BOOKS:
        if b["id"] == id:
            book = b
            break

    if not book:
        return HTMLResponse(content="Not found", status_code=404)

    return templates.TemplateResponse("index_detail.html", {"request": request, "book": book})


@app.get("/books/new", response_class=HTMLResponse)
def get_books_new(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})


@app.post("/books", response_class=HTMLResponse)
def post_books(
        request: Request,
        title: str = Form(),
        author: str = Form(),
        year: int = Form(),
        total_pages: int = Form(),
        genre: str = Form()
):
    new_id = len(BOOKS) + 1
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }
    BOOKS.append(new_book)

    return RedirectResponse("/books", status_code=303)
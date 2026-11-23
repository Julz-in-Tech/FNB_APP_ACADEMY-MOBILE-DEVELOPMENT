"""CRUD example for the Bookstore MockAPI inventory."""

import json

import requests


API_URL = "https://6b048975db01cf463607583b.mockapi.io/books"


def get_books():
    """Fetch and print every book."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        books = response.json()
        print("\nGET /books")
        print("Status code:", response.status_code)
        print(json.dumps(books, indent=2))
        return books
    except requests.exceptions.HTTPError as error:
        print("GET /books failed:", error)
        return None


def add_book(book):
    """Add one book and print the response."""
    response = requests.post(API_URL, json=book)
    response.raise_for_status()
    print("\nPOST /books")
    print("Status code:", response.status_code)
    print(json.dumps(response.json(), indent=2))
    return response.json()


def update_book(book_id, book):
    """Replace a book at the given id and print the response."""
    response = requests.put(f"{API_URL}/{book_id}", json=book)
    response.raise_for_status()
    print(f"\nPUT /books/{book_id}")
    print("Status code:", response.status_code)
    print(json.dumps(response.json(), indent=2))
    return response.json()


def delete_book(book_id):
    """Delete a book, then confirm a GET for it returns an HTTP error."""
    response = requests.delete(f"{API_URL}/{book_id}")
    response.raise_for_status()
    print(f"\nDELETE /books/{book_id}")
    print("Status code:", response.status_code)

    try:
        check_response = requests.get(f"{API_URL}/{book_id}")
        check_response.raise_for_status()
        print("Unexpectedly found the deleted book:")
        print(json.dumps(check_response.json(), indent=2))
        return False
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code if error.response is not None else "unknown"
        print(f"GET /books/{book_id} after deletion returned HTTP {status_code}, as expected.")
        return True


def main():
    """Run the four REST operations in sequence."""
    get_books()

    add_book(
        {
            "id": "6",
            "title": "Deep Work",
            "author": "Cal Newport",
            "rating": "9",
        }
    )

    update_book(
        "2",
        {
            "id": "2",
            "title": "The Alchemist: Illustrated Edition",
            "author": "Paulo Coelho",
            "rating": "9",
        },
    )

    delete_book("4")


if __name__ == "__main__":
    main()

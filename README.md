
# Bookstore

A basic app that authenticate signup by sending a link to provided email id. And enables you to see different books and their description.

## Project Objective
To authenticate the user and enable them to compare a book's description, publications, authors and price. 

## Prerequisites
Python 3.x


## Setup Instructions

1. Create a virtual env

```bash
  python -m venv env
```
2. Activate the virtual environment:
```bash
  env\Scripts\activate
```
3. Install the project dependencies:
```bash
   pip install -r requirements.txt
```
4. Apply database migrations:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
6. Fill the myapp/info.py file accordingly

5. Start the development server:
```bash
   python manage.py runserver
```
6. Start the development server: Open a web browser and visit http://localhost:8000 to view the application.


## Sample Output
![2023-05-27 (2)](https://github.com/VanshikaS25/bookstore/assets/100691826/a21e7974-d55d-43cb-bfe2-94129fd51dfb)


## Acknowledgements

 - [Google Books Api](https://www.googleapis.com/books/v1/volumes?q=Harry+Potter)


from flask import render_template, redirect, request, abort
from forms.add_book import AddBookForm
from datetime import datetime
from appvars import db, app
from models import Izd, Authors, Books


@app.route('/')
def index():
    pass


def main():
    pass


if __name__ == '__main__':
    main()

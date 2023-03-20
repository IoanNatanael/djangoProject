from django.shortcuts import render, redirect
import requests
import bs4
from pprint import pprint

from django.shortcuts import render, redirect

import requests
import bs4

from book.models import Book


def get_books_by_emag(request):

    url = 'https://www.emag.ro/dezvoltare-personala/c?ref=hp_menu_quick-nav_463_19&type=category'
    result = requests.get(url) # verificam daca site-ul este functional
    soup = bs4.BeautifulSoup(result.text, 'lxml') #bs4 = este un pachet python pentru a a analiza documente HTML
    #lxml - proceseaza cosul sursa(html) cu python

    context = {'all_books': []}

    all_cases = soup.find_all('div', class_='card-v2')

    for case in all_cases:
        book = {}
        name_of_book = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url')
        price = case.find('p', class_='product-new-price')

        if name_of_book is None:
            book['name_of_book'] = 'Not available'
        else:
            book['name_of_book'] = name_of_book.text

        if price is None:
            book['price'] = 'Not available'
        else:
            book['price'] = price.text

        context['all_books'].append(book)

    for book in context['all_books']:
        Book.objects.create(name=book['name_of_book'],
                            price=book['price'])




    return redirect('homepage')
import check50
import check50.c

@check50.check()
def exists():
    """greedy.js существует"""
    check50.exists("greedy.js")

@check50.check(exists)
def hello():
    """печатает решение"""
    check50.run("node greedy.js").stdout( 
"""Сортировка по удельной цене даёт:
Полная цена =  255
Взяли: ваза,часы,книга,радио"""
    ).exit()
    ## "Сортировка по удельной цене даёт:\nПолная цена =  255\nВзяли:  ваза,часы,книга,радио"

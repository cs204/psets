import check50

@check50.check()
def search():
    """search"""
    check50.run("node puzzle.js").stdout("Задание 0\n    А - лжец.\nЗадание 1\n    А - лжец.\n    Б - рыцарь.\nЗадание 2\n    А - лжец.\n    Б - рыцарь.\nЗадание 3\n    А - рыцарь.\n    Б - лжец.\n    В - рыцарь.\n", regex=False).exit(0)
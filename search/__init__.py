import check50

@check50.check()
def search():
    """search"""
    check50.run("node main.js").stdout("a\na-0->b\na-0->b-1->d\na-0->b-1->d-0->f\na-0->b-0->c\nSolution  a-0->b-0->c-0->e\n", regex=False).exit(0)
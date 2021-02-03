import check50
import check50.c

@check50.check()
def exists():
    """hello.js существует"""
    check50.exists("hello.js")

@check50.check(exists)
def hello():
    """печатает Hello, world"""
    check50.run("node hello.js").stdout("Hello, world!").exit()

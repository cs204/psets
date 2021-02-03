import check50

@check50.check()
def hello_world():
    """hello world"""
    check50.run("node hello.js").stdout("Hello, world!", regex=False).exit(0)
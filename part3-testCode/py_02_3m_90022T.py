import pprint

def calc_unitprice() -> None:
    """20200918, display unit price for same kind of 3M 90022T
    
    NOTE: im too lazy to do web scraping stuff. hardcode won :^)
    """
    _no1 = 16 / 22.9
    _no2 = 180 / 142.35
    _no3 = 48 / 68
    _no4 = 10 / 57
    _no5 = 24 / 32.9
    pprint.pprint(locals())

if __name__ == "__main__":
    calc_unitprice()
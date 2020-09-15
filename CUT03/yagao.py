import pprint

def calc_price():
    sw   = 150 * 3 / 39.9
    sk   = 120 * 6 / 39
    ssd  = (100 * 3 + 20 * 2) / 69
    jjs  = 116 * 2 / 39.9
    hr   = 480 / 39.9
    glj  = 250 / 13.2
    ynby = 500 / 69

    # much bigger much better
    # print(globals())
    # print()
    # print(locals())
    pprint.pprint(locals())

# def calc_melatonim():
#     nature = 63

if __name__ == "__main__":
    calc_price()
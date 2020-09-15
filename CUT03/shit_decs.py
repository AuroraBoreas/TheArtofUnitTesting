import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def addBreaker(f):
    def inner(*args, **kwargs):
        logging.debug('-' * 50)
        return f(*args)
    return inner

def addHoshi(f):
    def inner(*args, **kwargs):
        logging.debug('*' * 50)
        return f(*args)
    return inner

def addSwitch(toggle=False):
    def dec(f):
        def inner(*args, **kargs):
            if toggle:
                logging.debug('~' * 50)
            return f(*args)
        return inner
    return dec

def run_n_times(n=1):
    def dec(f):
        def inner(*args, **kwargs):
            for _ in range(n):
                f(*args)
        return inner
    return dec

@addSwitch(toggle=False)
@addHoshi
@addBreaker
def victim(*args):
    return args

@run_n_times(n=10)
def victim1(*args):
    logging.debug(f'{args}')

if __name__ == "__main__":
    logging.debug(victim(1, 2, 3))
    print()
    victim1(1, 2, 3)
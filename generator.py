import random as prand
import itertools

import hypothesis.strategies as st
from hypothesis.strategies import characters
import math

default_names = ['abe', 'value', 'inn', 'info']

names = [ x + str(y) for x,y in itertools.product(default_names, range(5))]
key_prefix = ['name', 'GGIM', 'place', 'somethinglong']

widths = [10, 50, 200]


txt_g1 = st.text(min_size=3, max_size=200)
txt_g2 = st.text(alphabet=characters(whitelist_categories=('Lu', 'Ll')), min_size=4, max_size=16)
i_g1 = prand.randint(2234567890110, 9234567890110)


#hist([ skew(prand.weibullvariate(1.9,3), 1.8)  for y in range(2500)], 50)
def skew(x, factor=2): 
    return (numpy.sin(x)) * factor + x



def get_array(width=10):
    #headers = 
    raise Exception('Not implemented yet')
    return 0


def rotate(n, size):
    return n - size * math.floor(n / size)


def gen_headers(prefixes, width):
    return [ prefixes[rotate(y, len(prefixes))] + str(y)  for y in range(width)]



def get_dict(width=10):
    headers = gen_headers(key_prefix)
    
    return headers





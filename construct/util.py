import string
import random
random.seed(0)

sampler = "ABCDEF" + string.digits

def generate_id():
  lens = [8, 4, 4, 4, 12]
  parts = [''.join(random.choices(sampler, k=l)) for l in lens]
  return '-'.join(parts)

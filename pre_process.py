import os
import pandas as pd

from pprint import pprint

def generate_hex_string():
  import secrets

  # Generate a 128-bit random number
  random_number = secrets.randbits(128)

  # Convert the random number to a hex string
  hex_string = format(random_number, 'x')

  # Ensure the hex string is 32 characters long (128 bits / 4 bits per hex character = 32 characters)
  hex_string = hex_string.zfill(32)

  return hex_string

def get_ad_names():
  directory = 'data'
  ad_hex_codes = {}

  for filename in os.listdir(directory):
    ad_hex_codes[filename] = generate_hex_string()
  
  return ad_hex_codes

ad_hex_codes = get_ad_names()
df = pd.DataFrame(
  list(ad_hex_codes.items()),
  columns = [
    'ad_name',
    'hash'
  ]
)

df.to_csv('ads_hex.csv', index = False)

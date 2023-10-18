import os
import subprocess

encoded_audios = 'encoded'
strength = 50

mappings = {
  '3c490cdd62f27f36970529a39fac6187': 'walmart.mp3',
  'b2cc55a72451262402038e15821e99e1': 'pizza_hut.mp3',
  '587328e6076283114baa1b3d78bb3b4e': 'att.mp3',
  'a75057182de87de5c103017d62344761': 'verizon.mp3',
  '6d7582d3cb8a44e09a8e833e32d5a316': 'subway.mp3'
}

for filename in os.listdir(encoded_audios):
  full_path = os.path.join(encoded_audios, filename)

  command = f'audiowmark get {full_path}'

  process = subprocess.Popen(
    command,
    shell = True,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
  )
  stdout, stderr = process.communicate()

  if process.returncode == 0:
    print(f'File name: {full_path}')
    print(f'{stdout.decode("utf-8")}')
  else:
    print(f'Failed: {stderr.decode("utf-8")}')
  
  print()
  print()

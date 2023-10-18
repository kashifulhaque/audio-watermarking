import os
import subprocess

raw_audios = 'data'
encoded_audios = 'encoded'
strength = 50

mappings = {
  'walmart.mp3': '3c490cdd62f27f36970529a39fac6187',
  'pizza_hut.mp3': 'b2cc55a72451262402038e15821e99e1',
  'att.mp3': '587328e6076283114baa1b3d78bb3b4e',
  'verizon.mp3': 'a75057182de87de5c103017d62344761',
  'subway.mp3': '6d7582d3cb8a44e09a8e833e32d5a316'
}

for filename in os.listdir(raw_audios):
  full_path = os.path.join(raw_audios, filename)
  encoded_path = os.path.join(encoded_audios, filename)

  command = f'audiowmark add --strength {strength} {full_path} {encoded_path} {mappings[filename]}'

  process = subprocess.Popen(
    command,
    shell = True,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
  )
  stdout, stderr = process.communicate()

  if process.returncode == 0:
    print(f'Success')
  else:
    print(f'Failed: {stderr.decode("utf-8")}')

import random
import string
import argparse

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

parser = argparse.ArgumentParser(description= 'Password Generator')
parser.add_argument('--length', type=int, default=7, help='Length of password')
args = parser.parse_args()

password = generate_password(args.length)
print(f'Generated Password: {password}')



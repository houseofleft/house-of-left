import glob
import os
import random

from jinja2 import Environment, FileSystemLoader

pieces = glob.glob('pieces/*.py')

try:
    os.mkdir('gallery')
except FileExistsError:
    pass

for piece in pieces:
    name = piece.rsplit('/', 1)[-1]
    name = name.replace('.py', '')
    width = 1000
    height = random.randint(5, 15) * 100
    os.system(f'python3 {piece} gallery/{name}.png {width} {height}') 

print('gallery images created')

image_files = glob.glob('gallery/*.png')

env = Environment(
    loader=FileSystemLoader('.')
)
template = env.get_template('readme_template.md')
rendered_gallery = template.render(
    images=glob.glob('gallery/*.png')
)
with open('README.md', 'w') as file:
    file.write(rendered_gallery)

print('readme rendered and saved')

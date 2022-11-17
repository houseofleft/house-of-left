# house of left

## What's this repo?

Heya 👋 I make mostly visual artworks with code.

I'm interested in generative art systems, where based on an input (usually random) the output can vary.

In this repo, you'll find works in progress under "sketches" (stuff in here might work, might have errors, and might produce some kind of crazy half finished output) and more complete stuff under "pieces".

## Generative readme gallery

This readme is also a self-generating gallery of outputs from everything in the pieces folder. The pieces here will be different each time the readme file is generated.

{% for image in images %}

### {{ image.rsplit('/', 1)[-1].replace('.png', '') }}
![auto-generated image for below title]({{ image }})

{% endfor %}

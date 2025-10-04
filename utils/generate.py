#!/usr/bin/env python3

from pathlib import Path

from matplotlib.pyplot import Circle, subplots, show
from numpy import frombuffer, save

def generate(dots, filename):
    fig, ax = subplots(figsize=(10, 10), dpi=100)
    ax.set_axis_off()
    ax.set_xlim(-10, +10)
    ax.set_ylim(-10, +10)

    for x in dots:
        ax.add_patch(x)

    fig.savefig(filename.with_suffix('.png'))
    arr = frombuffer(fig.canvas.buffer_rgba(), dtype='uint8').reshape(
        (fig.canvas.width(), fig.canvas.height(), -1)
    )
    arr = arr[:, :, :3] # remove alpha channel
    arr = arr.min(axis=-1) # make monochrome
    save(filename.with_suffix('.npy'), arr)

if __name__ == '__main__':
    examples_dir = Path('examples')

    generate(dots=[
        Circle(( 0,  0), 1, color='black'),
    ], filename=examples_dir / 'one-dot')

    generate(dots=[
        Circle(( 0,  0), 1, color='black'),
        Circle((+5, +5), 1, color='black'),
        Circle((-5, -5), 1, color='black'),
    ], filename=examples_dir / 'three-dots')

    generate(dots=[
        Circle(( 0,  0), 1, color='black'),
        Circle((+5, +5), 1, color='black'),
        Circle((-5, +5), 1, color='black'),
        Circle((+5, -5), 1, color='black'),
        Circle((-5, -5), 1, color='black'),
    ], filename=examples_dir / 'five-dots')

    generate(dots=[], filename=examples_dir / 'no-dots')

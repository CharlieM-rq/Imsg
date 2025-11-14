# Examples

This directory contains small standalone scripts that demonstrate or test-drive
parts of the project infrastructure. At the moment it includes a 2D random walk
simulation that visualizes the final position of a collection of walkers.

## Random walk simulation

The script relies on `numpy` and `matplotlib`. Install them with:

```bash
python -m pip install numpy matplotlib
```

Then run the simulation (the default values simulate 500 walkers for 200
steps):

```bash
python examples/random_walk_simulation.py
```

You can tweak the walk via command-line flags:

```bash
python examples/random_walk_simulation.py --num-particles 1000 --num-steps 400
```

A scatter plot will appear showing the final locations of each walker.

"""Run a configurable 2D random walk simulation and visualize the final positions."""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class SimulationConfig:
    """Configuration options for the random walk simulation."""

    num_particles: int
    num_steps: int


def run_simulation(config: SimulationConfig) -> np.ndarray:
    """Simulate a 2D random walk and return the particle positions."""
    positions = np.zeros((config.num_particles, 2), dtype=int)
    step_options = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])

    for _ in range(config.num_steps):
        steps = step_options[
            np.random.randint(0, len(step_options), size=config.num_particles)
        ]
        positions += steps

    return positions


def plot_positions(positions: np.ndarray, config: SimulationConfig) -> None:
    """Plot the final positions of all particles."""
    plt.figure()
    plt.scatter(positions[:, 0], positions[:, 1], s=5)
    plt.title(
        f"2D Random Walk: {config.num_particles} Particles After {config.num_steps} Steps"
    )
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.axis("equal")
    plt.show()


def parse_args() -> SimulationConfig:
    """Parse command-line arguments for the simulation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--num-particles",
        type=int,
        default=500,
        help="Number of walkers to simulate (default: %(default)s)",
    )
    parser.add_argument(
        "--num-steps",
        type=int,
        default=200,
        help="Number of steps each walker takes (default: %(default)s)",
    )

    args = parser.parse_args()
    return SimulationConfig(num_particles=args.num_particles, num_steps=args.num_steps)


def main() -> None:
    config = parse_args()
    positions = run_simulation(config)
    plot_positions(positions, config)


if __name__ == "__main__":
    main()

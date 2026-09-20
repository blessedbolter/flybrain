import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from flywire_sim import generate_synthetic, run_simulation
from stimulation import Stimulus


N_NEURONS = 1000
N_SYNAPSES = 5000

print("Creating small synthetic brain...")
n, syn, offsets, targets, weights = generate_synthetic(
    n_neurons=N_NEURONS,
    n_synapses=N_SYNAPSES,
    seed=42,
)

stimulus = Stimulus(
    neuron_ids=[0],
    current=2.0,
    start_step=10,
    duration=20,
)

print("Applying stimulus to neuron 0...")
run_simulation(
    n,
    syn,
    offsets,
    targets,
    weights,
    num_timesteps=50,
    warmup_steps=0,
    seed=42,
    verbose=True,
    stimuli=[stimulus],
)

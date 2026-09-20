import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import cupy as cp


class Stimulus:
    """External current stimulus applied to selected neurons."""

    def __init__(self, neuron_ids, current, start_step, duration):
        self.neuron_ids = cp.asarray(neuron_ids, dtype=cp.int32)
        self.current = float(current)
        self.start_step = int(start_step)
        self.end_step = self.start_step + int(duration)

    def apply(self, d_current, step):
        """Inject current if the stimulus is active at this timestep."""
        if self.start_step <= step < self.end_step:
            d_current[self.neuron_ids] += self.current

import numpy as np
from ._madrona_simple_example_cpp import SimpleGridworldSimulator, madrona

__all__ = ['GridWorld']

class GridWorld:
    def __init__(self,
                 num_worlds,
                 start_cell,
                 end_cells,
                 rewards,
                 walls,
                 gpu_sim = False,
                 _gpu_id = 0,
                 _k_aray = 4, # fei add in 20241202
                 _cc_method = 0,
            ):
        self.size = np.array(walls.shape)
        self.start_cell = start_cell
        self.end_cells = end_cells
        self.rewards_input = rewards
        self.walls = walls

        self.sim = SimpleGridworldSimulator(
                walls = np.array(walls).astype(np.bool_),
                rewards = np.array(rewards).astype(np.float32),
                end_cells = np.array(end_cells).astype(np.int32),
                start_x = start_cell[1],
                start_y = start_cell[0],
                max_episode_length = 0, # No max
                exec_mode = madrona.ExecMode.CUDA if gpu_sim else madrona.ExecMode.CPU,
                num_worlds = num_worlds,
                gpu_id = _gpu_id,
                k_aray = _k_aray,
                cc_method = _cc_method,
            )

        self.force_reset = self.sim.reset_tensor().to_torch()
        self.actions = self.sim.action_tensor().to_torch()
        self.observations = self.sim.observation_tensor().to_torch()
        self.rewards = self.sim.reward_tensor().to_torch()
        self.dones = self.sim.done_tensor().to_torch()
        self.results = self.sim.results_tensor().to_torch()
        self.results2 = self.sim.results2_tensor().to_torch()
        self.simulation_time = self.sim.simulation_time_tensor().to_torch()
        self.madronaEvents = self.sim.madronaEvents_tensor().to_torch()
        self.madronaEventsResult = self.sim.madronaEventsResult_tensor().to_torch()
        self.processParams = self.sim.processParams_tensor().to_torch()

    def step(self):
        self.sim.step()

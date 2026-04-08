from models import Observation, Action
from simulator import simulate

class PoliSimEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state_data = {
            "pollution": 80,
            "economy": 70,
            "satisfaction": 50,
            "month": 0
        }
        return Observation(**self.state_data)

    def step(self, action: Action):
        self.state_data["month"] += 1

        new_state = simulate(self.state_data, action.model_dump())
        self.state_data.update(new_state)

        reward = self.compute_reward()
        done = self.state_data["month"] >= 6

        return Observation(**self.state_data), reward, done, {}

    def compute_reward(self):
        p = self.state_data["pollution"]
        e = self.state_data["economy"]
        s = self.state_data["satisfaction"]

        return round(((100 - p)*0.4 + e*0.3 + s*0.3)/100, 2)

    def state(self):
        return self.state_data

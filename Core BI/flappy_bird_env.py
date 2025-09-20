import gymnasium as gym
from gymnasium import spaces
import numpy as np

class FlappyBirdEnv(gym.Env):
    def __init__(self, width=288, height=512, render_mode=None, max_steps=1000):
        super().__init__()
        self.width = width
        self.height = height
        self.render_mode = render_mode
        self.max_steps = max_steps

        self.action_space = spaces.Discrete(2)
        low = np.array([0, -10, 0, 0], dtype=np.float32)
        high = np.array([self.height, 10, self.width, self.height], dtype=np.float32)
        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        self.gravity = 0.25
        self.flap_power = -4
        self.pipe_width = 52
        self.pipe_gap = 100
        self.steps = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.bird_y = self.height // 2
        self.bird_vel = 0
        self.pipe_x = self.width
        self.pipe_y = np.random.randint(100, self.height - 100)
        self.score = 0
        self.steps = 0

        return np.array([self.bird_y, self.bird_vel, self.pipe_x, self.pipe_y], dtype=np.float32), {}

    def step(self, action):
        self.steps += 1
        self.bird_vel += self.gravity
        if action == 1:
            self.bird_vel = self.flap_power
        self.bird_y += self.bird_vel

        self.pipe_x -= 2
        if self.pipe_x < -self.pipe_width:
            self.pipe_x = self.width
            self.pipe_y = np.random.randint(100, self.height - 100)
            self.score += 1

        reward = 1.0
        terminated = False
        truncated = self.steps >= self.max_steps

        if self.bird_y <= 0 or self.bird_y >= self.height:
            terminated = True
        if (self.pipe_x < 60 < self.pipe_x + self.pipe_width):  # 假设小鸟x=60
            if not (self.pipe_y < self.bird_y < self.pipe_y + self.pipe_gap):
                terminated = True

        obs = np.array([self.bird_y, self.bird_vel, self.pipe_x, self.pipe_y], dtype=np.float32)
        return obs, reward, terminated, truncated, {"score": self.score}

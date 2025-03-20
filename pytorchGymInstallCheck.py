import torch
from gym import envs
x = torch.empty(3,4)
print(x)
print('SpaceInvaders-v0' in list(envs.registry))
print('SpaceInvaders-v4' in list(envs.registry))
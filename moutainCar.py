import gym
import logging
import numpy as np
logging.basicConfig(level=logging.INFO)
env = gym.make('MountainCar-v0', render_mode="human")
# for key in vars(env.spec):
#     logging.info('%s:%s',key,vars(env.spec)[key])
# for key in vars(env.unwrapped):
#     logging.info('%s:%s',key,vars(env.unwrapped)[key])

#!!!this "agent" is just a prameter optimized equation, which do not "reinforce learn" during the process!!!
#!!!只使用了一个优化好的公式代入，每一步按照公式修正速度，并没有真正强化学习，并没有优化策略。!!!
class CloseFormAgent:
    def __init__(self,__):
        pass
    def reset(self,mode=None):
        pass
    def step(self, observation, reward, terminated):
        position, velocity = observation
        lb = min(-0.09*(position+0.25)**2+0.03,0.3*(position+0.9)**4-0.008)
        ub = -0.07*(position+0.38)**2 + 0.07
        if lb< velocity< ub:
            action = 2
        else:
            action = 0
        return action
    def close(self):
        pass
agent = CloseFormAgent(env)
env.reset()
def play_episode(env, agent, seed=None, mode= None, render= False, render_interval = 0):
    observation, _ = env.reset(seed = seed)
    reward, terminated, trucated = 0.,False,False
    agent.reset(mode = mode)
    episode_reward, elapsed_steps = 0.,0
    while True:
        action = agent.step(observation, reward, terminated)
        if render and render_interval and elapsed_steps%render_interval == 0:
            env.render()
        if terminated or trucated:
            break
        observation, reward, terminated, trucated, _ = env.step(action)
        episode_reward += reward
        elapsed_steps += 1
    agent.close()
    return episode_reward, elapsed_steps

episode_rewards = []
for episode in range(10):
    render = True
    #render = (episode % 100 == 0)
    episode_reward, elapsed_steps = play_episode(env,agent,seed = 42,render = render,render_interval=100)
    episode_rewards.append(episode_reward)
    logging.info('round%d: reward%0.2f,step:%d', episode,episode_reward,elapsed_steps)

logging.info('average round%0.2f ± %0.2f', np.mean(episode_rewards), np.std(episode_rewards))
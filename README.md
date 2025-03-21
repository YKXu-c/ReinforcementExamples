# ReinforcementExamples
I am learning reinfocement learning based on pytorch, and will record the projects in this repository.

## Environments and Install\
- As [pytorch 2.6.0](https://pytorch.org/get-started/locally/) needs python 3.9 or later, [gym](https://www.gymlibrary.dev/) needs 3.7-3.10. Use python 3.10 is a good choice. And basic conda env is in [pytorchgym.yml](https://github.com/YKXu-c/ReinforcementExamples/edit/main/pytorchgym.yml)\
You can just use `conda env create -f pytorchgym.yml` to create the same env in your PC.
- Rules of gym.make.reset and render() are updated, so codes in [YuxiLiu's cookbook](https://www.amazon.com/PyTorch-Reinforcement-Learning-Cookbook-self-learning-ebook/dp/B07YZ9GZ7J) need to be updated

## Games Examples
- [MountainCar](https://github.com/YKXu-c/ReinforcementExamples/blob/main/examples_gym_games/moutainCar.py)\
  This is a basic game. Code is form [肖智清Zhiqing Xiao](https://book.douban.com/subject/34478302/).
  In this game, we can learn how to define an agent(without policy reinforcement, just an equation), how to use render() to show the process of each step, the interaction between agent and env.

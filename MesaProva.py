# model.py
from mesa import Agent, Model
from mesa.time import RandomActivation


class MoneyAgent(Agent):

    def __init__(self, unique_id, model,p):
        super().__init__(unique_id, model)
        print(p)
    def step(self):
        self.otherAgents = self.model.schedule.agents
        print(self.otherAgents)


class MoneyModel(Model):

    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self, 3)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()

empty_model = MoneyModel(10)
empty_model.step()
from media_agents import AgentFactory
agent = AgentFactory.create_agent("C")
print(agent.getStaircase(10))
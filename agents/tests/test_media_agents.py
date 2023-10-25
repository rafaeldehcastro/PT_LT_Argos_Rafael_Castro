import unittest
from media_agents.media_agents import AgentFactory, AgentA, AgentB, AgentC

class TestAgentA(unittest.TestCase):
    
    def setUp(self):
        self.agent = AgentFactory.create_agent("A")
        
    def test_average(self):
        self.assertEqual(self.agent.getMedia([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(self.agent.getMedia([10, 20, 30]), 20.0)
        

class TestAgentB(unittest.TestCase):
    
    def setUp(self):
        self.agent = AgentFactory.create_agent("B")
        
    def test_harmonic_mean(self):
        self.assertEqual(self.agent.getMedia([1, 2, 4]), 1.7142857142857142)
        
    def test_zero_in_list(self):
        with self.assertRaises(ValueError):
            self.agent.getMedia([0, 1, 2])
            

class TestAgentC(unittest.TestCase):
    
    def setUp(self):
        self.agent = AgentFactory.create_agent("C")
        
    def test_median_odd(self):
        self.assertEqual(self.agent.getMedia([1, 3, 2, 5, 4]), 3)
        
    def test_median_even(self):
        self.assertEqual(self.agent.getMedia([1, 3, 2, 5, 4, 6]), 3.5)


if __name__ == '__main__':
    unittest.main()

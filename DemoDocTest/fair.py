import fairpyx as fp
import fairpyx.instances as instances
def main():

    """
    /home/abodi-massarwa/Ariel@PycharmProjects/DemoDocTest/bin/python /home/abodi-massarwa/Ariel@PycharmProjects/DemoDocTest/fair.py
Help on class Instance in module fairpyx.instances:

class Instance(builtins.object)
 |  Instance(valuations: <built-in function any>, agent_capacities: <built-in function any> = None, agent_entitlements: <built-in function any> = None, item_capacities: <built-in function any> = None, agent_conflicts: <built-in function any> = None, item_conflicts: <built-in function any> = None, agents: list = None, items: list = None)
 |
 |  Represents an instance of the fair course-allocation problem.
 |  Exposes the following functions:
 |   * agent_capacity:       maps an agent name/index to its capacity (num of seats required).
 |   * item_capacity:        maps an item  name/index to its capacity (num of seats allocated).
 |   * agent_conflicts:      maps an agent  name/index to a set of items that conflict with it (- cannot be allocated to this agent).
 |   * item_conflicts:       maps an item  name/index to a set of items that conflict with it (- cannot be allocated together).
 |   * agent_item_value:     maps an agent,item pair to the agent's value for the item.
 |   * agents: an enumeration of the agents (derived from agent_capacity).
 |   * items: an enumeration of the items (derived from item_capacity).
 |
 |  ### dict of dicts:
 |  >>> instance = Instance(
 |  ...   agent_capacities = {"Alice": 2, "Bob": 3},
 |  ...   item_capacities  = {"c1": 4, "c2": 5},
 |  ...   valuations       = {"Alice": {"c1": 11, "c2": 22}, "Bob": {"c1": 33, "c2": 44}})
 |  >>> instance.agent_capacity("Alice")
 |  2
 |  >>> instance.item_capacity("c2")
 |  5
 |  >>> instance.agent_item_value("Bob", "c1")
 |  33
 |  >>> instance.agent_bundle_value("Bob", ["c1","c2"])
 |  77
 |  >>> instance.agent_fractionalbundle_value("Bob", {"c1":1, "c2":0.5})
 |  55.0
 |  >>> instance.agent_maximum_value("Alice")
 |  33
 |  >>> instance.agent_maximum_value("Bob")
 |  77
 |  >>> instance.agent_ranking("Alice", [])
 |  {'c2': 1, 'c1': 2}
 |  >>> instance.agent_ranking("Alice", ["c1"])
 |  {'c2': 1, 'c1': 2}
 |  >>> instance.agent_ranking("Alice", ["c2"])
 |  {'c2': 1, 'c1': 2}
 |
 |  ### dict of lists:
 |  >>> instance = Instance(
 |  ...   agent_capacities = {"Alice": 2, "Bob": 3},
 |  ...   item_capacities  = [1,2,3,4],
 |  ...   valuations       = {"Alice": [22,33,44,55], "Bob": [66,77,88,99]})
 |  >>> instance.agent_capacity("Alice")
 |  2
 |  >>> instance.item_capacity(2)
 |  3
 |  >>> instance.agent_item_value("Alice", 3)
 |  55
 |  >>> instance.agent_maximum_value("Alice")
 |  99
 |  >>> instance.agent_maximum_value("Bob")
 |  264
 |
 |
 |  ### default values:
 |  >>> instance = Instance(valuations={"avi": {"x":5, "y": 4}, "beni": {"x":2, "y":3}})
 |  >>> instance.agent_capacity("avi")
 |  2
 |  >>> instance.item_capacity("x")
 |  1
 |  >>> instance.agent_item_value("beni", "y")
 |  3
 |  >>> instance.agent_entitlement("Alice")
 |  1
 |  >>> instance.agent_conflicts("Alice")
 |  set()
 |  >>> instance.item_conflicts("c1")
 |  set()
 |
 |  ### agent rankings
 |  >>> instance = Instance(valuations={"avi": {"x":5, "y": 5}, "beni": {"x":3, "y":3}}, agent_capacities=1)
 |  >>> instance.agent_capacity("avi")
 |  1
 |  >>> instance.agent_ranking("avi", ["x"])
 |  {'x': 1, 'y': 2}
 |  >>> instance.agent_ranking("avi", ["y"])
 |  {'y': 1, 'x': 2}
 |
 |  ### conflicts:
 |  >>> instance = Instance(
 |  ...   agent_conflicts = {"Alice": {0,1,2}, "Bob": {2,3,4}},
 |  ...   item_conflicts  = [{"Alice", "Bob"}, set(), {"Alice"}, {"Bob"}, set()],
 |  ...   valuations       = {"Alice": [22,33,44,55,66], "Bob": [66,77,88,99,100]})
 |  >>> instance.agent_conflicts("Bob")
 |  {2, 3, 4}
 |  >>> instance.item_conflicts(2)
 |  {'Alice'}
 |
 |  Methods defined here:
 |
 |  __init__(self, valuations: <built-in function any>, agent_capacities: <built-in function any> = None, agent_entitlements: <built-in function any> = None, item_capacities: <built-in function any> = None, agent_conflicts: <built-in function any> = None, item_conflicts: <built-in function any> = None, agents: list = None, items: list = None)
 |      Initialize an instance from the given
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  agent_bundle_value(self, agent: <built-in function any>, bundle: list[any])
 |      Return the agent's value for a bundle (a list of items).
 |
 |  agent_fractionalbundle_value(self, agent: <built-in function any>, bundle: list[any])
 |      Return the agent's value for a fractional bundle (a dict mapping items to fractions).
 |
 |  agent_maximum_value(self, agent: <built-in function any>)
 |      Return the maximum possible value of an agent: the sum of the top x items, where x is the agent's capacity.
 |
 |  agent_normalized_item_value(self, agent: <built-in function any>, item: <built-in function any>)
 |
 |  agent_ranking(self, agent: <built-in function any>, prioritized_items: list = []) -> dict
 |      Compute a map in which each item is mapped to its ranking: the best item is mapped to 1, the second-best to 2, etc.
 |
 |      :prioritized_items: a list of items that are "prioritized".
 |           This list is used for tie-breaking, in cases the agent assigns the same value to different items.
 |
 |  map_agent_to_ranking(self, map_agent_to_prioritized_items={}) -> dict
 |      Compute a map in which each agent is mapped to a dict mapping each item to its ranking.
 |      For example, if item 'x' is the best item of Alice, then result["Alice"]["x"]==1.
 |
 |      :map_agent_to_prioritized_items: maps each agent to a list of items that are "prioritized".
 |           This list is used for tie-breaking, in cases the agent assigns the same value to different items.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  random_sample(max_num_of_agents: int, max_total_agent_capacity: int, prototype_valuations: dict, prototype_agent_capacities: dict, prototype_agent_conflicts: dict, item_capacities: dict, item_conflicts: dict, random_seed: int = None)
 |      Generate a random instance by sampling values of existing agents.
 |
 |      :param max_num_of_agents: creates at most this number of agents.
 |      :param max_total_agent_capacity: the total capacity of all agents will be at most this number plus one agent.
 |
 |  random_szws(num_of_agents: int, num_of_items: int, agent_capacity: int, supply_ratio: float, num_of_popular_items: int, mean_num_of_favorite_items: float, favorite_item_value_bounds: tuple[int, int], nonfavorite_item_value_bounds: tuple[int, int], normalized_sum_of_values: int, agent_name_template='s{index}', item_name_template='c{index}', random_seed: int = None)
 |      Generate a random instance with additive utilities, using the process described at:
 |          Soumalias, Zamanlooy, Weissteiner, Seuken: "Machine Learning-powered Course Allocation", arXiv 2210.00954, subsection 5.1
 |      NOTE: currently, we do not generate complementarities and substitutabilities. We also do not model reporting mistakes.
 |
 |  random_uniform(num_of_agents: int, num_of_items: int, agent_capacity_bounds: tuple[int, int], item_capacity_bounds: tuple[int, int], item_base_value_bounds: tuple[int, int], item_subjective_ratio_bounds: tuple[float, float], normalized_sum_of_values: int, agent_name_template='s{index}', item_name_template='c{index}', random_seed: int = None)
 |      Generate a random instance by drawing values from uniform distributions.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  logger = <Logger fairpyx.instances (WARNING)>


Process finished with exit code 0

    """
    #help(fp.instances.Instance)
    """
    
    """
    #help(fp.allocations.AllocationBuilder)
    #help()

    #agent_capacities = {"Abed El Kareem":5}
    # agent_capacities = {"Abed El Kareem":{"Apples":1,"Melons":1,"Bananas":2}}#TODO doesnt work capacity for each item.
    # item_capacities = {"Apples": 1,"Melons":1, "Bananas": 2}
    # item_valuations = {"Abed El Kareem":{"Apples": 10, "Bananas":1}}
    # inst=instances.Instance(agent_capacities=agent_capacities,item_capacities=item_capacities,valuations=item_valuations)
    # print(fp.divide(fp.algorithms.round_robin,instance=inst)) # TODO doesn't work since the algorithm seems to only support the courses allocation case #  in which there is no different capacities for different catergories
    # print(inst)
    """#TODO the exisiting Instance class lacks the support for a partition matroid in which items are divided into 
    categories and each agent has a unique capacity for each category |M|=>|categories|>=1"""

    #TODO ask Ariel whats is expected from me in here ? to expand an existing class of instance , or make my own instance class , or the exisiting one is enough ?

# def incr(x):
#     return x+1


def capped_round_robin(inst: instances.Instance):
    """
    This function
    :param inst:
    :return:
    """



if __name__ == '__main__':
    main()




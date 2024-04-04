import fairpyx as fp
from fairpyx.instances import Instance

"""
Types Encountered:
Dictionaries: Used for storing mappings such as valuations, agent capacities, item capacities, agent conflicts, and item conflicts.
Lists: Used in some cases like item capacities and valuations, where items are indexed by integers.
Numpy Arrays: Similar to lists but with additional functionalities and optimizations for numerical computations.

Functions and Their Explanations:
__init__: Initializes an instance of the Instance class with various parameters such as valuations, agent capacities, item capacities, agent conflicts, and item conflicts.
agent_capacity: Maps an agent name/index to its capacity (number of seats required).
item_capacity: Maps an item name/index to its capacity (number of seats allocated).
agent_conflicts: Maps an agent name/index to a set of items that conflict with it (cannot be allocated to this agent).
item_conflicts: Maps an item name/index to a set of items that conflict with it (cannot be allocated together).
agent_item_value: Maps an agent, item pair to the agent's value for the item.
agents: Enumerates the agents derived from agent capacities.
items: Enumerates the items derived from item capacities.
agent_bundle_value: Computes an agent's value for a bundle (list) of items.
agent_fractionalbundle_value: Computes an agent's value for a fractional bundle (dict) of items with fractions.
agent_ranking: Computes a map where each item is ranked based on the agent's value, considering prioritized items for tie-breaking.
map_agent_to_ranking: Computes a map of agents to their item rankings.
__str__: Provides a string representation of the instance with detailed information about agents, items, capacities, conflicts, and valuations.
agent_maximum_value: Computes the maximum possible value of an agent based on the top items it can select.
agent_normalized_item_value: Computes the normalized value of an item for an agent based on its maximum possible value.
random_uniform: Generates a random instance with uniform distributions for agent and item properties.
random_szws: Generates a random instance using a specific process described in the SZWS experiment.
random_sample: Generates a random instance by sampling values from existing agents.
These functions collectively provide functionalities for initializing, managing, and analyzing instances of the fair course-allocation problem, including generating random instances for experimental purposes.
"""


class CustomInstance(Instance):
    def __init__(self, valuations: dict, agent_capacities: dict, categories: dict, item_categories: dict, items: list):
        """
        super class constructor is :
         TODO def __init__(self, valuations:any, agent_capacities:any=None, agent_entitlements:any=None,
          item_capacities:any=None, agent_conflicts:any=None, item_conflicts:any=None, agents:list=None, items:list=None):

          TODO item capacities can be dealt with as constant 1's , this case is handles in case of not passing any item_capacity arguments

  TODO agent_capacities are a bit different than the ones handled in the parent class since now each agent has capacities for each category ...
         TODO parent-class agent-capacity-example  {Alice:2,Bob:3}
         TODO sub-class agent-capacity-example {Alice:{c1:2,c2:3},Bob:{c1:0,c2,1}}
         agent_capacity_keys, agent_capacity_func = get_keys_and_mapping(agent_capacities) (TODO from original class constructor)
        """
        super().__init__(valuations=valuations, items=items)
        key1,key2,agent_capacity_func=self.get_keys_and_mapping_2d(agent_capacities)
        self.agent_capacity = agent_capacity_func or self.constant_function(len(self.items))
        ##TODO ask Erel
        ## but this causes a problem in which the original class only deals with capacity per agent its not used to deal with several capacities per agent(for each category)
        ## TODO categorization -AFFECTS-> Agent_capacities (need to fix the use-cases in the future !!)

        self.item_categories=item_categories # for example {"category1":['item1','item2','item3'],'category2':['item4','item5','item6']} TODO we can pass it as extra argument
        # TODO in divide(algorithm=foo,categories={"category1":['item1','item2','item3'],'category2':['item4','item5','item6']})










        # self.agent_capacities = agent_capacities
        # self.categories = categories
        # self.item_categories = item_categories
        # self.items=items
        # self._item_capacities ={}

    def agent_category_capacity(self, agent: str, category: str) -> int:
        return self.agent_capacities[agent][category]

    def agent_category_items(self, agent: str, category: str) -> set:
        return self.categories[agent][category]

    def item_category(self, item: str) -> str:
        return self.item_categories[item]

    def get_all_agents(self) -> list:
        return list(self.agent_capacities.keys())

    def get_all_categories(self, agent: str) -> list:
        return list(self.categories[agent].keys())

    def get_items(self):
        return self.items


def example1():
    # Example usage
    valuations = {
        "alice": {"item1": 5, "item2": 3},
        "bob": {"item1": 4, "item2": 6}
    }
    agent_capacities = {
        "alice": {"category1": 2, "category2": 3},
        "bob": {"category1": 4, "category2": 2}
    }
    categories = {
        "alice": {"category1": {"item1"}, "category2": {"item2"}},
        "bob": {"category1": {"item2"}, "category2": {"item1"}}
    }
    item_categories = {
        "item1": "category1",
        "item2": "category2"
    }
    items = ["item1", "item2"]

    custom_instance = CustomInstance(valuations, agent_capacities, categories, item_categories, items)
    # Accessing all agents
    print(custom_instance.get_all_agents())  # Output: ['alice', 'bob']

    # Accessing all categories for an agent
    print(custom_instance.get_all_categories("alice"))  # Output: ['category1', 'category2']

    # Accessing agent capacities
    print(custom_instance.agent_category_capacity("alice", "category1"))  # Output: 2

    # Accessing agent's items in a category
    print(custom_instance.agent_category_items("alice", "category1"))  # Output: {'item1'}

    # Accessing item's category
    print(custom_instance.item_category("item1"))  # Output: category1

    # printing all item list
    print(custom_instance.get_items())


def example2():
    valuations = {"Alice": {"c1": 11, "c2": 22}, "Bob": {"c1": 33, "c2": 44}}
    agent_capacities = {"Alice": {"category1": 2, "category2": 3}, "Bob": {"category1": 1, "category2": 2}}
    categories = {"Alice": {"category1": {"c1"}, "category2": {"c2"}},
                  "Bob": {"category1": {"c2"}, "category2": {"c1"}}}
    items = ["c1", "c2"]

    custom_instance = CustomInstance(valuations=valuations, agent_capacities=agent_capacities, categories=categories,
                                     item_categories=categories, items=items)

    alice_capacity_category1 = custom_instance.agent_category_capacity("Alice", "category1")
    print(alice_capacity_category1)  # Output: 2

    bob_items_category2 = custom_instance.agent_category_items("Bob", "category2")
    print(bob_items_category2)  # Output: {'c1'}

    # printing all item list
    print(custom_instance.get_items())


def main():
    example1()
    print("**************")
    example2()


if __name__ == "__main__":
    main()

# agent.py
from tools import search_space_facts

class Aryabot:
    def __init__(self):
        self.memory = {}

    def ask(self, query):
        fact = search_space_facts(query)
        simplified = self.simplify(fact)
        self.memory[query] = simplified
        return simplified

    def simplify(self, text):
        return f"Aryabot says: {text}"

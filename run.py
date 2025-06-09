from env.node import Node
from agents.attacker import AttackerAgent
from agents.defender import DefenderAgent
from core.simulation import run_simulation

# Create a list of simulated machines in the network
nodes = [
    Node(id="Node-1", services=["ssh", "http"]),
    Node(id="Node-2", services=["ftp"]),
    Node(id="Node-3", services=["http", "smtp"])
]

# Initialize the attacker and defender agents
attacker = AttackerAgent()
defender = DefenderAgent()

# Start the simulation loop
run_simulation(nodes, attacker, defender, rounds=10)

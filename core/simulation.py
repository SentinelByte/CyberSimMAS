def run_simulation(nodes, attacker, defender, rounds=10):
    """
    Simulate a series of attacker and defender actions over a number of rounds.
    :param nodes: List of Node objects in the environment
    :param attacker: Instance of AttackerAgent
    :param defender: Instance of DefenderAgent
    :param rounds: Number of simulation cycles to run
    """
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        for node in nodes:
            attacker.act(node)  # Attacker tries to exploit the node
            defender.act(node)  # Defender checks and responds

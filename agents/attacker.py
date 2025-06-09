class AttackerAgent:
    def __init__(self, known_services=["ssh", "http"]):
        """
        Initialize the attacker with knowledge of services it can exploit.
        :param known_services: List of services attacker will attempt to exploit
        """
        self.known_services = known_services

    def act(self, node):
        """
        Attempt to exploit each known service on the node.
        :param node: Target Node object
        """
        for svc in self.known_services:
            success = node.receive_attack(svc)
            if success:
                print(f"[Attacker] Compromised {node.id} via {svc}")
                break  # Stop once one service is successfully exploited

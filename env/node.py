class Node:
    def __init__(self, id, services, is_patched=False):
        """
        Initialize a node in the simulated network.
        :param id: Unique identifier for the node
        :param services: List of services running on the node (e.g., ['ssh', 'http'])
        :param is_patched: Whether the node has been patched (default: False)
        """
        self.id = id
        self.services = services
        self.is_patched = is_patched
        self.compromised = False
        self.logs = []  # Records attack attempts and system actions

    def receive_attack(self, service):
        """
        Simulate an attack attempt on a specific service.
        :param service: The target service to attack
        :return: True if the attack was successful, False otherwise
        """
        if not self.is_patched and service in self.services:
            self.compromised = True
            self.logs.append(f"Exploit on {service}")
            return True
        self.logs.append(f"Failed exploit on {service}")
        return False

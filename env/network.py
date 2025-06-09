from env.node import Node

def build_network(size=5):
    nodes = []
    for i in range(size):
        services = ["ssh", "http"] if i % 2 == 0 else ["ftp", "smtp"]
        node = Node(id=i, services=services)
        nodes.append(node)
    return nodes

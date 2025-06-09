def print_node_status(node):
    status = "COMPROMISED" if node.compromised else "SAFE"
    patched = "Yes" if node.is_patched else "No"
    print(f"[{node.id}] Status: {status}, Patched: {patched}")

def count_compromised(nodes):
    return sum(1 for node in nodes if node.compromised)

class DefenderAgent:
    def act(self, node):
        """
        Monitor logs and patch the node if signs of exploitation are detected.
        :param node: Target Node object
        """
        # Look for evidence of an exploit in the logs
        suspicious = any("Exploit" in log for log in node.logs)
        if suspicious:
            node.is_patched = True  # Patching is a simple fix in this model
            print(f"[Defender] Patched {node.id}")

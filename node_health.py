def count_nodes_states(nodes: list[dict]) -> dict:
    """Count how many nodes are ready, notready, and cordoned."""
    cordoned = 0
    notready = 0
    ready = 0
    for i in nodes:
        if i["unschedulable"] == True:
            cordoned += 1
        elif i["ready"] == False:
            notready += 1
        else:
            ready += 1
    return {"ready": ready, "notready": notready, "cordoned": cordoned}


def unhealthy_node_names(nodes: list[dict]) -> list[str]:
    """Return the names of nodes that are NotReady or Cordoned."""
    return [n["name"] for n in nodes if n.get("unschedulable") or not n.get("ready", False)]


if __name__ == "__main__":
    node1 = {"name": "worker-1", "ready": True, "unschedulable": False}
    node2 = {"name": "worker-2", "ready": False, "unschedulable": False}
    node3 = {"name": "worker-3", "ready": True, "unschedulable": True}
    nodes = [node1, node2, node3]
    print(count_nodes_states(nodes))
    print(unhealthy_node_names(nodes))

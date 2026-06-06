node1 = {"name": "worker-1", "ready": True, "unschedulable": False}
node2 = {"name": "worker-2", "ready": False, "unschedulable": False}
node3 = {"name": "worker-3", "ready": True, "unschedulable": True}
nodes = [node1, node2, node3]

ready = 0
notready = 0
cordoned = 0

for i in nodes:
    if i["unschedulable"] == True:
        cordoned += 1
    elif i["ready"] == True:
        ready += 1
    else:
        notready += 1

print(cordoned)
print(ready)
print(notready)


"""
You are tasked with building a simple Python tool that reads a JSON file containing Kubernetes pod information
and outputs a summary report of resource usage (CPU and memory). The tool should calculate the total and average
CPU and memory usage across all pods.

The JSON file represents a simplified snapshot of the "kubectl get pods -o json" output.

Requirements:
Input: A JSON file named pods.json which contains pod information.
Output: A summary report printed to the console.
    - Total CPU usage (sum of CPU for all pods)
    - Total Memory usage (sum of memory for all pods)
    - Average CPU usage (average CPU for all pods)
    - Average Memory usage (average memory for all pods)
Pod Information Structure: Each pod has the following structure in the JSON:
'''
{
    "pod_name": "pod-1",
    "namespace": "default",
    "containers": [
        {
            "container_name": "container-1",
            "cpu_usage": "100m",  // CPU usage in millicores
            "memory_usage": "200Mi"  // Memory usage in MiB
        },
        {
            "container_name": "container-2",
            "cpu_usage": "150m",
            "memory_usage": "300Mi"
        }
    ]
}
'''
* CPU usage is in milicores (100m = 0.1 core).
* Memory usage is in MiB (200Mi = 200 MiB).

Considerations:
The tool should handle multiple containers in a pod.
If the file is empty or the JSON structure is invalid, handle the error gracefully.
Messages addressed to "meeting group chat" will also appear in the meeting group chat in Team Chat
"""
# Expected output
# Total CPU Usage: 450m (0.45 cores)
# Total Memory Usage: 900Mi
# Average CPU Usage: 150m (0.15 cores)
# Average Memory Usage: 300Mi

from typing import List
import json

with open('file.json', 'r') as file:
    data = json.load(file)
    
def return_expected_data(ls_pods:List):
    ls_cpu_usage:List = []
    ls_tot_memory_usage:List = []

    for pod in ls_pods:
        for container in pod['containers']:
            ls_cpu_usage.append(int(container['cpu_usage'][0:3]))
            ls_tot_memory_usage.append(int(container['memory_usage'][0:3]))
            
    print(sum(ls_cpu_usage), sum(ls_tot_memory_usage), sum(ls_cpu_usage)// len(ls_cpu_usage))
            

return_expected_data(data)

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    n = len(gas)
    start_idx = float('inf')
    for i in range(n):
        canStart = gas[i]-cost[i]
        if canStart>=0:
            start_idx = i
            gas_tmp = gas[i:]+gas[:i]
            cost_tmp = cost[i:]+cost[:i]
            remain_gas = 0
            for j in range(n):
                remain_gas = remain_gas+gas_tmp[j]-cost_tmp[j]
                if remain_gas<0:
                    start_idx = float('inf')
                    break
            if start_idx != float('inf'):
                return start_idx
    return -1 

if __name__ == '__main__':
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas, cost))

    gas  = [2,3,4]
    cost = [3,4,3]
    print(canCompleteCircuit(gas, cost))
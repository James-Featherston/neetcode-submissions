class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 1000 * 100 + 1
        arr = [INF] * (n)
        arr[src] = 0
        for _ in range(k + 1):
            temp = arr.copy()
            for flight in flights:
                start = flight[0]
                end = flight[1]
                cost = flight[2]
                if arr[start] == INF:
                    continue
                if arr[start] + cost < temp[end]:
                    temp[end] = arr[start] + cost
            arr = temp

        return -1 if arr[dst] == INF else arr[dst]


        
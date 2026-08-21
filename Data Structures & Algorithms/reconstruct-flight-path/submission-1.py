class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = len(tickets)
        m = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            m[src].append(dst)
        
        res = ["JFK"]
        city = "JFK"
        def rec (flights, city):
            
            if flights == 0:
                return True
            if city not in m:
                return False
            options = m[city]
            for i, option in enumerate(options):
                options.pop(i)
                res.append(option)
                if rec(flights - 1, option):
                    return True
                res.pop()
                options.insert(i, option)
            return False
        
        rec(flights, city)
        return res
            


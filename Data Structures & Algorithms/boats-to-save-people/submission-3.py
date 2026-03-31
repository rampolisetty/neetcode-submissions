class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # Heaviest at last
        l = 0
        r = len(people) - 1
        res = 0 #Boats

        while l <= r:
            rem = limit - people[r]
            # Put heaviest right away
            r -= 1
            res += 1
            if rem >= people[l]:
                l += 1 # Shares same boat
        
        return res
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        count=0
        while(i<=j):
            if(i==j):
                count+=1
                break
            if(people[i]+people[j]<=limit):
                i=i+1
                j=j-1
                count+=1
                continue
            j=j-1
            count+=1
            
        return count
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        cnt = 0 
        n = len(seats)
        for i in range(n):
            cnt += abs(seats[i]-students[i])
        return cnt
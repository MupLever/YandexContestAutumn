class Solution:
    def time_of_existence(self, start_on, end_on) -> (int, int):
        MAX = (365, 12, 0, 23, 59, 59)
        MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        
        i = len(end_on) - 1
        while i >= 0:
            while start_on[i] > end_on[i]:
                if i == 2:
                    end_on[i] += MONTH[i]
                else:
                    end_on[i] += MAX[i]
                i -= 1
                end_on[i] -= 1
            i -= 1

        i = len(end_on) - 1
        while i >= 0:
            end_on[i] -= start_on[i]
            i -= 1
            
        count_seconds = end_on[5] + end_on[4] * 60 + end_on[3] * 3600
        count_day = end_on[2] + end_on[1] * MONTH[end_on[1]] + end_on[0] * 365
        return count_day, count_seconds
start_on = list(map(int, input().split(' ')))
end_on = list(map(int, input().split(' ')))

solution = Solution()
days, seconds = solution.time_of_existence(start_on, end_on)
print(f'{days} {seconds}')

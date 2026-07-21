class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            hasWarmer = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i]>=temperatures[j]:
                    count += 1
                else:
                    count += 1
                    result.append(count)
                    hasWarmer = True
                    break
            if not hasWarmer:
                result.append(0)
        return result
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
            sorted_worker=sorted(worker)
            jobs=zip(difficulty,profit)
            sorted_jobs=sorted(jobs)
            n=len(sorted_jobs)
            best_profit=0
            total_best_profit=0
            i=0
            for skill in sorted_worker:
                while i<n and skill>=sorted_jobs[i][0]:
                    best_profit=max(best_profit, sorted_jobs[i][1])
                    i+=1
                total_best_profit+=best_profit
            return total_best_profit        

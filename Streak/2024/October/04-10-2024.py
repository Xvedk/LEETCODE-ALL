class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the skills
        skill.sort()
        
        # Total skill of each team
        target_sum = skill[0] + skill[-1]
        
        total_chemistry = 0
        n = len(skill)
        
        # Try to pair the players with the same total skill
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1  # If any pair doesn't match the target sum, return -1
            # Add the product (chemistry) of this team
            total_chemistry += skill[i] * skill[n - 1 - i]
        
        return total_chemistry

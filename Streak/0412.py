class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""  # Initialize an empty string to store the result
        empty = ""  # Initialize an empty string for a special case
        temp = 0  # Initialize a variable to store the largest digit found
        check = True  # Initialize a flag to check for a specific condition

        # Loop through the string to find the largest digit occurring thrice consecutively
        for i in range(len(num) - 2):
            # Check if the current digit is the same as the next two digits
            if i + 2 < len(num) and num[i] == num[i + 1] == num[i + 2]:
                # Convert the character digit to its integer equivalent and update 'temp'
                temp = max(temp, int(num[i]))
                check = False  # Update the flag to indicate the condition was met

        # If the condition was met (i.e., a triplet was found)
        if not check:
            # Append the largest digit found three times to the 'ans' string
            ans += str(temp) * 3

        else:  # If no such triplet found
            return empty  # Return the empty string

        return ans  # Return the result containing the largest good integer

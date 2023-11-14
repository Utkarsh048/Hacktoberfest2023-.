class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        for char in set(s):
            first_occurrence = s.index(char)
            last_occurrence = s.rindex(char)

            unique_chars_between = set(s[first_occurrence+1:last_occurrence])

            result += len(unique_chars_between)

        return result

# Example usage:
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))  # Output: 3
print(solution.countPalindromicSubsequence("adc"))    # Output: 0
print(solution.countPalindromicSubsequence("bbcbaba"))  # Output: 4

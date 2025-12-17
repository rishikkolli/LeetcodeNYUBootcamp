class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []
        p_count = [0] * 26
        window = [0] * 26

        # Build frequency count for p
        for c in p:
            p_count[ord(c) - ord('a')] += 1

        left = 0
        for right in range(len(s)):
            # Add current character to window
            window[ord(s[right]) - ord('a')] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            # If window matches p frequency, record start index
            if window == p_count:
                result.append(left)

        return result

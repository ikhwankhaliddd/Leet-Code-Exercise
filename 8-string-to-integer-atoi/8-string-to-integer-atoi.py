class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)',s)
        return min(max((int(match.group(1)) if match else 0), -2**31), 2**31 - 1)
        
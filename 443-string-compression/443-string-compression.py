class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars) :
            count = 1
            chars[slow] = chars[fast]
            slow += 1
            while fast < len(chars) -1 and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1
            
            if count > 1:
                for c in str(count):
                    chars[slow] = c
                    slow += 1
            fast += 1 
        return slow
        
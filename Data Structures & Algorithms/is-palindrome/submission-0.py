class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.lower()

        left = 0
        right = len(cleaned) - 1

        while left < right:
            ascii_l = ord(cleaned[left])
            ascii_r = ord(cleaned[right])

            if (ascii_l < 97 or ascii_l > 122) and (ascii_l < 48 or ascii_l > 57):
                left += 1

            elif (ascii_r < 97 or ascii_r > 122) and (ascii_r < 48 or ascii_r > 57):
                right -= 1

            else:
                if cleaned[left] != cleaned[right]:
                    return False

                if cleaned[left] == cleaned[right]:
                    left += 1
                    right -= 1

        return True




























        # cleaned = ""
        # for char in s:
        #     if char.isalnum():
        #         cleaned += "".join(char.lower())
        # print(cleaned)

        # low = 0
        # high = len(cleaned) - 1
        # while low < high:
        #     if cleaned[low] != cleaned[high]:
        #         return False
        #     else:
        #         low+=1
        #         high-=1
        # return True

        
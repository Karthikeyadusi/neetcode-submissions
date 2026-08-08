class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        temp = s
        item = ""
        decoded = []
        num = ""
        i = 0
        while i < len(s):
            if 47 < ord(s[i]) < 59:
                num+=s[i]
                i+=1
            if s[i] == "#":
                j = i+1
                while j < (i+1+(int(num))):
                    item += s[j]
                    j+=1
                i = j
                decoded.append(item)
                num = ""
                item = ""
        return decoded

                    




        
        

        

        
        

class Solution:
    def makeFancyString(self, s: str) -> str:
        result=[]
        count=0
        prev=""
        for char in s:
            if char==prev:
                count+=1
            else:
                count=1
            if count<=2:
                result.append(char)
            prev=char

        return "".join(result)




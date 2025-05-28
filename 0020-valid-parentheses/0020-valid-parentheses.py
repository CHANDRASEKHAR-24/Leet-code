class Solution(object):
    def isValid(self, s) :
        stack=[]
        bracket_pairs = { ')' : '(' , ']' : '[' , '}' : '{' }

        for ch in s :
            if ch in bracket_pairs:
                if not stack or stack[-1] != bracket_pairs[ch]:
                    return False
                stack.pop()

            else:
                stack.append(ch)
        return not stack



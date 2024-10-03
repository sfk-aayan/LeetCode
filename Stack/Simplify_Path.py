class Solution:
    def simplifyPath(self, path: str) -> str:
        dCheck = ('.','..')

        pLen = len(path)

        if pLen == 1 and path[0] == "/":
            return "/"

        stack = []
        curr = ""
        
        for char in path + "/":
            if char == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += char
        
        return "/" + "/".join(stack) 


        
        
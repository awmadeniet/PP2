class Solution:
    def interpret(self, command: str) -> str:
        ns = ""
        for i in range(len(command)):
            if "(" == command[i] and ")" == command[i + 1]:
                ns = ns + "o"
            elif "(" == command[i] and ")" != command[i + 1]:
                ns = ns + ""
            elif ")" == command[i]:
                ns = ns + ""
            else:
                ns = ns + command[i]
        return ns
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        length = 0

        i = 0

        while i < len(words):

            if length + len(line) + len(words[i]) > maxWidth:

                whites = maxWidth - length
                spaces = whites // max(1, (len(line) - 1))
                remainder = whites % max(1, (len(line) - 1))

                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces

                    if remainder:
                        line[j] += " "
                        remainder -= 1  
                
                result.append("".join(line))
                line = []
                length = 0
                continue

            line.append(words[i])
            length += len(words[i])
            i += 1

        last = " ".join(line)
        left_spaces = maxWidth - len(last)
        total_spaces = " " * left_spaces
        last += total_spaces
        result.append("".join(last))

        return result            
        
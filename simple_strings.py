
#Returns lexicographically smallest string after deleting exactly k characters from 
def lexicographically_smallest_string(s, k):
    out = []
    for c in s:
        while k > 0 and len(out) > 0 and c < out[-1]:
            out.pop(-1)
            k -= 1
        out.append(c)
    return ''.join(out)
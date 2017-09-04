def reverseWords(s):

    words = s.split(" ")
    rs = list()
    for word in words:
        rs.append(word[::-1])

    return " ".join(rs)

print reverseWords("Let's take LeetCode contest")
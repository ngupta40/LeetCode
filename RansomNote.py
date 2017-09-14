def canConstruct(ransomNote, magazine):
    if (len(ransomNote) > len(magazine)):
        return False
    elif (len(ransomNote) == 0):
        return True
    else:
        dict1 = dict()
        for char in ransomNote:
            if (dict1.has_key(char) == 0):
                dict1[char] = 1
            else:
                dict1[char] += 1
        for chars in magazine:
            if (dict1.has_key(chars)):
                if (dict1[chars] != 0): dict1[chars] -= 1

        if (sum(dict1.values()) == 0):
            return True
        else:
            return False


print canConstruct("fffbfg","effjfggbffjdgbjjhhdegh")
def merged_tow_strings(word1,word2):
    result = []
    len1 ,len2 = len(word1) , len(word2)
    i,j = 0,0
    while i<len1 and j<len2:
        result.append(word1[i])
        result.append(word2[j])
        i +=1
        j +=1
    if i<len1:
        result.extend(word1[i:])
    if j<len2:
        result.extend(word2[j:])
    merged_string = "".join(result)
    print(merged_string)
    return merged_string


merged_tow_strings("abcd","pqrs")
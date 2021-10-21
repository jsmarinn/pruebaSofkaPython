string1 = "ca_kdjfoa2, cd_fjaei3, ca_kjakjfd5, ce_fdkajkjl8, cd_ltlcvzc9"


def modifyString(sentence):
    string2 = ""
    for i in sentence.split(", "):
        if i[slice(0, 3)] == "ca_":
            string2 = string2 + i[slice(3, len(i))].upper() + ", "
        else:
            string2 = string2 + i + ", "
    string2 = string2.strip(", ")
    return [sentence, string2]


print(modifyString(string1)[0])
print(modifyString(string1)[1])

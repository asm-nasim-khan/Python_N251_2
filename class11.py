name = "HappyBirthday" #String
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# vowel = 0
# conso = 0
# for i in range(len(name)):
#     if name[i].lower() in "aeiou":
#         vowel = vowel + 1
#     else:
#         conso = conso + 1

# print(vowel)
# print(conso)

# print("ABCD".lower())
# print("pqrst".upper())
# words = "Throughout the Divine Comedy, Dante is concerned with the ways in which selfishness destroys the social fabric. He details how people pay for that selfishness in Hell or by having to trudge up the seven terraces of Mount Purgatory. But Dante isn’t only interested in what happens after death, he is also talking about how we live while on earth. His life was destroyed by the petty grudges of partisan politics. As an exile, he was under constant threat of death. He takes great risks in writing his poem because he hopes that by addressing the greed and megalomania that is destroying Italy, he can help put a stop to it. He also knows that this is not a time-limited problem but a timeless one, which is why he wrote the poem in the vernacular—so that, unlike poems written in literary Latin, it would change over time. He said he was also writing his poem in the vernacular so that it could be read by everyone. That is why I translated the poem into the American vernacular."
# word_list = words.split("\n")
# for i in range(len(word_list)):
#     print(i,":",word_list[i].split(" "))

# name = "HappyBirthday" #String
# # print(name[len(name)-1:3:-1]) #slicing [start(including):stop(excluding)]
# print(name[-1])


line = "I love Python"
output = "I lOvE pYtHoN"
start = 0
end = len(line)
count = 0
while start<end:
    if line[start] != " ":
        if count % 2 == 0:
            print(line[start].upper(),end="")
        else:
            print(line[start].lower(),end="")
        count = count + 1
    else:
        print(line[start],end="")
    start = start + 1

print()
print(count)
print(start)

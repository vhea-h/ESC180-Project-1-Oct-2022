import synonyms as s

# cos_sim = s.cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6})
# cos2 = s.cosine_similarity({"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}, {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})
# print(cos_sim)
# print(cos2)

# NFU = [["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]

# print(s.build_semantic_descriptors(NFU)["man"])

# print(s.build_semantic_descriptors_from_files(["ugh.txt"]))
sem_descriptors = s.build_semantic_descriptors_from_files(["ugh.txt"])
print(sem_descriptors)
res = s.run_similarity_test("test.txt", sem_descriptors, s.cosine_similarity)
print(res, "percent of guesses were correct")
#print(s.run_similarity_test("test.txt", lul_dic, s.cosine_similarity))

# def test_build_semantic_descriptors(self):
#     sentences = [["i", "am", "a", "sick", "man"],
#     ["i", "am", "a", "spiteful", "man"],
#     ["i", "am", "an", "unattractive", "man"],
#     ["i", "believe", "my", "liver", "is", "diseased"],
#     ["however", "i", "know", "nothing", "at", "all", "about", "my",
#     "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
#     sem_desc = s.build_semantic_descriptors(sentences)
#     a1 = self.assertEqual(sem_desc["man"], {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1})
#     a2 = self.assertEqual(sem_desc["liver"], {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})

# sentences = [["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
# sem_desc = s.build_semantic_descriptors(sentences)
# print(sem_desc["man"] == {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1})
# print(sem_desc["liver"] == {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})

# f1 = open("text1.txt", "w")
# f2 = open("text2.txt", "w")
# f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\n")
# f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
# f1.close()
# f2.close()

# sem_desc = s.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
# print(sem_desc["man"])
# print(sem_desc["man"] == {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1})
# print(sem_desc["liver"] == {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})

# print(sem_desc["nothing"]["ails"] == 1)

# f1 = open("text1.txt", "w")
# f2 = open("text2.txt", "w")
# f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased\n")
# f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
# f1.close()
# f2.close()

# f3 = open("test.txt", "w")
# f3.write("man i liver i\nsick man certain man")
# f3.close()
# sem_desc =  s.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
# res =  s.run_similarity_test("test.txt", sem_desc,  s.cosine_similarity)
# print(res)
# print(res == 100.0)
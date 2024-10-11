text = input()
words = text.lower().split()  # Преобразуем в нижний регистр и разделяем по пробелам
word_counts = {}
for word in words:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1

for word, count in word_counts.items():
  print(f"{word} {count}")



# put your python code here
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
from __future__ import annotations

from Utilities import cleanWord

word = "His existence So question reversed Why cant assume universe exists assume God exist Why must universe It may one day man create life also create man Now I dont see happening lifetime I assert probable But possibility given scientist working hard decoding genetic code perhaps help cure disease genetic variation Again though must divine prupose man existence As far tell man fall mammal catagory Now something man say soul yet find evidence But man mammal baby born live mother give milk warmblooded etc mammal similar genetic construction particular primate For check talkorigins Well Buddhism Confucianism Taoism Hinduism Judaism Zoerasterism Shintoism Islam fit bit logic quite nicely All depth enduring value thus must true Stephen Atheist Libertarian Proindividuality Proresponsibility Jr jazz"
(cleanWord(word))

categories = ['soc.religion.christian']

from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train',
    categories=categories, shuffle=True, random_state=42)


(cleanWord(twenty_train.data[7]))

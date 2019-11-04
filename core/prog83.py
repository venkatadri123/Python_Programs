# Retrive only the first letter of each word in a list.
words=['hyder','secunder','pune','goa','vellore','jammu']
lst=[]
for ch in words:
    lst.append(ch[0])
print(lst)

# To convert into List Comprehension.

lst=[ch[0] for ch in words]
print(lst)

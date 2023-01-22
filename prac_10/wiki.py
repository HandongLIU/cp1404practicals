import wikipedia

searchs = input("input search: ")
while searchs == "":
    searchs = input("input search")
print(wikipedia.search(searchs))

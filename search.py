try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


urls = []
# to search
def Google(query,deph): 
    for j in search(query, tld="co.in", num=deph, stop=deph, pause=2):
        print(j)
        urls.append(j)
    return urls
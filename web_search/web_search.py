import webbrowser

def google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)


user_query =input('input your search query')
google_search(user_query)
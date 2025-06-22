import requests

class Search:

    def get_user_search_results(self, search_term):
        try:
            search_term_formatted = search_term.replace(" ", "+")
            fields = ["title", "author_name"]
            fields_formatted = ",".join(fields)
            limit = 1

            URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

            response = requests.get(URL)
            response.raise_for_status()

            data = response.json()

            if not data['docs']:
                return "No results found."

            title = data['docs'][0].get('title', 'Unknown')
            authors = data['docs'][0].get('author_name', ['Unknown'])

            return f"Title: {title}\nAuthor: {authors[0]}"
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("\nSearch Result:\n")
    print(result)

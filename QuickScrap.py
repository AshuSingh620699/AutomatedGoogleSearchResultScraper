import requests
from bs4 import BeautifulSoup as BS

def google_search(query, num_results=10):
    baseUrl = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(baseUrl, headers=headers, params=params)

    if response.status_code != 200:
        print("Failed to retrieve results!")
        return []

    soup = BS(response.text, "html.parser")
    results = []  # Correctly define as a list to store the results

    for result in soup.select('.tF2Cxc'):
        title = result.select_one('h3')
        link = result.select_one('a')
        desc = result.select_one('.VwiC3b')

        if title and link and desc:
            # Append the dictionary to the list
            results.append({
                "title": title.get_text(),
                "link": link['href'],
                "desc": desc.get_text()
            })

    if not results:
        print("No results found!")

    return results


query = input("Search here! to get link..")
results = google_search(query)

for i, result in enumerate(results, start=1):
    print(f"{i}. {result['title']}")
    print(f"    Link: {result['link']}")
    print(f"    Description: {result['desc']}\n")

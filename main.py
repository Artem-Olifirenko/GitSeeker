import requests
import sys
import os
import logging

logging.basicConfig(level=logging.INFO)

def search_github_repositories(access_token, query, per_page=10, page=1):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"q": query, "per_page": per_page, "page": page}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        response.raise_for_status()

def main():
    if "GITHUB_ACCESS_TOKEN" not in os.environ:
        logging.error("GitHub access token not found in environment variables.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python main.py <search_query> [per_page] [page]")
        sys.exit(1)

    access_token = os.environ["GITHUB_ACCESS_TOKEN"]
    search_query = sys.argv[1]
    per_page = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    page = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    try:
        logging.info("Searching GitHub repositories...")
        repositories = search_github_repositories(access_token, search_query, per_page, page)
        for repo in repositories:
            print(f"Name: {repo['name']}\nURL: {repo['html_url']}\nDescription: {repo.get('description', 'No description')}\n")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

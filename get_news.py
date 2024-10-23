import os
import requests
from dotenv import load_dotenv

# Initialize a global variable to store articles and an index
articles = []
current_article_index = 0


def fetch_news():
    global articles
    load_dotenv()
    api_key = os.environ.get("news_api")
    url = f"https://newsapi.org/v2/everything?q=apple&from=2024-10-07&to=2024-10-07&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])


def get_news():
    global current_article_index
    # Check if articles are loaded, if not, fetch them
    if not articles:
        fetch_news()

    # Get the current article
    if articles:
        article = articles[current_article_index]
        title = article.get("title", "No title available")
        description = article.get("description", "No description available")
        content = article.get("content", "No content available")  # Full content of the article
        author = article.get("author", "Unknown author")
        published_at = article.get("publishedAt", "Unknown date")
        source_name = article.get("source", {}).get("name", "Unknown source")

        # Format the article to include full content and a divider
        news_content = (
                f"Title       : {title}\n"
                f"Description : {description}\n"
                f"Content     : {content}\n"
                f"Author      : {author}\n"
                f"Published At: {published_at}\n"
                f"Source      : {source_name}\n"
                + "-" * 50
        )

        # Update index for the next call
        current_article_index = (current_article_index + 1) % len(articles)
        return news_content
    else:
        return "No articles found or an error occurred."

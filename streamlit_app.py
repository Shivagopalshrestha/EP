import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from plyer import notification

def get_stock_split_news():
    url = "https://finance.yahoo.com/splits"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_elements = soup.select(".Mb(0.5em) .Mb(0) a")
        
        news = []
        for element in news_elements:
            news.append(element.text.strip())
        
        return news

    return None

def send_notification(news):
    title = "Stock Split News"
    message = "\n".join(news)

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def main():
    while True:
        try:
            news = get_stock_split_news()
            
            if news:
                print(f"\n[{datetime.now()}] Stock Split News:\n{news}")
                send_notification(news)
        except Exception as e:
            print(f"An error occurred: {e}")

        # Sleep for 5 minutes before checking again
        sleep(300)

if __name__ == "__main__":
    main()

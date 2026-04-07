from datetime import datetime, timedelta

def is_recent_article(pub_date_str):
    """Check if article was published in the last 24 hours"""
    # Parse RSS pubDate format: "Tue, 07 Apr 2026 13:25:32 +0000"
    pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")

    # Get today and yesterday's dates
    today = datetime.now().date()
    yesterday = (datetime.now() - timedelta(days=1)).date()

    # Check if published today or yesterday
    return pub_date.date() in [yesterday, today]

def exp():
    # Test cases
    test_dates = [
        "Tue, 07 Apr 2026 13:25:32 +0000",  # Today
        "Mon, 06 Apr 2026 23:30:00 +0000",  # Yesterday evening
        "Sun, 05 Apr 2026 10:00:00 +0000",  # Two days ago
    ]

    for date_str in test_dates:
        result = is_recent_article(date_str)
        print(f"{date_str}: {result}")

if __name__ == "__main__":
    exp()
    
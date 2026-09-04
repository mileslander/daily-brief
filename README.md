# Daily Brief

OpenClaw inspired and token optimized daily brief telegram messaging script. Collects daily news, personal schedule, and weather data which is compiled and formatted by Claude Code and then sent to a telegram bot.

## Data Aggregation

Data is aggregated from the following sources into a .txt file.

### News

Collects news from [The New York Times RSS Feeds](https://www.nytimes.com/rss), [BBC Tennis](https://feeds.bbci.co.uk/sport/tennis/rss.xml) and [Hacker News](https://news.ycombinator.com/rss). Filters stories by publications date, within the last 24 hours, and extracts their descriptions.

### Schedule

Calls Google Calendar API for daily schedule.

### Weather

Current weather conditions are collected from [weatherapi.com](https://www.weatherapi.com) API.

## Claude Code Call

Claude Code parses and formats the data for telegram messaging according to [CLAUDE.md](./CLAUDE.md).

## Telegram

The formatted brief is sent to a telegram bot using a Telegram Bot API.

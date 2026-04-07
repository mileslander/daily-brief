# Daily Brief

OpenClaw inspired and token optimized daily brief telegram messaging script. Collects daily news, personal schedule, and weather data which is compiled and formatted by Claude Code and then sent to a telegram bot.

## Data Aggregation

### News

Collects news from [The New York Times RSS Feeds](https://www.nytimes.com/rss). Stories are filtered by publications date, within the last 24 hours, and then their descriptions are collected in a .txt file.

### Schedule

Calls Google Calendar API for daily schedule which is aggregated with other data.

### Weather

Current weather conditions are collected from [weatherapi.com](https://www.weatherapi.com) API and aggregated with other data.

## Claude Code Call

Claude Code is called and parses and formats the data for telegram messaging according to [CLAUDE.md](./CLAUDE.md).

## Telegram

The formatted brief is sent to a telegram bot using a Telegram Bot API.

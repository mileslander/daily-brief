# Daily Brief

Instructions for Claude to generate daily report including daily news updates, weather forecast, and schedule. All of the data is collected in rss.txt. Don't include any filler words or transitional phrases.

## Formatting

This is to be sent as a text message through a telegram bot and to be formatted accordingly for mobile messaging.

### Weather

The brief should start with todays date followed by the weather on a new line. This should be one short line about the weather. Temperature and precipitation only. Do not include other information unless it is highly atypical. Include a short second line, a casual human remark about the weather.

### Schedule

The weather is to be followed by my schedule with each event on a new line in the format "TIME - EVENT" (e.g., "8:00 AM - Team standup"). Only include if there are events, if no events exist write "No Events Today" as a plain line.

### News

Finally, include a short summary of the days news. Group stories under bold topics headers, using Telegram markdown bold: *Topic Name*, use title case not all caps. Focus on major stories, tech, and sports. Skip entertainment and celebrity news. Use dashes not bullet points. At most two lines per story. Include a maximum of 10 stories.

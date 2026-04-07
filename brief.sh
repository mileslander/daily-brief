#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

python3 data.py > rss.txt

BRIEF=$(claude --print "Generate my daily brief according to CLAUDE.md from rss.txt")


python3 -c "
import requests
requests.post('https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage', 
    json={'chat_id': '8212507901', 'text': '''$BRIEF''', 'parse_mode': 'Markdown'})
"
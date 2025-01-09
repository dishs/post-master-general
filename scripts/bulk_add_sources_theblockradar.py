import common.sources as sources
import common.platforms as platforms
from datetime import datetime

# channels = [
#   {
#     "title": "",
#     "url": "",
#     "keywords": "",
#   }
# ]

channels = [
  {
    "title": "Mike Korzemba",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCp3dgMf1OUP2XqOpyOY2bzQ",
    "keywords": "",
    "channel_id": "UCp3dgMf1OUP2XqOpyOY2bzQ",
    "thumbnail": "https://yt3.googleusercontent.com/ytc/AIdro_nZ6sPLDsqmDevD_1qPf4NGOxyKFTjjCkokAlnSEgbYQko=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@MikeKorzemba"
  },
  {
    "title": "",
    "url": "",
    "keywords": "",
    "channel_id": "",
    "thumbnail": "",
    "custom_url": "@"
  },
  {
    "title": "",
    "url": "",
    "keywords": "",
    "channel_id": "",
    "thumbnail": "",
    "custom_url": "@"
  },
]


genre = "Cryptocurrency"

for channel in channels:
  channel['prompt_video'] = f"Please summarize in 3 paragraphs, for a blog post, with a playfully sarcastic and witty tone, this Youtube video transcript for a youtube channel named {channel['title']} in the {genre} genre for a blog post as a loyal fan. Utilize the following keywords for SEO: {channel['keywords']}.  Assume you are writing for a familiar audience.  Don't use 'he', 'I', 'we' or 'you', refer to the channel as {channel['title']} mostly.  You are not {channel['title']}.  Don't mention sponsors of the video. "
  channel['prompt_comments'] = f"Please summarize these comments for a youtube video by {channel['title']} in the {genre} genre.  Point out anything that might be of interest that you would have to watch the video to know.  Analyze what the viewers are thinking in as many bullet points are necessary.  Format the response for a blog post.  Do not sound like a robot or AI."
  channel['active'] = True
  channel['pending'] = False
  channel['authority'] = 1
  channel['owner'] = "editorcuts"
  channel['platform_id'] = platforms.getPlatformIdByTitle('Youtube')['_id']
  channel['createdAt'] = datetime.utcnow()
  sources.createNewSource(channel)




import json

channels = [
    {
        "title": "Coin Bureau",
        "subscribers": "2.32M",
        "channel_id": "UCqK_GSMbpiV8spgD3ZGloSw",
        "seo_keywords": "crypto,bitcoin,altcoins,blockchain,ethereum,cryptocurrency news,crypto analysis,defi,investing,finance"
    },
    {
        "title": "BitBoy Crypto",
        "subscribers": "1.45M",
        "channel_id": "UCjemQfjaXAzA-95RKoy9n_g",
        "seo_keywords": "crypto,bitcoin,altcoins,blockchain,ethereum,analysis,trading,investment,cryptocurrency news,defi"
    },
    {
        "title": "Altcoin Daily",
        "subscribers": "1.32M",
        "channel_id": "UCnWo4CzbHPwEfB5Arm2gQiw",
        "seo_keywords": "crypto,bitcoin,altcoins,cryptocurrency news,analysis,trading,price predictions,ethereum,blockchain,finance"
    },
    {
        "title": "Benjamin Cowen",
        "subscribers": "770K",
        "channel_id": "UCja77J8gL_3FVDPKACa5VUw",
        "seo_keywords": "crypto,bitcoin,analysis,ethereum,blockchain,data science,technical analysis,altcoins,investing,finance"
    },
    {
        "title": "Sheldon Evans",
        "subscribers": "740K",
        "channel_id": "UCU-6Bor5y8KLonqOD3s3yAA",
        "seo_keywords": "crypto,blockchain,nfts,ethereum,bitcoin,finance,altcoins,investing,cryptocurrency news,defi"
    },
    {
        "title": "Real Vision Finance",
        "subscribers": "677K",
        "channel_id": "UCpKX1wCJ5c9HGPSXsHaE_Og",
        "seo_keywords": "finance,macro,investing,crypto,bitcoin,blockchain,interviews,economics,analysis,markets"
    },
    {
        "title": "Crypto R Us",
        "subscribers": "650K",
        "channel_id": "UCJgHmpwK_CUu_7i1b7D6rCA",
        "seo_keywords": "crypto,bitcoin,ethereum,altcoins,analysis,defi,cryptocurrency news,trading,hodl,market updates"
    },
    {
        "title": "EllioTrades",
        "subscribers": "610K",
        "channel_id": "UCo-_O6cdR52WQ5T8pMcA0Vg",
        "seo_keywords": "crypto,bitcoin,altcoins,ethereum,investing,nfts,metaverse,defi,analysis,blockchain"
    },
    {
        "title": "Crypto Banter",
        "subscribers": "586K",
        "channel_id": "UCRr2SPNypaMZzLYr8uXKSWQ",
        "seo_keywords": "crypto,bitcoin,altcoins,blockchain,trading,analysis,news,ethereum,investing,defi"
    },
    {
        "title": "Anthony Pompliano",
        "subscribers": "579K",
        "channel_id": "UCgE46TG0RwAkaolFgH0NPAg",
        "seo_keywords": "crypto,bitcoin,finance,entrepreneurship,blockchain,investing,tech,interviews,economics,business"
    },
    {
        "title": "The Moon",
        "subscribers": "558K",
        "channel_id": "UCtfY2aZl4-Zr2Z_2eDHUU7Q",
        "seo_keywords": "crypto,bitcoin,ethereum,analysis,price predictions,defi,market updates,trading,blockchain,news"
    },
    {
        "title": "DataDash",
        "subscribers": "516K",
        "channel_id": "UCezQOD3Lq1htE4UK6zYZyXw",
        "seo_keywords": "crypto,bitcoin,economics,blockchain,data science,investing,altcoins,analysis,ethereum,finance"
    },
    {
        "title": "Ivan on Tech",
        "subscribers": "500K",
        "channel_id": "UCyI7FNTudkyALBh9N7hwI9Q",
        "seo_keywords": "crypto,blockchain,bitcoin,smart contracts,ethereum,analysis,development,defi,tech,investing"
    },
    {
        "title": "Lark Davis",
        "subscribers": "483K",
        "channel_id": "UC9Coi2KZAdG6NG1nUZf0Utg",
        "seo_keywords": "crypto,bitcoin,ethereum,altcoins,investing,blockchain,news,analysis,defi,finance"
    },
    {
        "title": "Crypto Casey",
        "subscribers": "405K",
        "channel_id": "UCPvWTJI1INHM4Irs0TQLXhA",
        "seo_keywords": "crypto,bitcoin,education,beginners,blockchain,ethereum,investing,safety,defi,news"
    },
    {
        "title": "Crypto Daily",
        "subscribers": "319K",
        "channel_id": "UC67AeejEYDSB8FrTd1z5h7w",
        "seo_keywords": "crypto,bitcoin,comedy,altcoins,news,blockchain,roasts,commentary,ethereum,analysis"
    },
    {
        "title": "Chico Crypto",
        "subscribers": "315K",
        "channel_id": "UC6r4krKnxxfGHZgAVAwn2jQ",
        "seo_keywords": "crypto,bitcoin,altcoins,ethereum,defi,analysis,blockchain,news,trading,dex"
    },
    {
        "title": "Crypto Zombie",
        "subscribers": "288K",
        "channel_id": "UCGm0wq2ODGxvGgU6k2ZPfhw",
        "seo_keywords": "crypto,bitcoin,analysis,ethereum,technical analysis,market trends,blockchain,altcoins,trading,news"
    },
    {
        "title": "Boxmining",
        "subscribers": "277K",
        "channel_id": "UCx4ZGkAEsHpNx7U0b8cYDug",
        "seo_keywords": "crypto,bitcoin,blockchain,news,interviews,projects,altcoins,technology,analysis,investing"
    },
    {
        "title": "The Modern Investor",
        "subscribers": "259K",
        "channel_id": "UC-2DOTP5HVKSvPyky2bD9Bw",
        "seo_keywords": "crypto,bitcoin,blockchain,news,market updates,analysis,altcoins,investing,hodl,finance"
    },
    {
        "title": "The Blockchain Backer",
        "subscribers": "251K",
        "channel_id": "UCp7iFZJ-Yf8ZJCD6bMOJTcw",
        "seo_keywords": "crypto,bitcoin,altcoins,technical analysis,xrp,ethereum,charts,blockchain,trading,investing"
    },
    {
        "title": "Tyler S",
        "subscribers": "210K",
        "channel_id": "UC0idWe2c4qHnjlQ9Z1NNaVQ",
        "seo_keywords": "crypto,bitcoin,market updates,ethereum,analysis,trading,finance,blockchain,altcoins,defi"
    },
    {
        "title": "The Bearable Bull",
        "subscribers": "147K",
        "channel_id": "UC2TI6jQJm9HQV6jM01b8XPA",
        "seo_keywords": "crypto,bitcoin,xrp,ripple,news,analysis,investing,blockchain,finance,defi"
    },
    {
        "title": "crypt0",
        "subscribers": "137K",
        "channel_id": "UCd4FnrMh3mNS2ncQ-SaaVVA",
        "seo_keywords": "crypto,bitcoin,ethereum,blockchain,news,mining,tech,analysis,altcoins,trading"
    },
    {
        "title": "Tone Vays",
        "subscribers": "125K",
        "channel_id": "UCGTTzWN5rK3siw8EccEaWYA",
        "seo_keywords": "crypto,bitcoin,analysis,trading,blockchain,technical analysis,finance,markets,investing,news"
    }
]

print(json.dumps(channels, indent=2))

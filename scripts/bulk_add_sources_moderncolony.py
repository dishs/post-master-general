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


genre = "Real Estate"

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



channels = [
    {
        "title": "Graham Stephan",
        "subscribers": "4.45M",
        "channel_id": "UCV6KDgJskWaEckne5aPA0aQ",
        "seo_keywords": "real estate,investing,personal finance,property,housing market,entrepreneurship,wealth building,rentals,flipping,mortgages"
    },
    {
        "title": "Enes Yilmazer",
        "subscribers": "4.02M",
        "channel_id": "UCETVcPlDqm5dBdGG3OBxhBQ",
        "seo_keywords": "luxury real estate,house tours,architecture,property walkthroughs,interior design,investing,high end homes,mansion tours,construction,lifestyle"
    },
    {
        "title": "Manny Khoshbin",
        "subscribers": "2.52M",
        "channel_id": "UCEyyub2lIYxyB7n44wTOT6A",
        "seo_keywords": "real estate,investing,luxury cars,commercial property,business,entrepreneurship,money,success,wealth,flipping"
    },
    {
        "title": "Grant Cardone",
        "subscribers": "2.47M",
        "channel_id": "UCnyx8Hjd4WQKfX3Cd6tH6xw",
        "seo_keywords": "real estate,investing,10x,entrepreneurship,multifamily,wealth,sales,property,grit,success"
    },
    {
        "title": "Meet Kevin",
        "subscribers": "1.86M",
        "channel_id": "UCNY3gWvKFikZ3I2ZUzH7vTg",
        "seo_keywords": "real estate,investing,personal finance,stock market,economics,flipping,landlording,wealth building,business,entrepreneurship"
    },
    {
        "title": "Ryan Serhant",
        "subscribers": "1.38M",
        "channel_id": "UCgT6BO0P9mOrY2R5LCmB2ZQ",
        "seo_keywords": "real estate,luxury homes,brokerage,high-end listings,property tours,sales,negotiation,NYC,marketing,success"
    },
    {
        "title": "BiggerPockets",
        "subscribers": "881K",
        "channel_id": "UC9TYZFX7Z0G3cY2UEb2pDgA",
        "seo_keywords": "real estate,investing,rentals,wholesaling,house hacking,flipping,podcasts,landlording,finance,wealth"
    },
    {
        "title": "Kris Krohn",
        "subscribers": "810K",
        "channel_id": "UCykzCbbX8GqaMU6klncvx7Q",
        "seo_keywords": "real estate,investing,motivation,personal development,wealth creation,financial freedom,property,entrepreneurship,mentoring,flipping"
    },
    {
        "title": "Ben Mallah",
        "subscribers": "750K",
        "channel_id": "UC7QpXeQPpE2gUF3XJlfulTg",
        "seo_keywords": "real estate,investing,lifestyle,big deals,flipping,commercial property,money,negotiations,landlording,wealth"
    },
    {
        "title": "Glenda Baker",
        "subscribers": "660K",
        "channel_id": "UC-c48Cv6Ka5kzobIECUUp9Q",
        "seo_keywords": "realtor,tips and tricks,home buying,home selling,negotiation,market insights,property,staging,client advice,marketing"
    },
    {
        "title": "Jerry Norton (Flipping Mastery TV)",
        "subscribers": "530K",
        "channel_id": "UCv7EaPKkQLz7tQm3lvHQb1g",
        "seo_keywords": "flipping,real estate,wholesaling,investing,property deals,renovations,strategies,education,mentoring,housing market"
    },
    {
        "title": "Phil Pustejovsky",
        "subscribers": "500K",
        "channel_id": "UCkYYZ0MTY08Z7fFbSy5MChw",
        "seo_keywords": "real estate,coaching,investment,flipping,foreclosures,creative financing,mentor,wholesale,wealth building,property"
    },
    {
        "title": "Coach Carson",
        "subscribers": "410K",
        "channel_id": "UCfNgWJCD9GjmfNoCYogmR7A",
        "seo_keywords": "real estate,investing,retire early,house hacking,rentals,financial independence,landlording,flipping,education,wealth"
    },
    {
        "title": "Samuel Leeds",
        "subscribers": "400K",
        "channel_id": "UCS6SES6btXx2tVFzWyK65eA",
        "seo_keywords": "real estate,UK investing,rent to rent,deal sourcing,property training,wealth,entrepreneurship,strategies,success,flipping"
    },
    {
        "title": "Ken McElroy",
        "subscribers": "379K",
        "channel_id": "UC2ju7kRfAnzo4Kevxvf3mhw",
        "seo_keywords": "real estate,investing,multifamily,rentals,finance,wealth building,business,economics,property,buy and hold"
    },
    {
        "title": "Max Maxwell",
        "subscribers": "350K",
        "channel_id": "UCXofllU6NMQY3shULa_hOAA",
        "seo_keywords": "wholesaling,real estate,investing,flipping,negotiation,contracts,entrepreneurship,marketing,building wealth,motivation"
    },
    {
        "title": "Ricky Carruth",
        "subscribers": "280K",
        "channel_id": "UCCgCrYa51o9EJ2-jlYox51Q",
        "seo_keywords": "real estate agent,coaching,sales,lead generation,marketing,buyers,sellers,negotiation,prospecting,mentoring"
    },
    {
        "title": "Chandler David Smith",
        "subscribers": "230K",
        "channel_id": "UCEM_4qCI5KgEYe-BPhl_RpQ",
        "seo_keywords": "real estate,investing,rentals,flips,wholesaling,house hacking,money,entrepreneurship,wealth,tips"
    },
    {
        "title": "Kevin Ward",
        "subscribers": "220K",
        "channel_id": "UCahgKLQNN2Y5urQ6qkZfZNA",
        "seo_keywords": "real estate agent,coach,training,prospecting,closing deals,marketing,strategy,scripts,success,listing"
    },
    {
        "title": "Bryan Casella",
        "subscribers": "190K",
        "channel_id": "UCX52HfLoKq8adTpgg9gAqUw",
        "seo_keywords": "real estate,agent tips,door knocking,prospecting,entrepreneurship,mindset,sales,personal branding,marketing,business"
    },
    {
        "title": "Chastin J. Miles",
        "subscribers": "185K",
        "channel_id": "UChtFm7WE7i2g8BIVYMUz8GA",
        "seo_keywords": "realtor,branding,agent advice,lead generation,business tips,negotiations,property,entrepreneurship,brokerage,mentorship"
    },
    {
        "title": "Loida Velasquez",
        "subscribers": "173K",
        "channel_id": "UCkeKU7Z6LdHu2TAMkMv-kow",
        "seo_keywords": "real estate agent,marketing,prospecting,lead generation,negotiation,flipping,client relations,property,buyers,sellers"
    },
    {
        "title": "Jamel Gibbs",
        "subscribers": "152K",
        "channel_id": "UC-qcYJUOedH6ET4yqePoFAw",
        "seo_keywords": "real estate,investing,house flipping,wholesaling,training,property deals,passive income,entrepreneurship,wealth building,education"
    },
    {
        "title": "Steph & Den",
        "subscribers": "120K",
        "channel_id": "UCnz2D5hBwU7oDX7-dQuIbcQ",
        "seo_keywords": "real estate,renovations,DIY,home tours,design,fix and flip,property,investing,rentals,couples"
    },
    {
        "title": "Mark Ferguson",
        "subscribers": "110K",
        "channel_id": "UCN7WszAX2Kk5wWRArqKFN3g",
        "seo_keywords": "real estate,flipping,investing,rentals,agent advice,property management,buy and hold,finance,wholesale,strategy"
    }
]

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


genre = "NFL Football"

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
        "title": "NFL",
        "subscribers": "11.20M",
        "channel_id": "UC4mLlRa_dezwvytUdp4yWZg",
        "seo_keywords": "football,nfl,highlights,american football,super bowl,players,teams,news,analysis,sports"
    },
    {
        "title": "NFL Throwback",
        "subscribers": "1.38M",
        "channel_id": "UCf4RDidKEqcYz3O8ojZ1bHA",
        "seo_keywords": "nfl,throwback,history,classics,legends,flashback,super bowl,plays,retro,highlights"
    },
    {
        "title": "Dallas Cowboys",
        "subscribers": "1.31M",
        "channel_id": "UCUsOBu0R6p62rN660d7dr5A",
        "seo_keywords": "dallas cowboys,nfl,football,america’s team,highlights,interviews,behind the scenes,dak prescott,cheerleaders,stadium"
    },
    {
        "title": "Highlight Heaven",
        "subscribers": "1.32M",
        "channel_id": "UC3nt9O1if_P8Y8h0c-NyRpg",
        "seo_keywords": "nfl,football,highlights,compilations,top plays,big hits,amazing moments,best catches,funny,edits"
    },
    {
        "title": "NFL Films",
        "subscribers": "1.09M",
        "channel_id": "UCMTk_R_Y49jvq-HQXDmKI0Q",
        "seo_keywords": "nfl films,documentaries,storytelling,football,classic footage,mic’d up,behind the scenes,players,coaches,archive"
    },
    {
        "title": "Ding Productions",
        "subscribers": "1.05M",
        "channel_id": "UCiSyrSq7ZVDo6nZooKN2HXg",
        "seo_keywords": "nfl,football,compilations,big hits,interceptions,funny moments,greatest plays,highlights,sports,edits"
    },
    {
        "title": "KTO",
        "subscribers": "1.02M",
        "channel_id": "UC8a9Dx5BvRh4SW68wT1tJPQ",
        "seo_keywords": "nfl,football,storytelling,analysis,documentary,history,fun facts,top 10,underdogs,highlights"
    },
    {
        "title": "NFL on FOX",
        "subscribers": "1.00M",
        "channel_id": "UCnC6d25eDkZ7YQOs7Y3WSyQ",
        "seo_keywords": "nfl,fox sports,highlights,analysis,previews,predictions,postgame,football,sports,talk show"
    },
    {
        "title": "Pittsburgh Steelers",
        "subscribers": "1.00M",
        "channel_id": "UCfrk7vT1sGNmmpDcHp7uUnQ",
        "seo_keywords": "pittsburgh steelers,nfl,football,terrible towel,highlights,steel city,roster updates,training camp,history,franchise"
    },
    {
        "title": "Seattle Seahawks",
        "subscribers": "420K",
        "channel_id": "UCSGyfB-EXrnZjKqzsWgpFlg",
        "seo_keywords": "seattle seahawks,nfl,football,russell wilson,12th man,highlights,lumen field,interviews,behind the scenes,blue friday"
    },
    {
        "title": "Green Bay Packers",
        "subscribers": "370K",
        "channel_id": "UCGVQ4StuTObf_iSShZABaQg",
        "seo_keywords": "green bay packers,nfl,lambeau field,cheeseheads,aaron rodgers,highlights,history,community,interviews,tradition"
    },
    {
        "title": "Chicago Bears",
        "subscribers": "310K",
        "channel_id": "UCp4pd12NshveDBpXBXhCiXQ",
        "seo_keywords": "chicago bears,nfl,football,monsters of the midway,highlights,team updates,halas hall,history,fans,gridiron"
    },
    {
        "title": "San Francisco 49ers",
        "subscribers": "280K",
        "channel_id": "UC2LGqD2SduG_kAV96EaSiPw",
        "seo_keywords": "san francisco 49ers,nfl,football,niners,levi’s stadium,highlights,history,joe montana,fans,red and gold"
    },
    {
        "title": "New England Patriots",
        "subscribers": "280K",
        "channel_id": "UCFEMjESr6Df6TVxn5G9RqdA",
        "seo_keywords": "new england patriots,nfl,football,tom brady,bill belichick,highlights,super bowl,champs,fans,foxboro"
    },
    {
        "title": "Minnesota Vikings",
        "subscribers": "210K",
        "channel_id": "UC5Z9TbyfXgM6k3bA3yUXpZA",
        "seo_keywords": "minnesota vikings,nfl,football,skol,us bank stadium,highlights,fans,kirk cousins,history,team updates"
    },
    {
        "title": "Philadelphia Eagles",
        "subscribers": "210K",
        "channel_id": "UCab1ZfhF6U2pRZ6CnQ0B8UQ",
        "seo_keywords": "philadelphia eagles,nfl,football,fly eagles fly,lincoln financial field,highlights,super bowl,fans,interviews,team news"
    },
    {
        "title": "Kansas City Chiefs",
        "subscribers": "211K",
        "channel_id": "UCpF0WcLVE1f_k9uRzZhFFgg",
        "seo_keywords": "kansas city chiefs,nfl,football,arrowhead stadium,mahomes,highlights,kingdom,tailgating,super bowl,red friday"
    },
    {
        "title": "Good Morning Football",
        "subscribers": "180K",
        "channel_id": "UCw3teYE5hpVymXhmRS0svIA",
        "seo_keywords": "nfl,talk show,analysis,morning show,highlights,news,kay adams,discussion,fun,predictions"
    },
    {
        "title": "Cleveland Browns",
        "subscribers": "140K",
        "channel_id": "UC6kBD2A1fWRFbW9u51FH-sA",
        "seo_keywords": "cleveland browns,nfl,football,dawg pound,highlights,baker mayfield,fans,first energy stadium,history,updates"
    },
    {
        "title": "New Orleans Saints",
        "subscribers": "135K",
        "channel_id": "UCn2TYnJc4yF4L3zUEiQsNhA",
        "seo_keywords": "new orleans saints,nfl,football,who dat,nola,superdome,highlights,drew brees,fans,community"
    },
    {
        "title": "The Pat McAfee Show",
        "subscribers": "120K",
        "channel_id": "UCxcTeAKWJca6XyJ37_ZoKIQ",
        "seo_keywords": "nfl,football,talk show,pat mcafee,analysis,comedy,interviews,headlines,opinions,sports"
    },
    {
        "title": "Tampa Bay Buccaneers",
        "subscribers": "110K",
        "channel_id": "UCW-g3PeFZ53lD2206dqyBXA",
        "seo_keywords": "tampa bay buccaneers,nfl,football,tom brady,raymond james stadium,pewter,highlights,fans,community,fireside chats"
    },
    {
        "title": "Baltimore Ravens",
        "subscribers": "100K",
        "channel_id": "UCt1iRj1Ob1k5eK8gH_v6iAw",
        "seo_keywords": "baltimore ravens,nfl,football,lamar jackson,mt bank stadium,highlights,fans,history,purple friday,interviews"
    },
    {
        "title": "Carolina Panthers",
        "subscribers": "80K",
        "channel_id": "UCgDtuZOLbC6GlS1FVhSU8Uw",
        "seo_keywords": "carolina panthers,nfl,football,keep pounding,cam newton,bank of america stadium,highlights,fans,news,community"
    },
    {
        "title": "That's Good Sports",
        "subscribers": "60K",
        "channel_id": "UCFkdpF7Y8mX22a02W9No54Q",
        "seo_keywords": "nfl,football,comedy,news,denver broncos,analysis,recaps,humor,highlight commentary,sports jokes"
    }
]

print(json.dumps(channels, indent=2))

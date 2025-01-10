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


genre = "PC Gaming"

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
        "title": "TBNRfrags",
        "subscribers": "7.70M",
        "channel_id": "UCpchmZ0oJ8i2Pz6Vdh4iC0w",
        "seo_keywords": "pc gaming,minecraft,preston,shooter games,commentary,multiplayer,gameplay,funny moments,livestreams,challenge videos"
    },
    {
        "title": "gameranx",
        "subscribers": "7.45M",
        "channel_id": "UCNvzD7Z-G8LLATvfuy2pETA",
        "seo_keywords": "pc gaming,game reviews,game news,top 10,gaming updates,steam,hardware,gaming industry,analysis,tips"
    },
    {
        "title": "Shroud",
        "subscribers": "6.83M",
        "channel_id": "UCoz3Kpu5lv-ALhR4h9bDvcw",
        "seo_keywords": "pc gaming,shooter games,competitive,gaming highlights,streams,pro gamer,cs go,pubg,aim skill,battle royale"
    },
    {
        "title": "jackfrags",
        "subscribers": "4.30M",
        "channel_id": "UCw7FkXsC00lH2v2yB5LQoYA",
        "seo_keywords": "pc gaming,fps,multiplayer,highlights,battlefield,call of duty,analysis,game reviews,funny moments,warzone"
    },
    {
        "title": "SovietWomble",
        "subscribers": "3.96M",
        "channel_id": "UChSa7k4G9gK3k6NY6dMIfTA",
        "seo_keywords": "pc gaming,multiplayer,funny moments,random bullshittery,montage,teamplay,trolling,commentary,arma,cs go"
    },
    {
        "title": "JayzTwoCents",
        "subscribers": "3.95M",
        "channel_id": "UCkWQ0gDrqOCarmUKmppD7GQ",
        "seo_keywords": "pc hardware,pc gaming,tech reviews,water cooling,gpu,cpu,build guides,tutorials,benchmarks,overclocking"
    },
    {
        "title": "TheRussianBadger",
        "subscribers": "3.43M",
        "channel_id": "UC1KDVoX4yP4TPsm3tRGF0Mg",
        "seo_keywords": "pc gaming,commentary,funny moments,battlefield,rainbow six siege,multiplayer,memes,humor,teamplay,fps"
    },
    {
        "title": "Node",
        "subscribers": "3.24M",
        "channel_id": "UCeOyZ4HE3tHbgx3LpQKHpJQ",
        "seo_keywords": "pc gaming,virtual reality,multiplayer,dnd,battle sims,live action,rp gaming,team challenges,funny moments,mods"
    },
    {
        "title": "FrankieOnPC",
        "subscribers": "2.78M",
        "channel_id": "UC0MYeQGxfwCrBogaaUPE6aQ",
        "seo_keywords": "pc gaming,dayz,arma,storytelling,immersive gameplay,commentary,open world,survival,multiplayer,modded"
    },
    {
        "title": "StoneMountain64",
        "subscribers": "2.42M",
        "channel_id": "UCieE3l9Py2VQqTs1FCL9Spg",
        "seo_keywords": "pc gaming,warzone,battlefield,live commentary,funny moments,strategy,streams,multiplayer,clutch plays,fps"
    },
    {
        "title": "PC Gamer",
        "subscribers": "2.24M",
        "channel_id": "UCaW8XOhbK0IRrP8Qlg9mZRw",
        "seo_keywords": "pc gaming,magazine,news,previews,reviews,trailers,interviews,hardware,steam,gaming events"
    },
    {
        "title": "PhlyDaily",
        "subscribers": "2.23M",
        "channel_id": "UCg4QS2gZ3m5K7EDTpB2IcGw",
        "seo_keywords": "pc gaming,war thunder,planes,tanks,multiplayer,simulation,funny commentary,battle,squad,highlights"
    },
    {
        "title": "Welyn",
        "subscribers": "2.18M",
        "channel_id": "UCgCRvAmkqpvqKwdENHjZ57Q",
        "seo_keywords": "pc gaming,rust,survival,multiplayer,raid,storytelling,stealth,open world,commentary,pvp"
    },
    {
        "title": "LevelCapGaming",
        "subscribers": "1.92M",
        "channel_id": "UCXeDFaoBV8aFdhp6NMy7uQA",
        "seo_keywords": "pc gaming,fps,battlefield,cod,guides,weapon reviews,tips,analysis,strategy,updates"
    },
    {
        "title": "Gamers Nexus",
        "subscribers": "1.86M",
        "channel_id": "UCXGgrKt94gR6lmN4aN3mYTg",
        "seo_keywords": "pc hardware,benchmarks,gpu,cpu,tech news,deep dive,analysis,pc gaming,cooling,build guides"
    },
    {
        "title": "Hardware Canucks",
        "subscribers": "1.79M",
        "channel_id": "UCsnvMm7nqgi7wXh59ab9W0Q",
        "seo_keywords": "pc hardware,reviews,builds,head to head,benchmarks,graphics cards,cpus,pc gaming,accessories,tech tips"
    },
    {
        "title": "Skill Up",
        "subscribers": "1.42M",
        "channel_id": "UCZ7H5tP-I88RBA1I4t3H_9g",
        "seo_keywords": "pc gaming,game reviews,analysis,news,opinions,rpgs,action games,steam,gaming commentary,industry discussion"
    },
    {
        "title": "Aculite",
        "subscribers": "1.40M",
        "channel_id": "UCQkd05iAYed2-LOmhjzDGgw",
        "seo_keywords": "pc gaming,battle royale,fps,sniping,compilations,highlights,multiplayer,warzone,pubg,live commentary"
    },
    {
        "title": "crowbcat",
        "subscribers": "1.28M",
        "channel_id": "UCmlRdtZvXR4YlZr3as8F7ug",
        "seo_keywords": "pc gaming,comparisons,editing,funny clips,analysis,industry critique,glitches,before after,trailers,commentary"
    },
    {
        "title": "Hardware Unboxed",
        "subscribers": "1.25M",
        "channel_id": "UCI8iQa1hv7oV_Z8D35vVuSg",
        "seo_keywords": "pc hardware,tech reviews,graphics cards,cpus,benchmarks,gaming performance,build guides,monitors,analysis,news"
    },
    {
        "title": "summit1g",
        "subscribers": "0.72M",
        "channel_id": "UCqzCTNYLtCrOkd802v7ePKg",
        "seo_keywords": "pc gaming,streamer,live highlights,shooters,variety,fun moments,battle royale,twitch replays,cs go,entertainment"
    },
    {
        "title": "LowSpecGamer",
        "subscribers": "0.68M",
        "channel_id": "UCoj6RxIAQ0mCIhZ6i1-532g",
        "seo_keywords": "pc gaming,low end,optimization,tips,hacks,old hardware,performance guides,steam,budget gaming,configs"
    },
    {
        "title": "Tech Deals",
        "subscribers": "0.54M",
        "channel_id": "UCmbkRUS_4Efdt5UIhwNqtcw",
        "seo_keywords": "pc gaming,build guides,hardware deals,budgets,performance tips,benchmarks,upgrades,cpu,gpu,tech help"
    },
    {
        "title": "EposVox",
        "subscribers": "0.46M",
        "channel_id": "UC9fSZHEh6XsRpX-xJc1iXaw",
        "seo_keywords": "pc gaming,streaming,tech tutorials,obs,recording,hardware,software tips,video optimization,config guides,gear reviews"
    },
    {
        "title": "CohhCarnage",
        "subscribers": "0.35M",
        "channel_id": "UCo4yb6XRa03V4rMiJfAb_bQ",
        "seo_keywords": "pc gaming,streamer,rpg,mmorpg,variety,friendly community,playthroughs,early access,twitch highlights,commentary"
    }
]

print(json.dumps(channels, indent=2))

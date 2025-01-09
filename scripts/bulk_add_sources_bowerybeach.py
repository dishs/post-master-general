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


genre = "Surfing"

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
        "title": "World Surf League",
        "subscribers": "1.04M",
        "channel_id": "UCo_q6aOlvPH7M-j_XGWVgXg",
        "seo_keywords": "surfing,competition,big waves,pro surfers,championship tour,beach culture,ocean sports,tutorials,highlights,travel"
    },
    {
        "title": "Jamie O'Brien",
        "subscribers": "990K",
        "channel_id": "UCZAsQd1NnHyL6Yj6bIE5BWg",
        "seo_keywords": "surfing,wave riding,hawaii,adventure,big waves,travel vlog,red bull athlete,barrels,extreme sports,beach life"
    },
    {
        "title": "Red Bull Surfing",
        "subscribers": "600K",
        "channel_id": "UCOpkn_1U2WLo2o1dDUP8RFA",
        "seo_keywords": "surfing,extreme sports,big waves,athletes,adventure,action sports,competition,barrels,filmmaking,ocean lifestyle"
    },
    {
        "title": "Nathan Florence",
        "subscribers": "420K",
        "channel_id": "UC7T9j0OXbC5S4YXRk2RKUrA",
        "seo_keywords": "surfing,hawaii,big wave,freesurf,barrels,training,vlogs,adventure,progression,travel"
    },
    {
        "title": "Koa Rothman",
        "subscribers": "361K",
        "channel_id": "UCE_imNNa3P0MmFO5oTqLtnw",
        "seo_keywords": "surfing,hawaii,big wave,travel,barrels,vlogs,lifestyle,ocean life,adventure,surf tips"
    },
    {
        "title": "Kook Of The Day",
        "subscribers": "285K",
        "channel_id": "UCNIx-p7f30vBfD3pI5hqkiQ",
        "seo_keywords": "surf fails,kook moments,comedy,beach culture,learning to surf,wipeouts,ocean humor,compilation,community,entertainment"
    },
    {
        "title": "Stab",
        "subscribers": "220K",
        "channel_id": "UCczn5z0wTFRn3m6YWRPZfjA",
        "seo_keywords": "surfing,magazine,documentaries,barrels,interviews,travel,films,gear reviews,innovation,stories"
    },
    {
        "title": "Ben Gravy",
        "subscribers": "171K",
        "channel_id": "UC4-3VX696g6l5kHMwTJ4cHg",
        "seo_keywords": "surfing,vlog,river waves,adventure,fun,eclectic spots,stoke,positive vibes,board reviews,travel"
    },
    {
        "title": "Surfline",
        "subscribers": "157K",
        "channel_id": "UC8b3yHtAU-3C0N3QvT_BpRQ",
        "seo_keywords": "surf forecasts,live cams,ocean science,surfing,barrels,big wave,travel,coaching,gear,community"
    },
    {
        "title": "Casey Willax",
        "subscribers": "137K",
        "channel_id": "UC3adCW5ZZ9dsAr2Y4m6-v1A",
        "seo_keywords": "surfing,snowboarding,action sports,travel,van life,adventure,vlogs,ocean,board sports,stoke"
    },
    {
        "title": "Brett Barley",
        "subscribers": "94K",
        "channel_id": "UC7rI7sfa7W-90KRoJ6Oo12g",
        "seo_keywords": "surfing,barrels,outer banks,north carolina,adventure,big waves,tutorials,gear,fish,surf vlogs"
    },
    {
        "title": "SURFER",
        "subscribers": "80K",
        "channel_id": "UCfBEX6F316QwP2MZ0GxSNdA",
        "seo_keywords": "surfing,magazine,stories,films,travel,barrels,icons,photography,ocean culture,history"
    },
    {
        "title": "Mauli Ola Foundation",
        "subscribers": "65K",
        "channel_id": "UC60vzizP_67LlsPtVSrJNCg",
        "seo_keywords": "surfing,foundation,cystic fibrosis,awareness,charity,ocean therapy,hawaii,community,health,events"
    },
    {
        "title": "Surf & Turf",
        "subscribers": "55K",
        "channel_id": "UCabCDSURFNTURFexample",
        "seo_keywords": "surfing,travel,beach lifestyle,seafood,coastal living,wave riding,local culture,adventure,barrels,documentary"
    },
    {
        "title": "Surf Lakes",
        "subscribers": "49K",
        "channel_id": "UC53KZx9qeozqRa0TWErOKUw",
        "seo_keywords": "wave pool,artificial surfing,technology,innovation,barrels,training,future surf,wave machine,demonstrations,australia"
    },
    {
        "title": "iSurfTribe",
        "subscribers": "43K",
        "channel_id": "UCisURFTRIBEexample",
        "seo_keywords": "surfing,tribe,community,coastal life,barrels,adventure,local breaks,vlogs,tutorials,lifestyle"
    },
    {
        "title": "Surf Vibes",
        "subscribers": "39K",
        "channel_id": "UCsurfvibesCHIDexample",
        "seo_keywords": "surfing,compilations,inspiration,barrels,beach vibes,summer,travel,music edits,highlights,fun"
    },
    {
        "title": "My Surf TV",
        "subscribers": "35K",
        "channel_id": "UCpWLrTur7yGVbM8hxtg9StQ",
        "seo_keywords": "surfing,events,highlights,travel,interviews,barrels,groms,legends,ocean culture,documentaries"
    },
    {
        "title": "REAL Watersports",
        "subscribers": "31K",
        "channel_id": "UCQUwilL2W6Dv0y31u4McIJw",
        "seo_keywords": "surfing,kiteboarding,foil,surf shop,lessons,gear reviews,outer banks,water sports,barrels,travel"
    },
    {
        "title": "Surfers of Bali",
        "subscribers": "28K",
        "channel_id": "UC19qBoEMfB_yWvJle16-JPg",
        "seo_keywords": "surfing,bali,beach breaks,barrels,tourism,local surfers,international vibe,travel,highlight reels,indonesia"
    },
    {
        "title": "Surf Travel Vlogs",
        "subscribers": "25K",
        "channel_id": "UCsurftravelvlogsIDexample",
        "seo_keywords": "surfing,travel,beach reviews,airline tips,budget trips,adventure,international,barrels,vlogs,gear"
    },
    {
        "title": "Freesurf Magazine",
        "subscribers": "22K",
        "channel_id": "UC3c55uCgSvrFUHEYv4Wd1lw",
        "seo_keywords": "surfing,hawaii,magazine,local pros,barrels,stories,highlights,style,gear,events"
    },
    {
        "title": "Surf Tutorials",
        "subscribers": "15K",
        "channel_id": "UCsurftutorialsCHIDexample",
        "seo_keywords": "surfing,how to,technique,paddling,duck dive,pop up,board selection,wave reading,footwork,beginner tips"
    },
    {
        "title": "Bing Surfboards",
        "subscribers": "12K",
        "channel_id": "UCchBingSurfboardsIDexample",
        "seo_keywords": "surfboards,craftsmanship,shaping,classic style,longboarding,ocean lifestyle,design,handmade,heritage,california"
    },
    {
        "title": "TheSurfChannelTV",
        "subscribers": "10K",
        "channel_id": "UCsurfchannelTVexample",
        "seo_keywords": "surfing,films,documentaries,interviews,travel,barrels,legends,big wave,stories,live events"
    }
]

print(json.dumps(channels, indent=2))

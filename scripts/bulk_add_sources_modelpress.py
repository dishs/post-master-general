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


genre = "R/C Cars"

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
        "title": "RCSparks Studio (RC Adventures)",
        "subscribers": "3.26M",
        "channel_id": "UCp6HF8h8bSmbx3N6XX3M2xQ",
        "seo_keywords": "rc cars,radio control,off road,monster trucks,scalers,custom builds,unboxing,adventures,upgrades,rc community"
    },
    {
        "title": "Kevin Talbot",
        "subscribers": "2.53M",
        "channel_id": "UCtmHAq2b1DgrM6z8GclK5GA",
        "seo_keywords": "rc cars,stunts,bashing,off road,monster trucks,rc racing,unboxing,fixes,upgrades,high speed"
    },
    {
        "title": "Peter Sripol",
        "subscribers": "2.14M",
        "channel_id": "UC7yF9tV4xWEMZkel7q8La_w",
        "seo_keywords": "rc planes,rc cars,diy builds,electric flight,custom projects,engineering,experiments,fun tests,innovation,creative"
    },
    {
        "title": "Traxxas",
        "subscribers": "0.95M",
        "channel_id": "UCtqNwzKboNVY5z5CVCncYAQ",
        "seo_keywords": "rc cars,monster trucks,short course,bashing,stunts,unboxing,upgrades,industry leader,waterproof,speed runs"
    },
    {
        "title": "Tomley RC",
        "subscribers": "0.70M",
        "channel_id": "UC2ZXTZMuKo7h4k8mZbu3_Og",
        "seo_keywords": "rc cars,builds,reviews,bashing,off road,drift,comparisons,mods,unboxings,rc tips"
    },
    {
        "title": "Quadcopter 101",
        "subscribers": "0.53M",
        "channel_id": "UCPeX6PvcwL7dTx3s7E6qOUQ",
        "seo_keywords": "rc drones,quadcopters,fpv,rc cars,product reviews,unboxings,beginner tips,range tests,camera drones,budget"
    },
    {
        "title": "RC Model Reviews",
        "subscribers": "0.39M",
        "channel_id": "UCahqHsTaADV3Hqk2lafWzjw",
        "seo_keywords": "rc tech,fpv,planes,drones,cars,reviews,how to,transmitters,budget tips,modifications"
    },
    {
        "title": "TheRcSaylors",
        "subscribers": "0.31M",
        "channel_id": "UCJ7MAZk6JJCFgkf3tB1f3HA",
        "seo_keywords": "rc reviews,beginner friendly,drones,cars,planes,boats,unboxings,fun vlogs,husband wife,adventures"
    },
    {
        "title": "Horizon Hobby",
        "subscribers": "0.30M",
        "channel_id": "UC1Up0ykoQ3BPJ-n5fYVZ30Q",
        "seo_keywords": "rc hobby,planes,cars,trucks,boats,brands,spektrum,e-flite,losi,arrma"
    },
    {
        "title": "Tamiya RC Official",
        "subscribers": "0.28M",
        "channel_id": "UCtamiyaRCchannelID",
        "seo_keywords": "tamiya,rc cars,model kits,scale trucks,bashing,drifting,assembly,classic designs,body shells,collectors"
    },
    {
        "title": "RCDriver_Online",
        "subscribers": "0.25M",
        "channel_id": "UCy9xMke1rh5tamzIx1PlNmw",
        "seo_keywords": "rc driver,reviews,how tos,build tips,gear tests,scalers,short course,electric,nitro,magazine"
    },
    {
        "title": "The RCNetwork",
        "subscribers": "0.17M",
        "channel_id": "UCpNF2mOPiis8fWoXsXcI_NQ",
        "seo_keywords": "rc builds,unboxings,upgrades,tech tips,off road,crawlers,bashing,drifting,reviews,custom projects"
    },
    {
        "title": "Aussie RC Playground",
        "subscribers": "0.13M",
        "channel_id": "UCD96rSgyyC3HsN0AtksEujQ",
        "seo_keywords": "rc cars,australia,bashing,off road,track tests,reviews,mods,unboxings,community,fun"
    },
    {
        "title": "URC (Ultimate RC)",
        "subscribers": "0.10M",
        "channel_id": "UCUltimateRCchannelID",
        "seo_keywords": "rc community,discussions,reviews,tips,builds,tech talk,off road,drift,scalers,how to"
    },
    {
        "title": "RC Car Action",
        "subscribers": "0.09M",
        "channel_id": "UCcarActionChannelID",
        "seo_keywords": "rc magazine,news,bashing,competitions,new releases,reviews,upgrades,drivers,events,coverage"
    },
    {
        "title": "scale Builders Guild",
        "subscribers": "0.084M",
        "channel_id": "UCscaleBuildersGuildID",
        "seo_keywords": "scale rc,crawlers,trucks,custom builds,weathering,detailing,miniature,tech tips,community,trail rides"
    },
    {
        "title": "EastTactics",
        "subscribers": "0.07M",
        "channel_id": "UCEastTacticsChannelID",
        "seo_keywords": "rc bashing,speed runs,mods,upgrades,arrma,tech tips,diy,drift,motors,electronics"
    },
    {
        "title": "CCxRC",
        "subscribers": "0.065M",
        "channel_id": "UCCCxRCchannelID",
        "seo_keywords": "rc monster trucks,custom builds,clod buster,crawlers,trail trucks,solid axle,backyard bashing,fun,mods,reviews"
    },
    {
        "title": "AMainHobbies",
        "subscribers": "0.06M",
        "channel_id": "UCAMainHobbiesChannelID",
        "seo_keywords": "rc shop,product overviews,cars,planes,drones,build tips,unboxings,gear,events,racing"
    },
    {
        "title": "GeoStealth R1",
        "subscribers": "0.06M",
        "channel_id": "UCGeoStealthR1channelID",
        "seo_keywords": "rc cars,drift,street speed,brushless,motor upgrades,custom bodies,bashing,how to,unboxing,performance"
    },
    {
        "title": "Spinning Leopard RC",
        "subscribers": "0.05M",
        "channel_id": "UCSpinningLeopardRC",
        "seo_keywords": "rc drifting,burning rubber,drift tracks,upgrade parts,how to,body kits,tires,setup tips,sliding,fun"
    },
    {
        "title": "Net Cruiser RC",
        "subscribers": "0.045M",
        "channel_id": "UCNetCruiserRCchannelID",
        "seo_keywords": "rc lifestyle,cars,trucks,tech reviews,bashing,vlogs,motorsports,trail riding,drones,personal projects"
    },
    {
        "title": "Banksy RC",
        "subscribers": "0.04M",
        "channel_id": "UCBanksyRCchannelID",
        "seo_keywords": "rc cars,monster trucks,stunts,indoor tracks,mods,unboxing,how to,testing,fun,community"
    },
    {
        "title": "Elmo's RC Playground",
        "subscribers": "0.035M",
        "channel_id": "UCElmosRCPlaygroundID",
        "seo_keywords": "rc cars,family friendly,backyard track,mini rc,fun runs,unboxings,kids,build logs,creative,community"
    },
    {
        "title": "Blacktop RC",
        "subscribers": "0.02M",
        "channel_id": "UCBlacktopRCchannelID",
        "seo_keywords": "rc street,drag racing,belts,custom builds,speed run,mods,tires,electronics,transmissions,tutorials"
    }
]

print(json.dumps(channels, indent=2))

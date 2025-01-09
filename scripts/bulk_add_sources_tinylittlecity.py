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


genre = "Tiny & Box Homes"

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
        "title": "Living Big in a Tiny House",
        "subscribers": "4.60M",
        "channel_id": "UCgd7ezKHalK0D92O7z4uUsg",
        "seo_keywords": "tiny house,small living,architecture,off grid,downsize,container homes,sustainability,design,DIY,travel"
    },
    {
        "title": "Off Grid With Jake and Nicolle",
        "subscribers": "2.74M",
        "channel_id": "UCne-C82oZgM2Wm4mMH4-WlA",
        "seo_keywords": "off grid,cabin living,tiny home,homesteading,diy,sustainability,construction,self reliance,nature,adventure"
    },
    {
        "title": "Exploring Alternatives",
        "subscribers": "2.41M",
        "channel_id": "UC8EQAfuePhNLy0vLO4JXF1A",
        "seo_keywords": "tiny house,van life,minimalism,travel,off grid,camper,alternative living,design,eco friendly,container homes"
    },
    {
        "title": "Eamon & Bec",
        "subscribers": "2.35M",
        "channel_id": "UC4laAHbk8VSgmvB47tsd03Q",
        "seo_keywords": "van life,off grid,tiny home,camper conversions,couple travel,minimalism,adventure,budget living,vegan,DIY"
    },
    {
        "title": "Never Too Small",
        "subscribers": "2.10M",
        "channel_id": "UC9zAWQyX9Dz0fkgb-9VvW-A",
        "seo_keywords": "micro apartments,small space,tiny living,city design,architecture,efficiency,urban lifestyle,interior design,storage solutions,innovation"
    },
    {
        "title": "Kirsten Dirksen",
        "subscribers": "2.00M",
        "channel_id": "UC7lI2mbvD7v5P1exXg_5hww",
        "seo_keywords": "tiny homes,architecture,handmade homes,off grid,eco living,minimalism,alternative living,self build,design,documentary"
    },
    {
        "title": "Tiny House Giant Journey",
        "subscribers": "1.56M",
        "channel_id": "UCaboPlKqY0MZCitZKwUA-9w",
        "seo_keywords": "tiny house,mobile living,DIY,alternative lifestyle,travel,downsize,off grid,design,van life,interviews"
    },
    {
        "title": "Tiny Home Tours",
        "subscribers": "1.47M",
        "channel_id": "UC7ZIzM0HTlK35p6keRzNp5w",
        "seo_keywords": "tiny home,tours,van life,school bus conversion,minimalism,camper living,off grid,design,eco living,DIY"
    },
    {
        "title": "Levi Kelly",
        "subscribers": "1.14M",
        "channel_id": "UCB1Yh-FrcKTEYQEYDa7QTyg",
        "seo_keywords": "tiny house,unique stays,travel,airbnb reviews,architecture,glamping,cabins,design,modern living,luxury small spaces"
    },
    {
        "title": "Living The Van Life",
        "subscribers": "610K",
        "channel_id": "UCioA3jZiTrWHwwK7pZ9akXA",
        "seo_keywords": "van life,tiny home on wheels,adventure travel,camper conversions,off grid,simple living,camping,DIY,overlanding,exploration"
    },
    {
        "title": "Van Wives",
        "subscribers": "551K",
        "channel_id": "UCcUbMF_dnIvP7qSlwqAXzBA",
        "seo_keywords": "van life,tiny living,couple travel,off grid,dogs,camper conversions,adventure,eco living,minimalism,community"
    },
    {
        "title": "GoDownsize",
        "subscribers": "540K",
        "channel_id": "UC6ppkZ9h0YyeWpIdY5M1f8w",
        "seo_keywords": "downsizing,tiny house,small spaces,organization,minimalism,decluttering,interior design,DIY,budget living,efficiency"
    },
    {
        "title": "The Indie Projects",
        "subscribers": "520K",
        "channel_id": "UC5L_Xh2Qu2evuDJZgQaSpyA",
        "seo_keywords": "van life,off grid,cabin building,tiny living,DIY,homesteading,adventure,renovations,camper conversions,travel"
    },
    {
        "title": "Tiny House Expedition",
        "subscribers": "495K",
        "channel_id": "UC_7F7LtkCZNFQ7wG4UwiVjQ",
        "seo_keywords": "tiny house,legalization,documentary,off grid,community,nomadic living,DIY,design,downsizing,stories"
    },
    {
        "title": "The Nomadic Movement",
        "subscribers": "430K",
        "channel_id": "UC6kOHqEBRBmQl7h8KL_K3ew",
        "seo_keywords": "van life,tiny home,panama homestead,off grid,couple travel,DIY,adventure,community,downsizing,construction"
    },
    {
        "title": "Tiny House Listings",
        "subscribers": "425K",
        "channel_id": "UCWibZcxWsGF8u6OCy7gkSuw",
        "seo_keywords": "tiny house,real estate,for sale,alternative living,downsize,off grid,listings,DIY,cabins,container homes"
    },
    {
        "title": "Jenna Sue Design",
        "subscribers": "370K",
        "channel_id": "UClOsF09eicTknZa56AjM5Mg",
        "seo_keywords": "tiny home,renovation,DIY,design,decor,interiors,cottages,real estate,makeovers,downsizing"
    },
    {
        "title": "Tiny House Customs",
        "subscribers": "370K",
        "channel_id": "UCvfeZh9uXL9zEif9RT53fxw",
        "seo_keywords": "tiny house,build tutorials,woodworking,DIY,construction,design tips,off grid,cabins,minimalism,projects"
    },
    {
        "title": "Relax Shacks",
        "subscribers": "289K",
        "channel_id": "UCXEv-__7XS0aYznVkWVDN9A",
        "seo_keywords": "tiny houses,shelter,micro cabins,DIY,creative design,tree houses,forts,handmade,downsize,workshops"
    },
    {
        "title": "Minimalist Living",
        "subscribers": "210K",
        "channel_id": "UC74cDY27OHt2RnZhiWXDqGg",
        "seo_keywords": "minimalism,tiny space,clutter free,organization,downsizing,life hacks,declutter,design,eco friendly,simplicity"
    },
    {
        "title": "A Tiny Good Thing",
        "subscribers": "150K",
        "channel_id": "UCYbWV0Q7vCqMC3NmmCVnPJg",
        "seo_keywords": "tiny living,small homes,diy decor,eco building,off grid,downsize,design,creative spaces,minimalism,stories"
    },
    {
        "title": "Tiny House Movement",
        "subscribers": "100K",
        "channel_id": "UCFwnKtsuNdybY9YXySfB7ow",
        "seo_keywords": "tiny living,community,advocacy,design ideas,downsizing,off grid,housing solutions,sustainability,construction,innovation"
    },
    {
        "title": "Tiny House Big Living",
        "subscribers": "90K",
        "channel_id": "UC1abcXYZTinyHouseBigLiving",
        "seo_keywords": "tiny house,box home,creative builds,off grid,eco friendly,architecture,small space,DIY,urban living,design"
    },
    {
        "title": "HomeTourVision",
        "subscribers": "80K",
        "channel_id": "UC7xyzHomeTourVision",
        "seo_keywords": "tiny house tours,container homes,box living,design,architecture,creative spaces,small footprints,interior,modern,showcase"
    },
    {
        "title": "Small House Life",
        "subscribers": "60K",
        "channel_id": "UCabc123SmallHouse",
        "seo_keywords": "small home,tiny living,off grid,box house,downsizing,simple life,DIY,design,alternative living,minimalism"
    }
]


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


genre = "Travel Guides"

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
        "title": "Mark Wiens",
        "subscribers": "9.80M",
        "channel_id": "UCyEd6QBSgat5kkC6svyjudA",
        "seo_keywords": "food,travel,street food,asia,culture,adventure,beaches,local cuisine,global destinations,guides"
    },
    {
        "title": "Kara and Nate",
        "subscribers": "3.70M",
        "channel_id": "UC4ijq8Cg-8zQKx8OH12dUSw",
        "seo_keywords": "travel,couple adventures,backpacking,global destinations,airline reviews,adventure,food,tips,budget,cultural experiences"
    },
    {
        "title": "The Bucket List Family",
        "subscribers": "2.76M",
        "channel_id": "UC-niQ7GNE7W_s4p1Sqp3gNQ",
        "seo_keywords": "family travel,adventure,kids,beaches,resorts,storytelling,global exploration,hotels,vlogs,lifestyle"
    },
    {
        "title": "Sam Chui",
        "subscribers": "2.76M",
        "channel_id": "UCbzRzT0KfWwTg8r6fPzv--g",
        "seo_keywords": "aviation,travel,airline reviews,flight experiences,luxury,class,tips,global exploration,vlogs,airport tours"
    },
    {
        "title": "Drew Binsky",
        "subscribers": "2.73M",
        "channel_id": "UC0IntLFzLaudFG-xAvUEO-A",
        "seo_keywords": "travel,cultures,adventure,food,people,world tour,budget,tips,history,guides"
    },
    {
        "title": "Lost LeBlanc",
        "subscribers": "2.30M",
        "channel_id": "UCt_NLJ4McJlCyYM-dSPRo7Q",
        "seo_keywords": "travel,beaches,asia,adventure,lifestyle,vlogs,cinematic,filmmaking,global destinations,budget"
    },
    {
        "title": "Yes Theory",
        "subscribers": "2.20M",
        "channel_id": "UC3OZ6GcdZuyL9tlTHfRtTdw",
        "seo_keywords": "travel,adventure,experiences,challenge,hidden gems,social experiments,motivation,community,culture,bucket list"
    },
    {
        "title": "Indigo Traveller",
        "subscribers": "1.68M",
        "channel_id": "UCXulruMI7BHj3kGyosNa0jA",
        "seo_keywords": "travel,documentaries,offbeat,backpacking,adventure,social awareness,food,people,cultures,guides"
    },
    {
        "title": "Fearless & Far",
        "subscribers": "1.42M",
        "channel_id": "UCGaovZsizEMvNNLjApPY6sQ",
        "seo_keywords": "adventure,unusual destinations,travel,beaches,off the beaten path,culture,stories,thrill seeking,expedition,bucket list"
    },
    {
        "title": "Expoza Travel",
        "subscribers": "1.00M",
        "channel_id": "UCwAEUuDDBN1j6O8KV1haHAw",
        "seo_keywords": "travel guides,documentaries,city tours,history,culture,architecture,landmarks,world destinations,budget tips,museums"
    },
    {
        "title": "Wolters World",
        "subscribers": "1.07M",
        "channel_id": "UCFr3sz2t3bDp6Cux08B93KQ",
        "seo_keywords": "travel,tourism,city guides,what to expect,tips,culture,food,advice,beaches,mistakes"
    },
    {
        "title": "Vagabrothers",
        "subscribers": "1.13M",
        "channel_id": "UCbochVIwBCzJb9I2lLGXGjQ",
        "seo_keywords": "travel guides,adventure,culture,beaches,food,road trips,history,backpacking,stories,tips"
    },
    {
        "title": "Travel Beans",
        "subscribers": "400K",
        "channel_id": "UC43nr_7R0dG6a9OhclJidLg",
        "seo_keywords": "couple travel,backpacking,beaches,van life,adventures,stories,budget tips,road trips,hostels,fun"
    },
    {
        "title": "Hey Nadine",
        "subscribers": "445K",
        "channel_id": "UCNcTu7X1Obwt2kkX-vXy6qg",
        "seo_keywords": "travel tips,solo travel,adventure,packing tips,travel hacks,stories,budget,culture,vlogs,beaches"
    },
    {
        "title": "CupofTJ",
        "subscribers": "550K",
        "channel_id": "UC2DM45maPiOOUWc7M5ZCHBw",
        "seo_keywords": "travel,food,beach towns,vlogs,adventure,asia,street food,local tips,storytelling,fun"
    },
    {
        "title": "Lexie Limitless",
        "subscribers": "520K",
        "channel_id": "UCrI-jZJZpChgrUu0E3ZCApw",
        "seo_keywords": "travel,193 countries,adventure,world record,beaches,culture,vlogs,solo female,bucket list,guides"
    },
    {
        "title": "Migrationology",
        "subscribers": "500K",
        "channel_id": "UC6cXyMl-_2ayOIaZLrQJIMQ",
        "seo_keywords": "food,travel,street food,spicy,asia,culture,global,local guides,adventure,mark wiens"
    },
    {
        "title": "The Endless Adventure",
        "subscribers": "300K",
        "channel_id": "UCEjkioV3LO_OIUaSWRxFZ3A",
        "seo_keywords": "travel,vlogs,adventure,beaches,road trips,food,budget tips,culture,experiences,camping"
    },
    {
        "title": "Hopscotch the Globe",
        "subscribers": "700K",
        "channel_id": "UCkKCjlTe0A-dyZHvBkUom0w",
        "seo_keywords": "travel,couples,van life,off grid,adventure,global exploration,camping,road trip,stories,spiritual"
    },
    {
        "title": "Expert Vagabond",
        "subscribers": "250K",
        "channel_id": "UCexpertVagabondID",
        "seo_keywords": "adventure,travel photography,backpacking,budget,solo travel,beaches,extreme sports,photography tips,stories,culture"
    },
    {
        "title": "RayaWasHere",
        "subscribers": "220K",
        "channel_id": "UCftZQn4W3Z0nUVtbBGngMwA",
        "seo_keywords": "travel,vegan,solo female,lifestyle,road trips,backpacking,beaches,stories,budget tips,global"
    },
    {
        "title": "Backpacking Bananas",
        "subscribers": "190K",
        "channel_id": "UCbackpackingBananasID",
        "seo_keywords": "backpacking,travel,budget,hostels,culture,solo female,beaches,gap year,tips,adventures"
    },
    {
        "title": "Chase for Adventure",
        "subscribers": "160K",
        "channel_id": "UCchaseForAdventureID",
        "seo_keywords": "travel,world tour,couple,backpacking,beaches,digital nomad,budget tips,adventure,stories,culture"
    },
    {
        "title": "PsychoTraveller",
        "subscribers": "210K",
        "channel_id": "UCseh2gFytJCiZkQZIiM70mA",
        "seo_keywords": "travel,backpacking,solo female,beaches,motivation,hostels,budget tips,advice,stories,adventure"
    },
    {
        "title": "ExploTraveler",
        "subscribers": "120K",
        "channel_id": "UCExploTravelerIDchannel",
        "seo_keywords": "travel guides,hidden gems,off the beaten path,city tours,culture,food,budget,adventure,beaches,museums"
    }
]

print(json.dumps(channels, indent=2))



import json

channels = [
    {
        "title": "Mark Wiens",
        "subscribers": "9.80M",
        "channel_id": "UCyEd6QBSgat5kkC6svyjudA",
        "seo_keywords": "travel,food,street food,culture,asia,global exploring,vlogs,local experiences,adventure,beaches"
    },
    {
        "title": "Kara and Nate",
        "subscribers": "3.70M",
        "channel_id": "UC4ijq8Cg-8zQKx8OH12dUSw",
        "seo_keywords": "travel,couple,budget,adventure,global,culture,airline reviews,food,stories,tips"
    },
    {
        "title": "The Bucket List Family",
        "subscribers": "2.76M",
        "channel_id": "UC-niQ7GNE7W_s4p1Sqp3gNQ",
        "seo_keywords": "family travel,adventure,kids,beaches,hotels,resorts,globetrotting,vlogs,storytelling,experiences"
    },
    {
        "title": "Drew Binsky",
        "subscribers": "2.73M",
        "channel_id": "UC0IntLFzLaudFG-xAvUEO-A",
        "seo_keywords": "travel,travel vlog, global,people,cultures,budget,tips,vlogs,adventure,food,stories"
    },
    {
        "title": "Lost LeBlanc",
        "subscribers": "2.30M",
        "channel_id": "UCt_NLJ4McJlCyYM-dSPRo7Q",
        "seo_keywords": "travel,cinematic,filmmaking,adventure,asia,beaches,budget,stories,global destinations,lifestyle"
    },
    {
        "title": "Yes Theory",
        "subscribers": "2.20M",
        "channel_id": "UCvK4bOhULCpmLabd2pDMtnA",
        "seo_keywords": "travel,adventure,challenge,people,experiences,culture,hidden gems,motivation,exploration,fun"
    },
    {
        "title": "Indigo Traveller",
        "subscribers": "1.68M",
        "channel_id": "UCXulruMI7BHj3kGyosNa0jA",
        "seo_keywords": "travel,documentaries,backpacking,offbeat,social awareness,adventure,people,culture,vlogs,food"
    },
    {
        "title": "Luke Martin",
        "subscribers": "1.54M",
        "channel_id": "UCtMgyCDRLnXq0X3I-3F3LnQ",
        "seo_keywords": "travel,food,street food,exploration,local experiences,vlogs,asia,global,culinary tours,adventure"
    },
    {
        "title": "Fearless & Far",
        "subscribers": "1.42M",
        "channel_id": "UCGaovZsizEMvNNLjApPY6sQ",
        "seo_keywords": "adventure,travel,unusual destinations,offbeat,culture,storytelling,thrills,global,beaches,vlogs"
    },
    {
        "title": "Vagabrothers",
        "subscribers": "1.13M",
        "channel_id": "UCbochVIwBCzJb9I2lLGXGjQ",
        "seo_keywords": "travel guides,adventure,culture,beaches,food,road trips,history,stories,backpacking,tips"
    },
    {
        "title": "CupofTJ",
        "subscribers": "0.55M",
        "channel_id": "UC2DM45maPiOOUWc7M5ZCHBw",
        "seo_keywords": "travel,food,fun,beach towns,vlogs,adventure,asia,local tips,storytelling,culinary"
    },
    {
        "title": "Lexie Limitless",
        "subscribers": "0.52M",
        "channel_id": "UCrI-jZJZpChgrUu0E3ZCApw",
        "seo_keywords": "travel,193 countries,world record,adventure,beaches,culture,vlogs,solo female,bucket list,stories"
    },
    {
        "title": "Hey Nadine",
        "subscribers": "0.445M",
        "channel_id": "UCNcTu7X1Obwt2kkX-vXy6qg",
        "seo_keywords": "travel,adventure,tips,solo female,packing,stories,budget hacks,culture,vlogs,beaches"
    },
    {
        "title": "Travel Beans",
        "subscribers": "0.40M",
        "channel_id": "UC43nr_7R0dG6a9OhclJidLg",
        "seo_keywords": "couple travel,adventures,vlogs,van life,beaches,hostels,budget tips,road trips,stories,fun"
    },
    {
        "title": "Eileen Aldis",
        "subscribers": "0.33M",
        "channel_id": "UCtn7FZ2CmrX3cO9Bn0wSAfA",
        "seo_keywords": "travel guides,city tours,adventure,food,stories,culture,budget tips,vlogs,photography,experiences"
    },
    {
        "title": "The Endless Adventure",
        "subscribers": "0.30M",
        "channel_id": "UCEjkioV3LO_OIUaSWRxFZ3A",
        "seo_keywords": "travel,vlogs,adventure,beaches,road trips,food,culture,budget tips,camping,experiences"
    },
    {
        "title": "Expert Vagabond",
        "subscribers": "0.25M",
        "channel_id": "UCexpertVagabondID",
        "seo_keywords": "travel,adventure,photography,backpacking,solo travel,budget tips,extreme sports,culture,stories,off the beaten path"
    },
    {
        "title": "RayaWasHere",
        "subscribers": "0.22M",
        "channel_id": "UCftZQn4W3Z0nUVtbBGngMwA",
        "seo_keywords": "travel,vegan,solo female,road trips,backpacking,beaches,culture,stories,budget tips,global"
    },
    {
        "title": "PsychoTraveller",
        "subscribers": "0.21M",
        "channel_id": "UCseh2gFytJCiZkQZIiM70mA",
        "seo_keywords": "travel,backpacking,solo female,beaches,motivation,hostels,budget tips,advice,stories,adventure"
    },
    {
        "title": "Backpacking Bananas",
        "subscribers": "0.19M",
        "channel_id": "UCZpJXeRhzaO7NdqLy3T9KHw",
        "seo_keywords": "backpacking,travel,hostels,solo female,budget tips,culture,gap year,adventure,beaches,stories"
    },
    {
        "title": "Karl Watson: Travel Documentaries",
        "subscribers": "0.16M",
        "channel_id": "UCf3bTHFMB7fDHa4Z3FhTImA",
        "seo_keywords": "travel,documentaries,backpacking,adventure,culture,stories,hostels,filmmaking,budget tips,experiences"
    },
    {
        "title": "Chase for Adventure",
        "subscribers": "0.16M",
        "channel_id": "UCchaseForAdventureID",
        "seo_keywords": "travel,world tour,couple,backpacking,beaches,digital nomad,budget,adventure,stories,culture"
    },
    {
        "title": "The Travel Vlogger",
        "subscribers": "0.14M",
        "channel_id": "UCtheTravelVloggerID",
        "seo_keywords": "travel vlogs,city guides,local experiences,culture,food,history,adventure,budget tips,beaches,walking tours"
    },
    {
        "title": "ProjectAtticus",
        "subscribers": "0.13M",
        "channel_id": "UCprojectAtticusID",
        "seo_keywords": "travel,sailing,adventure,couple,world tour,boat life,beaches,off grid,vlogs,budget"
    },
    {
        "title": "Expedition Evans",
        "subscribers": "0.12M",
        "channel_id": "UCexpeditionEvansID",
        "seo_keywords": "travel,sailing,adventure,restoration,off grid,couple vlogs,oceans,beaches,liveaboard,stories"
    }
]

print(json.dumps(channels, indent=2))

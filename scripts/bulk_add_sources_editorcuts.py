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


genre = "Video Editing"

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
        "title": "Peter McKinnon",
        "subscribers": "5.90M",
        "channel_id": "UC3DkFux8Iv-aYnTRWzwaiBA",
        "keywords": "video editing, cinematography, filmmaking, tutorials, camera gear, premiere pro, photography, vlogs, creative process, transitions"
    },
    {
        "title": "Cinecom.net",
        "subscribers": "2.70M",
        "channel_id": "UCpLfM1pP0k2Uo5tIMgC34OA",
        "keywords": "video editing, after effects, premiere pro, filmmaking, effects, transitions, tutorials, tips and tricks, color grading, vfx"
    },
    {
        "title": "Daniel Schiffer",
        "subscribers": "2.48M",
        "channel_id": "UCGjB2iMSpT-Z4h0CkvQ3orQ",
        "keywords": "b-roll, transitions, filmmaking, video editing, premiere pro, cinematic, tutorials, tips, camera hacks, product videos"
    },
    {
        "title": "Full Time Filmmaker",
        "subscribers": "2.19M",
        "channel_id": "UC5cPHGtDkW3XDzIMy6YdbSw",
        "keywords": "video editing, filmmaking, premiere pro, cinematography, gear review, tutorials, wedding films, color grading, transitions, vlogs"
    },
    {
        "title": "Film Riot",
        "subscribers": "2.12M",
        "channel_id": "UC6PXD9iV5tXkEqWeiwOS8kg",
        "keywords": "filmmaking, tutorials, visual effects, video editing, gear, short films, after effects, directing, post production, tips"
    },
    {
        "title": "Make.Art.Now",
        "subscribers": "1.29M",
        "channel_id": "UCmRElY3j2xd5z1em4gA6Zyg",
        "keywords": "filmmaking, editing, creative process, camera gear, vfx, tutorials, premiere pro, cinematic, color grading, tips"
    },
    {
        "title": "tutvid",
        "subscribers": "1.23M",
        "channel_id": "UC8AEB4Rc8FrYIR7SfqCF7yQ",
        "keywords": "photoshop, video editing, premiere pro, after effects, tutorials, design, color grading, compositing, tips, motion graphics"
    },
    {
        "title": "Matti Haapoja",
        "subscribers": "1.20M",
        "channel_id": "UCbvIIQc5Jo9-jIXnkPe03oA",
        "keywords": "filmmaking, cinematography, vlogs, video editing, travel, premiere pro, camera gear, tips, tutorials, transitions"
    },
    {
        "title": "DSLRguide",
        "subscribers": "1.19M",
        "channel_id": "UCdm1_rdrN3lq6TPXv4mlsyg",
        "keywords": "filmmaking, dslr, editing, tutorials, gear, premiere pro, storytelling, cinematography, tips, camera basics"
    },
    {
        "title": "Justin Odisho",
        "subscribers": "1.15M",
        "channel_id": "UCy3cOo_z2ZJBg6hD6AyxK7g",
        "keywords": "premiere pro, after effects, editing tutorials, effects, transitions, color grading, short tips, creative workflow, design, vfx"
    },
    {
        "title": "Potato Jet",
        "subscribers": "1.05M",
        "channel_id": "UCYqHmFNT0-HE3S4x0gjYqMQ",
        "keywords": "filmmaking, gear reviews, comedic style, vlogging, editing, cinematography, camera tests, tutorials, tips, fun"
    },
    {
        "title": "Brandon Li",
        "subscribers": "810K",
        "channel_id": "UC6Unb9mUR6Yi0vCBGpEIx-Q",
        "keywords": "travel films, cinematic, editing, filmmaking, premiere pro, transitions, tips, storytelling, vlog, color grading"
    },
    {
        "title": "Chris Hau",
        "subscribers": "790K",
        "channel_id": "UCZ3IHc9QHsaY8CO3uZR7jDw",
        "keywords": "cinematic, vlogs, tutorials, editing tips, color grading, filmmaking, transitions, camera gear, b-roll, lifestyle"
    },
    {
        "title": "Premiere Gal",
        "subscribers": "505K",
        "channel_id": "UCcTlQJ3JL2B-OaXMBCcvIlw",
        "keywords": "premiere pro, after effects, video editing, tutorials, motion graphics, color grading, templates, transitions, tips, workflow"
    },
    {
        "title": "YCImaging",
        "subscribers": "497K",
        "channel_id": "UCZqkRu76QM1dV1DC4FT42nQ",
        "keywords": "music video, filmmaking, editing, color grading, cinematography, tutorials, gear reviews, transitions, business tips, vlogs"
    },
    {
        "title": "Fenchel & Janisch",
        "subscribers": "320K",
        "channel_id": "UCivgOLb2Osq8l2HS9G7Z-XQ",
        "keywords": "cinematography, gear, color grading, premiere pro, tutorials, short films, vfx, slow motion, editing, storytelling"
    },
    {
        "title": "Kyler Holland",
        "subscribers": "220K",
        "channel_id": "UCpR-y2yAyZqm7p71k1PN5_w",
        "keywords": "premiere pro, after effects, transitions, editing, tips, travel, glitch effects, cinematography, color grading, presets"
    },
    {
        "title": "The Basic Filmmaker",
        "subscribers": "210K",
        "channel_id": "UCp1HDUvuxQAUvgCLK-BC1vQ",
        "keywords": "filmmaking, editing, tutorials, gear tips, camera basics, premiere pro, lighting, cinematic, directing, color grading"
    },
    {
        "title": "Olufemii",
        "subscribers": "190K",
        "channel_id": "UCnk6eq9y7Bggqk6vWucrvqw",
        "keywords": "premiere pro, after effects, transitions, templates, tutorials, vfx, editing tips, color grading, music videos, motion graphics"
    },
    {
        "title": "Richard Kraus",
        "subscribers": "130K",
        "channel_id": "UCfY4KvoPh9d6Y4xeG5zV1Iw",
        "keywords": "video editing, film tips, color grading, transitions, premiere pro, filmmaking, gear, tutorials, short films, vfx"
    },
    {
        "title": "Jakter",
        "subscribers": "125K",
        "channel_id": "UCgIMYdWe2FP0C22uVzrxQYQ",
        "keywords": "premiere pro, editing, transitions, color grading, cinematic, gear, after effects, tutorials, effects, vlogs"
    },
    {
        "title": "MiesnerMedia",
        "subscribers": "120K",
        "channel_id": "UCrkQQHfKB6s84s5GOOW4mRA",
        "keywords": "video editing, color grading, story, premiere pro, tutorials, gear, filmmaking, tips, compositing, behind the scenes"
    },
    {
        "title": "Brian Jackson",
        "subscribers": "111K",
        "channel_id": "UCTh_2SGx0FMgES6WeHd8S9Q",
        "keywords": "video editing, tutorials, premiere pro, after effects, transitions, gear, color grading, music videos, cinematic, effects"
    },
    {
        "title": "Coffee & Celluloid",
        "subscribers": "100K",
        "channel_id": "UC3vtdTlNI27QNM4Eegnh2NQ",
        "keywords": "filmmaking, editing, behind the scenes, gear talk, color grading, short films, camera basics, transitions, vfx, creative tips"
    },
    {
        "title": "Robbie Janney",
        "subscribers": "95K",
        "channel_id": "UCVn3ghDsGAGp3xzX-f07KHw",
        "keywords": "premiere pro, vfx, transitions, editing, tutorials, color grading, motion graphics, filming tips, gear, creative process"
    }
]


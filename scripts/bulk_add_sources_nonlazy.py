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


genre = "Motivation and Productivity"

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
        "title": "Be Inspired",
        "subscribers": "8.70M",
        "channel_id": "UCJlnhc22dfZJK7blZqX4LgA",
        "seo_keywords": "side hustle,motivation,success,inspiration,personal growth,mindset,business,hustle culture,positivity,transformation"
    },
    {
        "title": "Charisma on Command",
        "subscribers": "6.50M",
        "channel_id": "UCsiYzPez0i3NeSwjEZx8yOg",
        "seo_keywords": "motivation,communication,personal development,self improvement,confidence,success,relationships,charisma,social skills,mindset"
    },
    {
        "title": "Jay Shetty",
        "subscribers": "5.08M",
        "channel_id": "UCbV60AGIHKz2xIGvbk0LLvg",
        "seo_keywords": "motivation,inspiration,mindset,wellness,productivity,relationships,success,life lessons,positivity,self growth"
    },
    {
        "title": "Ali Abdaal",
        "subscribers": "4.71M",
        "channel_id": "UCoOae5nYA7VqaXzerajD0lg",
        "seo_keywords": "productivity,study tips,side hustle,personal finance,self improvement,medicine,entrepreneurship,motivation,tech,habits"
    },
    {
        "title": "GaryVee",
        "subscribers": "4.25M",
        "channel_id": "UCctXZhXmG-kf3tlIXgVZUlw",
        "seo_keywords": "motivation,entrepreneurship,hustle,marketing,business,branding,side hustle,mindset,leadership,success"
    },
    {
        "title": "Evan Carmichael",
        "subscribers": "3.85M",
        "channel_id": "UCEc3UCLEV0avc8y2VLc8ZeA",
        "seo_keywords": "motivation,success,entrepreneurship,advice,leadership,personal development,habits,business,belief,mindset"
    },
    {
        "title": "Matt D'Avella",
        "subscribers": "3.46M",
        "channel_id": "UCsYUDKxTlvus46h4XMFm39w",
        "seo_keywords": "minimalism,productivity,habits,creativity,lifestyle design,side hustle,personal growth,films,motivation,routines"
    },
    {
        "title": "Better Ideas",
        "subscribers": "3.30M",
        "channel_id": "UCp1v_y4KLGXuSn2Uzax7N7g",
        "seo_keywords": "motivation,productivity,habits,self improvement,mindset,creativity,success,side hustle,psychology,time management"
    },
    {
        "title": "Thomas Frank",
        "subscribers": "2.91M",
        "channel_id": "UCG-KntY7aVnIGXYEBQvmBAQ",
        "seo_keywords": "productivity,studying,skills,habits,focus,side hustle,organization,personal finance,motivation,technology"
    },
    {
        "title": "Improvement Pill",
        "subscribers": "2.76M",
        "channel_id": "UCVkQ5i6R6ttZsqfTU4y2GCQ",
        "seo_keywords": "self improvement,productivity,motivation,side hustle,mindset,psychology,success,habits,education,inspiration"
    },
    {
        "title": "Team Fearless",
        "subscribers": "2.60M",
        "channel_id": "UCf9_s9ii6BZ-klpgmtIi3WQ",
        "seo_keywords": "motivation,inspiration,self help,success,personal growth,confidence,mindset,discipline,goals,achievement"
    },
    {
        "title": "Brian Tracy",
        "subscribers": "2.60M",
        "channel_id": "UCFzF6JtA7u7M2KNPrxNFPEA",
        "seo_keywords": "motivation,goal setting,time management,productivity,leadership,business,sales,mindset,success,personal growth"
    },
    {
        "title": "Tony Robbins",
        "subscribers": "1.55M",
        "channel_id": "UCJLMboBYME_CV2P9W-KX4MQ",
        "seo_keywords": "motivation,peak performance,personal development,success,leadership,relationship,finance,goal setting,energy,mindset"
    },
    {
        "title": "Mel Robbins",
        "subscribers": "1.53M",
        "channel_id": "UCOz-UDnw4w6w3mQq6bOw2Cg",
        "seo_keywords": "motivation,self help,5 second rule,confidence,mindset,habits,personal development,productivity,advice,inspiration"
    },
    {
        "title": "Nate O'Brien",
        "subscribers": "1.30M",
        "channel_id": "UCtYzVCmNxrshH4_bPO_-Y-A",
        "seo_keywords": "personal finance,self development,productivity,investing,minimalism,side hustles,motivation,entrepreneurship,wealth,psychology"
    },
    {
        "title": "Better Than Yesterday",
        "subscribers": "1.20M",
        "channel_id": "UCdyQBBAT6MduC-8C3yRda4Q",
        "seo_keywords": "motivation,mindset,personal growth,productivity,self help,habits,success,achievements,side hustle,inspiration"
    },
    {
        "title": "The Financial Diet",
        "subscribers": "1.05M",
        "channel_id": "UCGkBvCUGnGajf7qNxfOsyxw",
        "seo_keywords": "finance,productivity,side hustles,frugality,career,money management,motivation,budgeting,self improvement,investing"
    },
    {
        "title": "Rich Roll",
        "subscribers": "1.02M",
        "channel_id": "UCggQ4t4PcH2D2Q6ACVUG8QQ",
        "seo_keywords": "motivation,health,productivity,self improvement,interviews,personal development,wellness,success,mindset,inspiration"
    },
    {
        "title": "Goal Guys",
        "subscribers": "0.967M",
        "channel_id": "UC5BPuw0YmyPodhhH7kwiaeg",
        "seo_keywords": "goals,productivity,self improvement,fitness,motivation,side hustle,habits,personal growth,challenge,time management"
    },
    {
        "title": "Vanessa Lau",
        "subscribers": "0.600M",
        "channel_id": "UC6f66SSE9ZKc_uJ8mJj2B3g",
        "seo_keywords": "social media,business,marketing,side hustle,motivation,entrepreneurship,coaching,personal branding,content creation,productivity"
    },
    {
        "title": "Mike Vestil",
        "subscribers": "0.600M",
        "channel_id": "UCYGBwGvNh7Sui6SiWF6TjwA",
        "seo_keywords": "side hustle,online business,entrepreneurship,personal finance,motivation,wealth building,productivity,marketing,branding,passive income"
    },
    {
        "title": "Andrew Kirby",
        "subscribers": "0.500M",
        "channel_id": "UCdcZ4MA2Z2-HhnhBLHkm4Mg",
        "seo_keywords": "productivity,philosophy,side hustle,motivation,personal growth,self help,habits,deep work,finance,experiments"
    },
    {
        "title": "Pat Flynn (Smart Passive Income)",
        "subscribers": "0.409M",
        "channel_id": "UCEeBxznV3dO6Ch9h-dz_h0g",
        "seo_keywords": "side hustle,passive income,entrepreneurship,online business,podcast,affiliate marketing,blogging,marketing,motivation,leadership"
    },
    {
        "title": "Project Elon",
        "subscribers": "0.200M",
        "channel_id": "UCq2uHkM4BIXJJ6kiKr1lqfA",
        "seo_keywords": "productivity,study tips,side hustle,motivation,learning,personal growth,students,focus,discipline,success"
    },
    {
        "title": "Carl Konadu",
        "subscribers": "0.150M",
        "channel_id": "UCSJz0S0F6mf6jPrqVLrY2fg",
        "seo_keywords": "motivation,public speaking,self improvement,personal development,leadership,goal setting,productivity,side hustle,mindset,success"
    }
]


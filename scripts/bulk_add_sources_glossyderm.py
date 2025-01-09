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


genre = "Skincare"

for channel in channels:
  channel['prompt_video'] = f"Please summarize in 3 paragraphs, for a blog post, with a playfully sarcastic and witty tone, this Youtube video transcript for a youtube channel named {channel['title']} in the {genre} genre for a blog post as a loyal fan. Utilize the following keywords for SEO: {channel['keywords']}.  Assume you are writing for a familiar audience.  Don't use 'he', 'I', 'we' or 'you', refer to the channel as {channel['title']} mostly.  You are not {channel['title']}.  Don't mention sponsors of the video. "
  channel['prompt_comments'] = f"Please summarize these comments for a youtube video by {channel['title']} in the {genre} genre.  Point out anything that might be of interest that you would have to watch the video to know.  Analyze what the viewers are thinking in as many bullet points are necessary.  Format the response for a blog post.  Do not sound like a robot or AI."
  channel['active'] = True
  channel['pending'] = False
  channel['authority'] = 1
  channel['owner'] = "glossyderm"
  channel['platform_id'] = platforms.getPlatformIdByTitle('Youtube')['_id']
  channel['createdAt'] = datetime.utcnow()
  sources.createNewSource(channel)



channels_data = [
    {
        "title": "James Welsh",
        "subscribers": "1.50M",
        "channel_id": "UC2oRyU8jOdz8kF36XDqXkEQ",
        "keywords": "Skincare, Education, Reviews, Beauty, Tutorials, Routines, Tips, Product, Lifestyle, Face"
    },
    {
        "title": "Mixed Makeup",
        "subscribers": "1.50M",
        "channel_id": "UC-oUgCw7tMI9KkReV5Rr0wA",
        "keywords": "Skincare, Beauty, Reviews, Tutorials, Health, Lifestyle, Products, Routines, Makeup, Tips"
    },
    {
        "title": "Dr Dray",
        "subscribers": "1.61M",
        "channel_id": "UCF6PrdPs659QZy3plgmEDCw",
        "keywords": "Dermatologist, Skincare, Science, Health, Advice, Product, Reviews, Routine, Beauty, Education"
    },
    {
        "title": "Liah Yoo",
        "subscribers": "1.24M",
        "channel_id": "UC-ov4y1K9Q6H7ZkOinbaw7w",
        "keywords": "Skincare, Tips, K-Beauty, Lifestyle, Reviews, Routine, Acne, Health, Glow, Education"
    },
    {
        "title": "Wishtrend TV",
        "subscribers": "1.37M",
        "channel_id": "UChrS2z44PT6Zid7yFXbLHXg",
        "keywords": "K-Beauty, Products, Skincare, Tutorials, Acne, Routines, Glow, Health, Tips, Lifestyle"
    },
    {
        "title": "Beauty Within",
        "subscribers": "3.16M",
        "channel_id": "UCr8O8l5cCX85Oem1d18EezA",
        "keywords": "Skincare, Beauty, Routines, Tips, Wellness, Products, Glow, Health, Tutorials, Education"
    },
    {
        "title": "Susan Yara",
        "subscribers": "514K",
        "channel_id": "UC0HudN4q81QVI3l0d0q9fhg",
        "keywords": "Skincare, Beauty, Lifestyle, Product, Reviews, Education, Routine, Advice, Glow, Health"
    },
    {
        "title": "Michelle Phan",
        "subscribers": "8.86M",
        "channel_id": "UCuYx81nzzz4OFQrhbKDzTng",
        "keywords": "Beauty, Skincare, Makeup, Tutorials, Lifestyle, Tips, Products, Brand, Innovator, Inspiration"
    },
    {
        "title": "Gothamista",
        "subscribers": "699K",
        "channel_id": "UC8v4vz_n2rys6Yxpj8LuOmg",
        "keywords": "Skincare, Reviews, Routines, Products, Glow, Beauty, Advice, Education, Tips, Testing"
    },
    {
        "title": "Lab Muffin Beauty Science",
        "subscribers": "483K",
        "channel_id": "UCpbyqZ4tbEHxP2Fa3Eptbnw",
        "keywords": "Science, Beauty, Skincare, Education, Evidence-based, Myth-busting, Reviews, Products, Health, Tips"
    },
    {
        "title": "Dr Sam Bunting",
        "subscribers": "205K",
        "channel_id": "UCJZ3kC4Fd9QZkRavrU4rP8Q",
        "keywords": "Dermatologist, Skincare, Science, Routine, Advice, Product, Acne, Glow, Education, Expert"
    },
    {
        "title": "Dr Vanita Rattan",
        "subscribers": "1.25M",
        "channel_id": "UC1Z7h03ZkNDETsv3bOWDumw",
        "keywords": "Skincare, Hyperpigmentation, Science, Product, Advice, Routine, Education, Dermatology, Treatments, Glow"
    },
    {
        "title": "LAMUQE",
        "subscribers": "1.77M",
        "channel_id": "UCb6vGDnYB3mdSLZ__IlDsPw",
        "keywords": "K-Beauty, Makeup, Skincare, Tutorials, Glow, Advice, Products, Routines, Health, Lifestyle"
    },
    {
        "title": "Beauty Break",
        "subscribers": "1.80M",
        "channel_id": "UCtnnpCF9Mqm74vq53E7PiLA",
        "keywords": "Makeup, Skincare, Reviews, Tutorials, Fun, Trends, Glow, Lifestyle, Tips, Product"
    },
    {
        "title": "Tina Tanaka Harris",
        "subscribers": "280K",
        "channel_id": "UC5Ks6ccZB8M4Bg2rr05ygOA",
        "keywords": "Skincare, Beauty, Minimalism, Japanese, Lifestyle, Product, Glow, Tips, Reviews, Routine"
    },
    {
        "title": "The Budget Dermatologist",
        "subscribers": "530K",
        "channel_id": "UCn6wpHy1RMSbrPY6I0naIng",
        "keywords": "Dermatology, Affordable, Skincare, Product, Advice, Routine, Tips, Glow, Health, Science"
    },
    {
        "title": "QOVES Studio",
        "subscribers": "207K",
        "channel_id": "UCg1OIoHqrKu7IfNAUJkfSDw",
        "keywords": "Facial Aesthetics, Skincare, Beauty, Analysis, Science, Routine, Glow, Advice, Treatments, Education"
    },
    {
        "title": "Dr Davin Lim",
        "subscribers": "617K",
        "channel_id": "UC2YUPmPtYVqLFz9FWMvHnxA",
        "keywords": "Dermatology, Skincare, Treatments, Laser, Advice, Science, Glow, Routine, Education, Product"
    },
    {
        "title": "Cassandra Bankson",
        "subscribers": "2.08M",
        "channel_id": "UCDPdhcAMEXW5FZ7R5nxGbHA",
        "keywords": "Skincare, Acne, Advice, Beauty, Tips, Products, Education, Lifestyle, Glow, Science"
    },
    {
        "title": "Skincare by Alana",
        "subscribers": "50K",
        "channel_id": "UCWdBBcGoKKvhqiyHU2J4c1A",
        "keywords": "Skincare, Advice, Product, Education, Glow, Routine, Reviews, Beauty, Health, Tips"
    },
    {
        "title": "TheGoldenRx",
        "subscribers": "370K",
        "channel_id": "UCebOMeyFcCu9l09u1hV8O3g",
        "keywords": "Skincare, Tips, Glow, Advice, Routine, Education, Product, Health, Beauty, Treatments"
    },
    {
        "title": "Jen Luv",
        "subscribers": "294K",
        "channel_id": "UCR96t_gBHzl2hZSvMkz6INA",
        "keywords": "Beauty, Skincare, Reviews, Product, Advice, Analysis, Tips, Education, Makeup, Consumer"
    },
    {
        "title": "Dr Alexis Stephens",
        "subscribers": "200K",
        "channel_id": "UCT2ryNF883mX2GP7zJ9tk6A",
        "keywords": "Dermatologist, Skincare, Glow, Advice, Routine, Science, Education, Beauty, Health, Product"
    },
    {
        "title": "Aly Art",
        "subscribers": "1.58M",
        "channel_id": "UCQ9dA_ZAezxlufxePeH6Nhg",
        "keywords": "Beauty, Skincare, Analysis, Advice, Body Types, Glow, Lifestyle, Tips, Makeup, Style"
    }

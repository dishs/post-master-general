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


genre = "Artificial Intelligence"

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
        "title": "Edureka",
        "subscribers": "3.53M",
        "channel_id": "UCkw4JCwteGrDHIsyIIKo4tQ",
        "seo_keywords": "artificial intelligence,machine learning,deep learning,data science,tech tutorials,edtech,python,cloud computing,online courses,automation"
    },
    {
        "title": "Simplilearn",
        "subscribers": "3.00M",
        "channel_id": "UCsvqVGtbbyHaMoevxPaEDtg",
        "seo_keywords": "AI,machine learning,data science,devops,big data,certifications,tech education,deep learning,analytics,python"
    },
    {
        "title": "Lex Fridman",
        "subscribers": "3.00M",
        "channel_id": "UCSHZKyawb77ixDdsGog4iWA",
        "seo_keywords": "AI,podcasts,deep learning,robotics,philosophy,technology,computer science,research,interviews,autonomous vehicles"
    },
    {
        "title": "Code Bullet",
        "subscribers": "2.81M",
        "channel_id": "UC0e3QhIYukixgh5VVpKHH9Q",
        "seo_keywords": "AI,gaming,programming,neural networks,genetic algorithms,entertainment,coding,simulation,experiments,automation"
    },
    {
        "title": "Computerphile",
        "subscribers": "2.35M",
        "channel_id": "UC9-y-6csu5WGm29I7JiwpnA",
        "seo_keywords": "computing,AI,algorithms,programming,security,data science,cryptography,machine learning,tech,explanations"
    },
    {
        "title": "Two Minute Papers",
        "subscribers": "1.81M",
        "channel_id": "UCbfYPyITQ-7l4upoX8nvctg",
        "seo_keywords": "AI,research,papers,deep learning,computer graphics,simulation,neural networks,technology,science,innovation"
    },
    {
        "title": "TechLead",
        "subscribers": "1.70M",
        "channel_id": "UC4xKdmAXFh4ACyhpiQ_3qBw",
        "seo_keywords": "tech,AI,software engineering,programming,career,finance,crypto,machine learning,commentary,productivity"
    },
    {
        "title": "sentdex",
        "subscribers": "1.32M",
        "channel_id": "UCfzlCWGWYyIQ0aLC5w48gBQ",
        "seo_keywords": "python,AI,machine learning,deep learning,data science,tutorials,finance,algorithms,nlp,automation"
    },
    {
        "title": "Andrew Ng",
        "subscribers": "1.14M",
        "channel_id": "UCvQIGs80i0ju6UFHoJeqP5w",
        "seo_keywords": "AI,coursera,machine learning,deep learning,data science,Stanford,education,neural networks,ML ops,academia"
    },
    {
        "title": "Krish Naik",
        "subscribers": "790K",
        "channel_id": "UCNU_lfiiWBdtULKOw6X0Dig",
        "seo_keywords": "AI,machine learning,data science,python,deep learning,career guidance,live sessions,projects,tech tips,analytics"
    },
    {
        "title": "Siraj Raval",
        "subscribers": "720K",
        "channel_id": "UCWN3xxRkmTPmbKwht9FuE5A",
        "seo_keywords": "AI,machine learning,deep learning,programming,python,data science,tutorials,education,research,automation"
    },
    {
        "title": "Yannic Kilcher",
        "subscribers": "600K",
        "channel_id": "UCZHmQk67mSJgfCCTn7xBfew",
        "seo_keywords": "AI,ml papers,deep learning,research,transformers,neural networks,analysis,education,tech,discussion"
    },
    {
        "title": "Kaggle",
        "subscribers": "530K",
        "channel_id": "UCcoEtF2EM4nXx3N9RHIMNSg",
        "seo_keywords": "data science,machine learning,AI,competitions,analytics,coding tutorials,datasets,community,python,cloud"
    },
    {
        "title": "DeepMind",
        "subscribers": "380K",
        "channel_id": "UCP7jMXSY2xbc3KCAE0MHQ-A",
        "seo_keywords": "AI,deep learning,research,reinforcement learning,neuroscience,robotics,innovation,published papers,healthcare,games"
    },
    {
        "title": "Ken Jee",
        "subscribers": "280K",
        "channel_id": "UCiT9RITQ9PW6BhXK0y2jaeg",
        "seo_keywords": "data science,machine learning,AI,projects,career advice,kaggle,analytics,python,visualization,practical tips"
    },
    {
        "title": "NeuralNine",
        "subscribers": "239K",
        "channel_id": "UC8wZnXYK_CGKlBcZp-GxYPA",
        "seo_keywords": "python,AI,machine learning,automation,deep learning,projects,coding tutorials,neural networks,development,tech"
    },
    {
        "title": "AI and Games",
        "subscribers": "200K",
        "channel_id": "UCov_51F0betb6hJ6H9aIMAQ",
        "seo_keywords": "AI,gaming,reinforcement learning,game dev,analysis,design,computer science,ML,algorithms,education"
    },
    {
        "title": "OpenAI",
        "subscribers": "185K",
        "channel_id": "UCTO1pHTofIlC2oiY-cZNOew",
        "seo_keywords": "AI,research,chatgpt,deep learning,transformers,robotics,technology,innovation,open source,policy"
    },
    {
        "title": "Brandon Rohrer",
        "subscribers": "160K",
        "channel_id": "UC2XsHkVjaJtU4k7UK9iLXTg",
        "seo_keywords": "AI,machine learning,data science,explanations,neural networks,visual tutorials,ML tips,analytics,python,education"
    },
    {
        "title": "Arxiv Insights",
        "subscribers": "140K",
        "channel_id": "UCEukx5uizjK-kbtuiJUcK9w",
        "seo_keywords": "AI,research papers,deep learning,transformers,analysis,neural networks,ML news,education,science,tech"
    },
    {
        "title": "Aladdin Persson",
        "subscribers": "70K",
        "channel_id": "UCkzW5JSFwvKRjXABI-6rQXA",
        "seo_keywords": "AI,machine learning,deep learning,python,projects,tutorials,neural nets,ml frameworks,education,implementation"
    },
    {
        "title": "Henry AI Labs",
        "subscribers": "54K",
        "channel_id": "UCkjvzz4n2npKHAy6UN69i8w",
        "seo_keywords": "AI,machine learning,deep learning,paper reviews,transformers,model demos,education,tech news,analysis,frameworks"
    },
    {
        "title": "The AI Hacker",
        "subscribers": "50K",
        "channel_id": "UCBhosmHf2Y8zC1GzY14LFVg",
        "seo_keywords": "AI,projects,hacking,ML,neural networks,programming,tutorials,innovation,python,automation"
    },
    {
        "title": "AI Coffee Break with Letitia",
        "subscribers": "42K",
        "channel_id": "UCmorRRA6yLPfFU32fXNGkIg",
        "seo_keywords": "AI,tech talks,machine learning,explanations,projects,community,discussions,deep learning,neural networks,innovation"
    },
    {
        "title": "Neural Networks",
        "subscribers": "36K",
        "channel_id": "UCb3D0PZd13EtLq1EvD7N-BA",
        "seo_keywords": "neural networks,AI,deep learning,projects,ML tutorials,programming,education,python,frameworks,data science"
    }
]

print(json.dumps(channels, indent=2))

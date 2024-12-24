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
        "title": "Donut",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCL6JmiMXKoXS6bpP1D3bk8g",
        "keywords": "car culture, automotive history, car news, up to speed series, car evolution, car facts, car tech, automotive trends, car stories, high-performance vehicles, car science, vehicle design evolution, Donut Media podcasts, car enthusiast content, racing news"
    },
    {
        "title": "Jay Leno's Garage",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCQMELFlXQL38KPm8kM-4Adg",
        "keywords": "classic cars, car collections, celebrity car enthusiasts, rare cars, Jay Leno interviews, vintage cars, muscle cars, supercars, car restorations, Jay Leno car reviews, automotive history, unique vehicles, car maintenance tips, garage tours, custom-built cars"
    },
    {
        "title": "Regular Car Reviews",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCo1pShh6dtg-T_ZZkgi_JDQ",
        "keywords": "car reviews, daily driver reviews, regular car reviews, car humor, car culture, automotive commentary, car vlogs, budget cars, car stories, car test drives, vehicle history, car comparisons, common car reviews"
    },
    {
        "title": "Saabkyle04",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2dBZuI6gS-jv7PCIDXkXag",
        "keywords": "car reviews, in-depth reviews, new model overviews, car test drives, vehicle performance tests, detailed car reviews, car features explanations, automotive technology insights, new car showcases, car interior reviews, vehicle reviews, road tests, driving impressions"
    },
    {
        "title": "Tavarish",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCvAhDxNNUDhi78tMXVGBUaQ",
        "keywords": "car restoration, car build, flooded McLaren P1 rebuild, project car, rebuild, salvage cars, modified cars, custom cars, car projects, restoration project, budget build, automotive DIY, car flipping, car repair vlogs, project car updates"
    },
    {
        "title": "Petrolicious",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCgyJPixJl95X1ut3E9K99KA",
        "keywords": "classic cars, vintage cars, car stories, car culture, Petrolicious drives, car collector stories, automotive history, iconic cars, car photography, car films, rare cars, historic cars, car enthusiast stories, car lifestyle, Petrolicious interviews"
    },
    {
        "title": "TheSmokingTire",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCgeGealT0QYcrnoYRMltDZg",
        "keywords": "car reviews, one take reviews, car podcasts, automotive discussions, The Smoking Tire test drives, car commentary, car news, vehicle insights, car enthusiast content, performance car reviews, car buying guides, new car reviews, car vlogs, driving impressions, automotive trends"
    },
    {
        "title": "Car Throttle",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCNBbCOuAN1NZAuj0vPe_MkA",
        "keywords": "car memes, car culture, automotive news, car throttle quizzes, car communities, car mods, car humor, car enthusiast content, auto DIY, car reviews, project cars, car discussions, car buying guides, car maintenance tips, automotive lifestyle"
    },
    {
        "title": "Hoovies Garage",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCdEczn3MVkx_4PnMZ10MVFA",
        "keywords": "car auctions, cheap cars, Hoovies Garage projects, car repairs, car challenges, automotive adventures, car reviews, car restoration, car collection, automotive vlogs, luxury cars, buying used cars, cheap sports cars, car maintenance, budget car builds"
    },
    {
        "title": "Seen Through Glass",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCrBr8w4ki1xAcQ1JVDp_-Fg",
        "keywords": "car vlogs, luxury cars, supercars, car reviews, car events, automotive lifestyle, car travels, exotic cars, car photography, car culture, Seen Through Glass reviews, car adventures, driving tours, car collection tours, automotive experiences"
    },
    {
        "title": "Salomondrin",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCiGMIk8oeayv91jjTgm-CIw",
        "keywords": "car news, car vlogs, supercars, hypercars, car reviews, Salomondrin’s garage, automotive discussions, luxury cars, car buying advice, car comparisons, car events, automotive lifestyle, car collection, car enthusiast content, high-end cars"
    },
    {
        "title": "SavageGeese",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCgUvk6jVaf-1uKOqG8XNcaQ",
        "keywords": "car reviews, automotive engineering, car comparisons, vehicle testing, technical car reviews, in-depth car reviews, automotive industry insights, car technology, vehicle dynamics, car maintenance tips, new car features, detailed vehicle reviews, car buying guide, automotive trends, car mechanics"
    },
    {
        "title": "Scotty Kilmer",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCuxpxCCevIlF-k-K5YU8XPA",
        "keywords": "car repair, auto maintenance, mechanic advice, car fixing tips, car life hacks, DIY car repair, automotive technology, car troubleshooting, car review, Scotty Kilmer tips, vehicle maintenance, car care tips, repair tutorials, car mod advice, mechanic life"
    },
    {
        "title": "AutoTopNL",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC9DXAsBD4-ITVuvpd68401Q",
        "keywords": "car reviews, high-speed runs, POV driving videos, performance tests, top speed runs, AutoTopNL reviews, car comparisons, first drives, car testing, automotive news, car sound, driving impressions, performance car reviews, exhaust sound, high-performance vehicles"
    },
    {
        "title": "Hoonigan",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCXlfi8sf6cKGQ8sOd0-yRuw",
        "keywords": "car culture, motorsports, car build offs, Hoonigan racing, this vs that, automotive lifestyle, car stunts, drift culture, car build projects, garage life, car challenges, motorsport events, car mods, racing series, Hoonigan daily transmission"
    },
    {
        "title": "The Fast Lane Car",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC6S0jAvcapqJ48ZzLfva12g",
        "keywords": "car reviews, road tests, drag races, car comparisons, new car reviews, auto news, TFLcar tests, car buying advice, vehicle reviews, car test drives, automotive events, car rankings, vehicle technology insights, car features, automotive trends"
    },
    {
        "title": "B is for Build",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCl4-WBRqWA2MlxmZorKOV7w",
        "keywords": "car builds, custom cars, car restoration, car mods, DIY car builds, B is for Build projects, car repair, salvage rebuilds, car makeovers, automotive DIY, budget builds, car flipping, vehicle modifications, project cars, car transformation"
    },
    {
        "title": "Carfection",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCwuDqQjo53xnxWKRVfw_41w",
        "keywords": "high-quality car films, car reviews, Carfection documentaries, car stories, luxury cars, supercar reviews, classic car stories, automotive cinematography, car culture, in-depth car reviews, car adventures, iconic cars, car features, Carfection series, automotive craftsmanship"
    },
    {
        "title": "1320video",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC0PXqiud6dbwOAk8RvslgpQ",
        "keywords": "street racing, drag racing, car events, race coverage, 1320video races, car meets, racing events, car culture, high-performance cars, turbo cars, racing series, car interviews, race day coverage, drag racing events, car racing news"
    },
    {
        "title": "Adam LZ",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCXIYLgIp6DYZHjmUUUXErmg",
        "keywords": "car vlogs, car builds, drifting series, Adam LZ projects, car mods, automotive lifestyle, car reviews, car tours, drifting events, car adventures, automotive vlogs, car build series, car life"
    },
    {
        "title": "JR Garage",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCeTagg7gemi1jhFKhY6gcNw",
        "keywords": "car collection, supercar reviews, JR Garage adventures, car entrepreneurship, exotic cars, car investments, car flipping, buying and selling cars, young car enthusiasts, car rebuilds, car restorations, automotive tips, JR Garage projects, car vlogs, luxury car reviews"
    },
    {
        "title": "M539 Restorations",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCLLpxcworT8275nBXODXyqw",
        "keywords": "car restorations, project cars, M539 restoration projects, BMW restorations, car rebuilds, classic car restorations, DIY car repairs, car maintenance, vehicle restoration series, car renovations, car mechanical repairs, car restoration vlogs, car build series, car makeover, restoring old cars"
    },
    {
        "title": "Yiannimize",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCUHsXS2q7A7cTc8R6r31FRg",
        "keywords": "Car customizations, Luxury car modifications, Vinyl car wraps, Celebrity car wraps, Supercar transformations, Custom car interiors, Car detailing tutorials, Yiannimize car reviews, Luxury car tours, Unique car customizations, Bespoke car designs, Automotive vlogging, High-end car services, Vehicle customization tips, Custom car challenges"
    },
    {
        "title": "Davide Cironi",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCsD9nSAjE6uq1EPYlCORS9w",
        "keywords": "Italian car reviews, Classic car vlogs, Davide Cironi drives, Vintage car reviews, Italian automotive history, Classic car restoration, Sports car test drives, Motor racing insights, Classic Alfa Romeo, Iconic Ferrari reviews, Italian car culture, Auto industry interviews, Motor shows coverage, Italian supercars, Exotic car drives"
    },
    {
        "title": "SOL - Supercars of London",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCyoSWGYKkusssZWzRrsX4RA",
        "keywords": "Supercar vlogs, London car spotting, Exotic car reviews, Supercar reactions, Daily supercar drives, Luxury car lifestyle, London supercar culture, SOL exclusive drives, Supercar startup sounds, Hypercar test drives, Exclusive supercar events, High-speed car runs, Automotive adventures, Road trips with supercars, Supercar hunting"
    },
    {
        "title": "Gintani",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCoQtcj0e1mV7hotbIe76y_Q",
        "keywords": "Car tuning, Performance upgrades, Custom exhaust systems, Gintani project cars, Performance car tuning, ECU tuning, Custom fabrication, Dyno testing, Automotive engineering, Gintani builds, Supercharged cars, Turbocharged enhancements, Bespoke tuning projects, Gintani shop vlogs, High-performance car builds"
    },
    {
        "title": "Archie Hamilton Racing",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2CMXqVmLsmHU4bsaA8Eu0g",
        "keywords": "Racing vlogs, Motorsport insights, Archie Hamilton drives, Car racing events, Racing driver tips, Supercar experiences, Behind-the-scenes racing, Track day vlogs, Racing car reviews, Motorsport lifestyle, Personal car collection, Racing challenges, Endurance racing insights, Motorsport interviews, Race day preparations"
    },
    {
        "title": "Marchettino",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCBzfdgfIAANfgP3xyhVaEfQ",
        "keywords": "Supercar experiences, Marchettino reviews, Exotic car test drives, Supercar sound battles, Italian car reviews, High-speed test drives, Automotive events coverage, Car comparison reviews, Auto industry interviews, Car modifications vlogs, Exclusive car previews, Supercar lifestyle, Marchettino's car adventures, Performance car reviews, Luxury car experiences"
    },
    {
        "title": "Alex Choi",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCo00rI10S3Wpk4hVkL5IDTg",
        "keywords": "Supercar vlogs, Alex Choi adventures, Exotic car mods, Hypercar experiences, LA car culture, Supercar rallies, Custom car builds, Unorthodox car modifications, Street racing, Alex Choi car collection, Vlogging with supercars, Car meets in LA, Luxury car lifestyle, Automotive technology reviews, High adrenaline car vlogs"
    },
    {
        "title": "Mark McCann",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCZzQ9gNE0vjjlZVHn95QRuQ",
        "keywords": "Car vlogs, Personal car journeys, Car maintenance tips, Mark McCann drives, Auto detailing vlogs, Car ownership experiences, Practical car reviews, Automotive storytelling, Car travel vlogs, Driving tips and tricks, Everyday car adventures, Family car reviews, Car purchase advice, Hands-on car reviews, Road trip stories"
    },
    {
        "title": "StanceWorks",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCDBaiG0BtHluun67BgXgPRg",
        "keywords": "Car culture vlogs, Stanced car showcases, Car build projects, Custom car modifications, StanceWorks garage, Lowered cars reviews, Automotive photography, Car community events, Classic car restorations, DIY car modifications, StanceWorks features, Exclusive car shoots, Modified car reviews, Custom car build series, Stance car culture"
    },
    {
        "title": "throtl",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCCwfRj2zwwmPfphv4Hh9weQ",
        "keywords": "Car build projects, DIY car modifications, Throtl car challenges, Tuner car builds, Automotive marketplace, Car restoration projects, Car part reviews, Turbocharged build projects, Throtl vlogs, Car tuning tutorials, Auto swap meets, Modified car reviews, Car build-offs, Automotive DIY guides, Car tuning marketplace"
    },
    {
        "title": "Hagerty",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCLgEVx4mzk3T3mzgbKG54Eg",
        "keywords": "Classic car reviews, Car restoration series, Hagerty valuation tools, Collector car insights, Vintage car stories, Classic car buyer's guides, Historic car documentaries, Barn find hunter series, Automotive history lessons, Car auction insights, Vintage motorcycle reviews, Classic car maintenance, Collector car market trends, Iconic car reviews, Automotive heritage stories"
    },
    {
        "title": "Savage Garage",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCjLVHOL7Ez9LnaNU5lUGDWg",
        "keywords": "Supercar adventures, Savage Garage rallies, Hypercar reviews, Supercar lifestyle, Luxury car collection, Road trip vlogs, Car prank series, Savage Garage events, Exclusive car meet-ups, High-speed car adventures, Car modification series, Savage Garage crew, Car collection tours, Luxury car reviews, Automotive luxury lifestyle"
    },
    {
        "title": "Woyshnis Media",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCk55DOnuAgOiFnBj-0XXwGQ",
        "keywords": "Automotive cinematography, Car shoot tutorials, Cinematic car reviews, Car photography tips, Woyshnis Media projects, Automotive visual art, Car cinematic vlogs, High-quality car shoots, Car cinematography techniques, Visual car storytelling, Drone car shots, Car videography insights, Cinematic car features, Automotive filming techniques, Car photography tutorials"
    },
    {
        "title": "Ideal Media",
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC6XuRyMV0Kk0qspigsVOGNw",
        "keywords": "Car buying advice, Ideal car builds, Automotive history, Car comparison reviews, Ideal Media lists, Car market insights, DIY car modifications, Car investment tips, Ideal car setups, Automotive trends analysis, Car maintenance tips, Ideal Media guides, Performance car reviews, Car culture insights, Ideal car flips"
    }
]

for channel in channels:
  channel['prompt_video'] = f"Please summarize in 3 paragraphs, for a blog post, with a playfully sarcastic and witty tone, this Youtube video transcript for a youtube channel in the automobile genre for a blog post as a loyal fan. Utilize the following keywords for SEO: {channel['keywords']}.  Assume you are writing for a familiar audience.  Don't use 'he', 'I', 'we' or 'you', refer to the channel as {channel['title']} mostly.  You are not {channel['title']}.  Don't mention sponsors of the video. "
  channel['prompt_comments'] = f"Please summarize these comments for a youtube video by {channel['title']}.  Point out anything that might be of interest that you would have to watch the video to know.  Analyze what the viewers are thinking in as many bullet points are necessary.  Format the response for a blog post.  Do not sound like a robot or AI."
  channel['active'] = False
  channel['pending'] = True
  channel['authority'] = 1
  channel['owner'] = "wheelcircuit"
  channel['platform_id'] = platforms.getPlatformIdByTitle('Youtube')['_id']
  channel['createdAt'] = datetime.utcnow()
  sources.createNewSource(channel)



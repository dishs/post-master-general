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
    "title": "Ducky 3D",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCuNhGhbemBkdflZ1FGJ0lUQ",
    "keywords": "3d art, 3d design, blender, blender 3d, blender 3d modeling",
    "channel_id": "UCuNhGhbemBkdflZ1FGJ0lUQ",
    "thumbnail": "https://yt3.googleusercontent.com/GDFo9QnOEGgdZgZDigkzViI5dvGfD60c-wLSpVrpDfcooQDwLm1axE0UoZPmqTKYVOCXXCwL=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@TheDucky3D"
  },
  {
    "title": "Blender Guru",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCOKHwx1VCdgnxwbjyb9Iu1g",
    "keywords": "blender, 3d modeling, 3d animation, 3d rendering, blender tutorial",
    "channel_id": "UCOKHwx1VCdgnxwbjyb9Iu1g",
    "thumbnail": "https://yt3.googleusercontent.com/ewXcoWsc-CNvalYafQyR6X-f2BOg5t99m9oLH9m2Kf96dx7KbLQGKzBEPt-NYtIR0DVa0hM2yA=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@BlenderGuru"
  },
  {
    "title": "Derek Elliott",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCk7IufzS4r8v76NeWR6A3dg",
    "keywords": "blender tutorial, 3d design, product rendering, 3d animation, modeling tips",
    "channel_id": "UCk7IufzS4r8v76NeWR6A3dg",
    "thumbnail": "https://yt3.googleusercontent.com/aOrCGs6x-5K0ZEEvzDtaJmOXKcO4zAOnra5waBLJ9QYzCe6eA5B6LU4Lza7Tzy77mUYZAMTOxQ=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@DerekElliott"
  },
  {
    "title": "Adobe Substance 3D",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC-toy9WMImypmLAiU9h_SzQ",
    "keywords": "substance 3d, texturing, 3d design, 3d materials, adobe",
    "channel_id": "UC-toy9WMImypmLAiU9h_SzQ",
    "thumbnail": "https://yt3.googleusercontent.com/4SlDm0Ia58qgLmYZLb5NRtR-lbXj4KkeUn9uoZTVCvJB32uOV5olnKsUcwnHmFNsD7Rk08ktog=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@Substance3D"
  },
  {
    "title": "Fattu Tutorials",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC6SWCKmOGEUp82OdTV9fQkw",
    "keywords": "photoshop tutorials, graphic design, photo editing, text effects, software tips",
    "channel_id": "UC6SWCKmOGEUp82OdTV9fQkw",
    "thumbnail": "https://yt3.googleusercontent.com/ytc/AIdro_n8zQdU-UMhsGHiJN90gMLre2ulFaAIRZyohN99_VLjKA=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@FattuTutorials"
  },
  {
    "title": "The CG Essentials",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCqiJI3COVDqxJnJoVkCiEUg",
    "keywords": "blender, 3d modeling, 3d rendering, tutorials, cg tips",
    "channel_id": "UCqiJI3COVDqxJnJoVkCiEUg",
    "thumbnail": "https://yt3.googleusercontent.com/ytc/AIdro_mSYj-iPmVFIrVE4j2zpiOhU91oypL75oyVKBnRuJKrFvA=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@TheCGEssentials"
  },
  {
    "title": "3D Blending Hub",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UClF7yQhsR5wHG1t70gIvdCg",
    "keywords": "blender, 3d tutorials, 3d rendering, modeling tips, animation",
    "channel_id": "UClF7yQhsR5wHG1t70gIvdCg",
    "thumbnail": "https://yt3.googleusercontent.com/bkEjpvl-2pW34PSg4CDPQf4_bFBhSHAZDUNYGUTBJpeB9WWzSOYGlMA0t3jSv8iAZV4J4JT4_A=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@3DBlendingHub"
  },
  {
    "title": "Christopher 3D",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCu_PgLQjx8GI_Soe39PpC5Q",
    "keywords": "blender tutorial, modeling, animation, 3d design, 3d rendering",
    "channel_id": "UCu_PgLQjx8GI_Soe39PpC5Q",
    "thumbnail": "https://yt3.googleusercontent.com/ytc/AIdro_lpW_KTjshD22SCGnbizRyuzCfSzb0FQqslsb9yvxldzqs=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@Christopher3D"
  },
  {
    "title": "3D Megaverse",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCyTuaTlOVq6k2L1gwcol9Kw",
    "keywords": "3d art, blender, vfx, 3d modeling, 3d tutorials",
    "channel_id": "UCyTuaTlOVq6k2L1gwcol9Kw",
    "thumbnail": "https://yt3.googleusercontent.com/c1f3k88Rchcs03mSKGDw2DuhK9PDj1moHkd3pSTrgOyBVnZXf0ZjeNQyK9DDqVKA-xBHxt0xa1c=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@3dmegaverseJohn"
  },
  {
    "title": "Bad Normals",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCvigl2g67gl18hJgFex-3zg",
    "keywords": "blender, 3d modeling, 3d animation, game assets, bad normals",
    "channel_id": "UCvigl2g67gl18hJgFex-3zg",
    "thumbnail": "https://yt3.googleusercontent.com/ytc/AIdro_mfj_fhqZwdt79zwOWhGGCDv0noP8IasvVfpCE5Ncdp6k8=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@BadNormals"
  },
  {
    "title": "Cleverpoly",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCAWSyjNRkg-QUSV6UY5-ZyA",
    "keywords": "3d tutorials, blender workflow, texturing, clever tips, 3d modeling",
    "channel_id": "UCAWSyjNRkg-QUSV6UY5-ZyA",
    "thumbnail": "https://yt3.googleusercontent.com/81hE48VedvtsBuEQgT6l7FzRamnCK6pkq1lWE-m9LQ7HjmyMfLxbsshxK8VPWmyDP7jaW5jckA=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@cleverpoly"
  },
  {
    "title": "ProductionCrate",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCtl5VdRFeerk0-xAGBpMbdw",
    "keywords": "vfx, 3d animation, filmmaking, special effects, production crate",
    "channel_id": "UCtl5VdRFeerk0-xAGBpMbdw",
    "thumbnail": "https://yt3.googleusercontent.com/dQuSfax1B8LoQNlERB1HB2UNRCv8z-tnQVyCdaVTb9mu3tzOtnYClQ5GsOqNLb0TFxkPM2n4=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@ProductionCrate"
  },
  {
    "title": "Will Gibbons",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCOeW85utmZzFdBULeITo2mw",
    "keywords": "3d rendering, product design, keyshot, blender, tutorial",
    "channel_id": "UCOeW85utmZzFdBULeITo2mw",
    "thumbnail": "https://yt3.googleusercontent.com/G9ArEk1uRxslBaUqD_0NCmJ_yYeNDm-bgAQ6M7MIwjh_CPueu__4zAZcZ-WrwFeFpzGrdmYgNA=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@willgibbons"
  },
  {
    "title": "Mafriend",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCwEk1hO1KzzakGZ29va5uiQ",
    "keywords": "3d art, blender, 3d visuals, animations, modeling",
    "channel_id": "UCwEk1hO1KzzakGZ29va5uiQ",
    "thumbnail": "https://yt3.googleusercontent.com/0PCJjpOrb7y5nYuw_3sZNIAL7H2xLWhzJ8XT0WVGLqh9gTj4Q-SqVi_a-bxQ7cwn9WAmggSe0Q=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@mafriend"
  },
  {
    "title": "jhill",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCV4JXShy1U1PeMa3KdzeonQ",
    "keywords": "3d workflows, blender tutorial, environment art, texturing, animations",
    "channel_id": "UCV4JXShy1U1PeMa3KdzeonQ",
    "thumbnail": "https://yt3.googleusercontent.com/C5KNYUXf7pNS0FJM6kQKDURmIRZGxvE5ESALT_pQAG6WMaNBe0huqlosy-k_6-phKbBD0-27LhI=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@jhill"
  },
  {
    "title": "GRMNT",
    "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCUU5v3JscgO2oKAw0JSicag",
    "keywords": "3d creative, blender tips, garment simulation, cg fashion, rendering",
    "channel_id": "UCUU5v3JscgO2oKAw0JSicag",
    "thumbnail": "https://yt3.googleusercontent.com/z24HDFvESzztF4OMMqFaHr_w0RTkUYjBI_XWbmoU9Mxi6S3eQt3eMkB7qxTKDHfXW16lz0bzc6s=s160-c-k-c0x00ffffff-no-rj",
    "custom_url": "@GRMNT"
  }
]



for channel in channels:
  channel['prompt_video'] = f"Please summarize in 3 paragraphs, for a blog post, with a playfully sarcastic and witty tone, this Youtube video transcript for a youtube channel in the 3d art & design genre for a blog post as a loyal fan. Utilize the following keywords for SEO: {channel['keywords']}.  Assume you are writing for a familiar audience.  Don't use 'he', 'I', 'we' or 'you', refer to the channel as {channel['title']} mostly.  You are not {channel['title']}.  Don't mention sponsors of the video. "
  channel['prompt_comments'] = f"Please summarize these comments for a youtube video by {channel['title']} in the 3d art & design genre.  Point out anything that might be of interest that you would have to watch the video to know.  Analyze what the viewers are thinking in as many bullet points are necessary.  Format the response for a blog post.  Do not sound like a robot or AI."
  channel['active'] = True
  channel['pending'] = False
  channel['authority'] = 1
  channel['owner'] = "bevelfish"
  channel['platform_id'] = platforms.getPlatformIdByTitle('Youtube')['_id']
  channel['createdAt'] = datetime.utcnow()
  sources.createNewSource(channel)



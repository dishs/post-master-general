import common.dbconn as dbconn

class PlatformManager:

    def get_platform_id_by_title(self, title):
        try:
            return dbconn.dbPlatforms.find_one({'title': title})
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

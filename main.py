import sites  # Importing all site-specific modules
import celery_app  # Ensures Celery is initialized properly

def main():
    site_modules = {
        "wheelcircuit": sites.wheelcircuit,
        "dunkmania": sites.dunkmania,
        "slappytrillmore": sites.slappytrillmore,
    }

    for site_name, site_module in site_modules.items():
        try:
            print(f"====================================================================================================")
            print(f"                               Initializing {site_name}")
            print(f"====================================================================================================")
            processor = site_module.get_processor()
            if processor.enabled:
                print(f"Processing {site_name}...")
                process_site(processor)
            else:
                print(f"Site is disabled in config.")
        except AttributeError as e:
            print(f"Error processing {site_name}: Missing required attribute. {e}")
        except Exception as e:
            print(f"Unexpected error occurred while processing {site_name}: {e}")

def process_site(processor):
    try:
        processor.fetch_and_process_feeds()
        processor.update_and_publish_site()
        # Add any additional processing required per site
    except ConnectionError as e:
        print(f"Network error while processing videos: {e}")
    except Exception as e:
        print(f"Unexpected error during site processing: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical error: {e}")

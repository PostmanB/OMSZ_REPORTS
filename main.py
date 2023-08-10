import os
import webbrowser
from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor

# Replace with your own Imgur API credentials
client_id = '36502433b94e9fd'
client_secret = '786354b521fc67fdd5edd2b8f72da4dd729463b7'

# Initialize the Imgur client
client = ImgurClient(client_id, client_secret)

# Path to the folder containing images
image_folder = r'C:\SeeMTA\screenshots'

# List all image files in the folder
image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if
               filename.lower().endswith(('.jpg', '.png', '.gif'))]


# Upload and open links in parallel
def upload_and_open_link(path):
    try:
        # Upload the image
        upload = client.upload_from_path(path, anon=True)
        image_url = upload['link']

        # Open the image link in a new Chrome tab
        webbrowser.open_new_tab(image_url)

        print(f"Image uploaded and link opened: {image_url}")
    except Exception as e:
        print(f"Error uploading image '{path}': {e}")
    finally:
        # Close any open browser tabs or resources here if needed
        pass


# Use a thread pool to process images in parallel
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(upload_and_open_link, image_files)

# Explicitly shut down the thread pool
executor.shutdown()
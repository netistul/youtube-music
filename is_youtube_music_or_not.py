import requests
import json

# Global variable for UI_KEY (replace with your actual YouTube Data API v3)
UI_KEY = "your YouTube Data API v3"

# Options dictionary to mimic $options in PHP
options = {'music': True}  # Or set to False depending on your requirements

def get_json_func(raw_data, music=False):
    headers = {
        'Content-Type': 'application/json',
        'Accept-Language': 'en'
    }
    
    if music:
        headers['Referer'] = 'https://music.youtube.com'
    
    url = f"https://{ 'music' if music else 'www' }.youtube.com/youtubei/v1/player?key={UI_KEY}"
    
    # Print the full URL for debugging
    print(f"Full URL: {url}")
    
    response = requests.post(url, headers=headers, json=raw_data)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return None

# Usage example
video_id = "4oqRXI1Ck7k"  # Replace with any youtube video ID
CLIENT_VERSION = '1.9999099'  # Replace with your actual client version / you can let it like this

raw_data = {
    'videoId': video_id,
    'context': {
        'client': {
            'clientName': 'WEB_EMBEDDED_PLAYER',
            'clientVersion': CLIENT_VERSION
        }
    }
}

# Make the API call
if options['music']:
    raw_data['context']['client']['clientName'] = 'WEB_REMIX'
    result = get_json_func(raw_data, music=True)
else:
    result = get_json_func(raw_data, music=False)
    print(f"Entire YouTube API Response: {json.dumps(result, indent=4)}")

# Check music availability
    print(f"Playability Status: {result.get('playabilityStatus', {}).get('status', 'N/A')}")
if result:
    music_available = result.get('playabilityStatus', {}).get('status', '') == 'OK'
    print(f"Playability Status: {result.get('playabilityStatus', {}).get('status', 'N/A')}")
    print(f"Music available: {music_available}")
else:
    print("Failed to get JSON.")

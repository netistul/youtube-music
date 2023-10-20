# YouTube Music Link Detector 🎵🦉

A Python script for interfacing with the YouTube API to determine if a YouTube link is part of YouTube Music. The script allows you to check if a YouTube link is music-related or not.

## 📋 Prerequisites

- Python 3.x
- `requests` library

You'll also need a YouTube Data API v3 key. Obtain it from [here](https://developers.google.com/youtube/registering_an_application).

## 🛠️ Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/yourrepository.git](https://github.com/netistul/youtube-music.git
    ```
   
2. **Install Required Packages**
    ```bash
    pip install requests
    ```

3. **Setup API Key**

    Open the script and replace the `UI_KEY` variable with your actual YouTube Data API v3 key.

## 🚀 Usage

1. **Set Video ID**

    Replace the `video_id` variable in the script with the YouTube video ID you wish to investigate.

2. **Run the Script**
    ```bash
    python your_script_name.py
    ```

### 📄 Example Output
Music available: False (this means that the YouTube link is not music-related)

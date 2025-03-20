# 🫠 **AutoPost-Discord**  
### 📰 **Automatically Post Blogspot & YouTube Content to Discord**  

A powerful **Python automation bot** that monitors your **Blogspot** and **YouTube channel** and **auto-posts** new content to your **Discord server** with rich embeds & thumbnails.  

> [See The Demo](img/Demo.png) 

## **✨ Features**  
✔ **Automated Blogspot Post Monitoring** → Fetches and posts **new** Blogspot articles.  
✔ **Automated YouTube Video Monitoring** → Posts **new** YouTube videos as soon as they’re published.  
✔ **No Duplicate Posts** → Ensures each post/video is sent **only once**.  
✔ **Runs Automatically at Midnight (12:00 AM UTC)** via **GitHub Actions**.  
✔ **Uses GitHub Secrets** for secure API key storage.  
✔ **Rich Discord Embeds** → Posts content with **title, link, and thumbnail**.  
✔ **Lightweight & Fast** → Efficient JSON-based storage (`posted.json`) prevents duplicate posts.  


## **📜 Requirements**  
- **Python 3.8+**  
- **GitHub Actions** (for automated execution)  
- **A Discord Webhook URL**  
- **YouTube API Key** (to fetch video details)  
- **YouTube Channel ID** (of the channel to monitor)  
- **Blogspot RSS Feed URL** (for monitoring new blog posts)  


## **🔧 Installation & Setup**  

### **1️⃣ Fork & Clone the Repository**  
First, **fork** this repository and **clone it** to your local machine:  

```sh
git clone https://github.com/nayandas69/AutoPost-Discord.git
cd AutoPost-Discord
```


### **2️⃣ Install Dependencies**  
Install the required Python packages:  

```sh
pip install -r requirements.txt
```


### **3️⃣ Configure GitHub Secrets**  
To keep your credentials **secure**, **add the following secrets** to your GitHub repository:

#### **Steps to Add GitHub Secrets**  
1. Go to your **GitHub repository**.  
2. Navigate to **Settings → Secrets and variables → Actions**.  
3. Click **"New repository secret"** and add the following **secrets**:

| Secret Name          | Value (Example) |
|----------------------|-------------------------------------------------------------|
| **DISCORD_WEBHOOK**  | `https://discord.com/api/webhooks/XXXXXX/YYYYYY` |
| **BLOGSPOT_URL**     | `https://yourblog.blogspot.com/feeds/posts/default?alt=rss` |
| **YOUTUBE_API_KEY**  | `YOUR_YOUTUBE_API_KEY_HERE` |
| **YOUTUBE_CHANNEL_ID** | `UCXXXXXXXXXXXXXXX` |

or [Read The Doc](docs/CONFIGURATION.md)


### **4️⃣ Run the Bot Manually**  
To test if everything is working, run:  

```sh
python main.py
```


### **5️⃣ Enable GitHub Actions for Automation**  
The script **runs automatically every day at midnight (12:00 AM UTC)** via **GitHub Actions**.

#### **Steps to Enable GitHub Actions**  
1. **Push the code** to your GitHub repository.  
2. Go to the **Actions** tab in your repository.  
3. **Enable GitHub Actions** (if not enabled).  
4. The bot will now **run daily at 12:00 AM UTC** and post new content.  


## **📜 How It Works**  
### 🔹 **1. `main.py` (Entry Point)**
- Calls `check_blogspot()` to fetch **Blogspot posts**.  
- Calls `check_youtube()` to fetch **YouTube videos**.  
- Posts them to **Discord**, ensuring no duplicates.  

### 🔹 **2. `blogspot.py` (Fetches Blogspot Posts)**
- Uses **RSS Feed** to check for **new** Blogspot posts.  
- Extracts the **title, link, and thumbnail**.  
- Checks `posted.json` to **prevent duplicate posts**.  
- Sends the **new post** to **Discord**.  

### 🔹 **3. `youtube.py` (Fetches YouTube Videos)**
- Uses the **YouTube API** to fetch the **latest videos**.  
- Extracts the **title, video URL, and thumbnail**.  
- Checks `posted.json` to **prevent duplicate posts**.  
- Sends the **new video** to **Discord**.  

### 🔹 **4. `discord.py` (Sends Messages to Discord)**
- Uses a **Discord Webhook** to send messages as **rich embeds**.  
- Includes **title, link, and thumbnail**.  

### 🔹 **5. `storage.py` (Prevents Duplicate Posts)**
- Loads and updates `posted.json`, which tracks **already posted** content.  
- Ensures each post/video is **only sent once**.  

### 🔹 **6. `github_secrets.py` (Fetches GitHub Secrets)**
- Retrieves **API keys and webhook URLs** from GitHub Secrets.  

### 🔹 **7. `.github/workflows/ci.yml` (GitHub Actions Automation)**
- **Runs the bot automatically** at **12:00 AM UTC daily**.  
- Commits & pushes updates to `posted.json` to keep track of **posted content**.  


## **👌 Automating with GitHub Actions**  

The bot runs **automatically** every day at **12:00 AM UTC** using **GitHub Actions**.  

> HOW SET CRON [READ THIS](docs/SCHEDULE_GUIDE.md)

**Workflow Configuration (`.github/workflows/ci.yml`)**


## **🛠 Troubleshooting**  
### **1️⃣ Bot is Not Posting to Discord**  
✅ Ensure your **Discord Webhook URL** is correct.  
✅ Check if your **GitHub Secrets** are set properly.  
✅ Manually run the script:  
```sh
python main.py
```
✅ Check the **GitHub Actions logs** for errors.  

### **2️⃣ YouTube Videos Are Not Posting**  
✅ Ensure your **YouTube API Key** is correct.  
✅ Check if your **YouTube Channel ID** is correct.  
✅ Make sure your **channel is public**.  

### **3️⃣ Blogspot Posts Are Not Showing**  
✅ Check if your **Blogspot RSS URL** is correct.  
✅ Make sure your **Blog is public**.  
✅ Run the script manually and check for errors.  


## **📜 License**  
This project is licensed under the **MIT License**.  


## **📬 Support & Feedback**  
Facing issues? **Open an issue** on GitHub.  


💙 **Enjoy this automated posting bot!** 
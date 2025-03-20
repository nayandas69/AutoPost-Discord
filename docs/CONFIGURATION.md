# **🔑 How to Get YouTube API Key**
Since you have YouTube channels on your Google account, make sure you select the correct one.

### **Step 1: Create a Google Cloud Project**
1. Go to **[Google Cloud Console](https://console.cloud.google.com/)**.
2. Sign in with your **Google Account**.
3. Click on the **Select a project** dropdown at the top.
4. Click **New Project** → Give it a name (e.g., `YouTube AutoPost`).
5. Click **Create**.


### **Step 2: Enable YouTube Data API v3**
1. In **Google Cloud Console**, go to **APIs & Services** → **Library**.
2. Search for **YouTube Data API v3**.
3. Click **Enable**.


### **Step 3: Create an API Key**
1. In **Google Cloud Console**, go to **APIs & Services** → **Credentials**.
2. Click **Create Credentials** → Select **API Key**.
3. **Copy** the API key (you’ll need this later).
4. (Optional) Click **Restrict Key**, then:
   - Under **Application Restrictions**, choose **None** or **IP Address**.
   - Under **API Restrictions**, select **YouTube Data API v3**.
   - Click **Save**.

✅ **You now have your YouTube API Key**. Add it to **GitHub Secrets** as `YOUTUBE_API_KEY`.


# **📺 How to Get Your YouTube Channel ID**
Since you have **two YouTube channels**, follow these steps carefully:

1. Open **[YouTube Studio](https://studio.youtube.com/)**.
2. **Switch to the correct channel** (top-right corner, click on your profile icon).
3. Click **Settings** (left sidebar).
4. Go to **Channel** → **Advanced Settings**.
5. Scroll down to **YouTube Channel ID**.
6. Copy the **Channel ID** (a long string of letters and numbers).

✅ **You now have your YouTube Channel ID**. Add it to **GitHub Secrets** as `YOUTUBE_CHANNEL_ID`.

---

# **📰 How to Get Your Blogspot RSS Feed URL**
Your Blogspot **RSS feed URL** is:
```
https://your-blog-name.blogspot.com/feeds/posts/default?alt=rss
```
✅ **Add this URL** to **GitHub Secrets** as `BLOGSPOT_URL`.


# **💬 How to Create a Discord Webhook**
1. Open **Discord** and go to your **server**.
2. Click the **settings gear** next to the channel you want to post in.
3. Go to **Integrations** → Click **Create Webhook**.
4. Give it a **name** (e.g., `AutoPost Bot`).
5. Copy the **Webhook URL**.

✅ **Add this Webhook URL** to **GitHub Secrets** as `DISCORD_WEBHOOK`.


# **🔒 How to Add Secrets to GitHub**
Once you have collected all the required **secrets**, add them to **GitHub Secrets**:

### **Steps:**
1. **Go to your GitHub repository**.
2. Navigate to **`Settings` → `Secrets and variables` → `Actions`**.
3. Click **"New repository secret"**.
4. Add the following secrets one by one:

| Secret Name           | Value (Paste This) |
|----------------------|----------------|
| `DISCORD_WEBHOOK`   | Your **Discord Webhook URL** |
| `BLOGSPOT_URL`      | Your **Blogspot RSS Feed URL** |
| `YOUTUBE_API_KEY`   | Your **YouTube API Key** |
| `YOUTUBE_CHANNEL_ID`| Your **YouTube Channel ID** |

✅ **Now your GitHub Secrets are correctly set up!**

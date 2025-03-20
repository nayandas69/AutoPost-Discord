# **⏰ Schedule Guide for GitHub Actions**  

This guide explains how to schedule your GitHub Actions workflows using **cron expressions**.  

## **🔹 Understanding Cron Schedule (`cron: '0 0 * * *'`)**  
A cron expression consists of **five fields**, each representing a unit of time:  

```
# ┌───────── minute (0 - 59)
# │ ┌─────── hour (0 - 23)
# │ │ ┌───── day of the month (1 - 31)
# │ │ │ ┌─── month (1 - 12)
# │ │ │ │ ┌─ day of the week (0 - 6) (Sunday = 0 or 7)
# │ │ │ │ │
# 0 0 * * *  → Runs every day at 12:00 AM UTC
```

## **🔹 Example Cron Expressions**  
Here are some common scheduling examples:  

| Expression       | Meaning |
|-----------------|---------|
| `0 0 * * *`     | Every day at **12:00 AM (UTC)** |
| `30 18 * * *`   | Every day at **6:30 PM (UTC)** |
| `0 */6 * * *`   | Every **6 hours** |
| `0 12 * * 1`    | Every **Monday at 12:00 PM (UTC)** |
| `0 9 1 * *`     | Every **1st of the month at 9:00 AM (UTC)** |
| `*/15 * * * *`  | Every **15 minutes** |

## **🔹 How to Customize the Schedule**  
To adjust your workflow timing, modify the `schedule` section in your **.github/workflows/ci.yml**:  

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Runs every day at 12:00 AM UTC
```

Replace `'0 0 * * *'` with your preferred **cron expression** based on the table above.  

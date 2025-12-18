# Deployment Guide

You can deploy this application as a Web App in two main ways:

## Option 1: Streamlit Community Cloud (Easiest & Free)
This method hosts the app on the internet securely.

1.  **Create a GitHub Account** (if you don't have one).
2.  **Upload this folder** to a new GitHub Repository.
3.  Go to [share.streamlit.io](https://share.streamlit.io/).
4.  Log in and click "New App".
5.  Select your GitHub Repository and the file `app.py`.
6.  Click **Deploy**.

*Pros*: Free, accessible from anywhere via URL.
*Cons*: Data is processed on cloud (though Streamlit is secure, ensure it meets policy).

## Option 2: Docker (Local or Private Server)
If you want to run it on a secure private server or locally without installing Python manually:

1.  Install **Docker Desktop**.
2.  Open Terminal/Command Prompt in this folder.
3.  Run:
    ```bash
    docker build -t isp-letter-gen .
    docker run -p 8501:8501 isp-letter-gen
    ```
4.  Open `http://localhost:8501` in your browser.

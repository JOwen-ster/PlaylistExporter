# PlaylistExporter

**PlaylistExporter** is a web application that simplifies the process of transferring your favorite Spotify playlists to YouTube. Whether you’re switching platforms or just want to enjoy your music with video, this app takes care of the heavy lifting. By connecting to both Spotify and YouTube through secure logins, it fetches your playlists, matches songs with their YouTube counterparts, and creates a new YouTube playlist.

---

## 🛠️ Built With

- **Backend:** Python and Flask handle the application’s server-side logic and API interactions.
- **Frontend:** The interface is built using Svelte for dynamic UI updates and styled with Tailwind CSS for a sleek, responsive design.
- **APIs:** The Spotify API (via the Spotipy library) fetches playlist data, and the YouTube Data API is used to search and manage videos on YouTube along with create a playlist and add to it.
- **Authentication:** OAuth 2.0 ensures a secure and seamless login experience for both platforms.

---

## 🚀 How It Works

The app is designed to make the playlist conversion process as straightforward as possible. Here's the flow:

1. **Login and Authorization**  
   When users visit the app, they’re prompted to log in to both their Spotify and YouTube accounts. The app uses OAuth 2.0 to securely authenticate users and obtain the necessary permissions to access their playlists and create new ones.

2. **Fetch Spotify Playlists**  
   Once authenticated, the app retrieves a list of all the user’s public Spotify playlists. These playlists are displayed on the screen, allowing the user to select one for conversion.

3. **Playlist Conversion**  
   After selecting a Spotify playlist, the app extracts the names and artists of the songs within it. It then searches YouTube for the corresponding videos. When a match is found, the app compiles these videos into a new playlist on the user’s YouTube account.

4. **Limitations**
   Each user must choose a Spotify playlist with no more than 50 songs due to Youtube's API rate limit when creating and inserting to playlists.

---

## How to Run the Project

1. **Set Up Environment Variables**  
   - Obtain YouTube credentials (Client ID and Client Secret) from the [Google Cloud Console](https://console.cloud.google.com/).
   - Generate a Google API Key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Obtain Spotify Developer credentials (Client ID and Client Secret) from the [Spotify Developer Portal](https://developer.spotify.com/dashboard/).    
   - Create a `.env` file in the root directory using the format in `env.example`:
     ```env
     clientID="🩷"
     clientSecret="💜"
     GOOGLE_API_KEY="💛"

     SPOTIFY_CLIENT_ID="💚"
     SPOTIFY_CLIENT_SECRET="🧡"
     ```

2. **Install Dependencies**  
   - Ensure Python v3 is installed on your system.  
   - Open a terminal, navigate to the `backend/api` folder by running:  
     ```bash
     cd backend/api
     ```  
   - Install the required Python dependencies by running:  
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**  
   Open **two terminals**:  

   - **Terminal 1:**  
     - From the root directory of the project, navigate to the `backend/api` folder:  
       ```bash
       cd backend/api
       ```  
     - Start the Flask server:  
       - On Mac:  
         ```bash
         python3 flask-server.py
         ```  
       - On Windows:  
         ```bash
         python flask-server.py
         ```

   - **Terminal 2:**  
     - From the root directory of the project, navigate to the `frontend` folder:  
       ```bash
       cd frontend
       ```  
     - Install the required Node.js dependencies by running:  
       ```bash
       npm install
       ```  
     - Start the Svelte development server:  
       ```bash
       npm run dev
       ```

4. **Use the Application**  
   - Open a browser and navigate to the provided URL (usually `http://localhost:3000`).  
   - Click **Login to Spotify** to authenticate.  
   - Select a playlist and click **Submit Playlist**.  
   - Click **Login to YouTube**, and you'll be redirected to a success page.  
   - Check your YouTube account for the exported playlist.

**Note:** Both terminals must remain running simultaneously for the application to work.


---

## 🖼️ Screenshots
<img width="1470" alt="Screenshot 2024-12-10 at 7 51 38 PM" src="https://github.com/user-attachments/assets/dd5f18dc-ade0-4e4d-9a6e-060a789d6a4c">
<img width="1470" alt="Screenshot 2024-12-10 at 7 52 18 PM" src="https://github.com/user-attachments/assets/dcd8c846-91aa-4ed8-ad16-cd4d83150e5c">
<img width="1470" alt="Screenshot 2024-12-10 at 7 52 38 PM" src="https://github.com/user-attachments/assets/c3323423-31c2-46c1-b89a-cbb19880e3d7">
<img width="1470" alt="Screenshot 2024-12-10 at 7 53 01 PM" src="https://github.com/user-attachments/assets/d33a7cb6-1ff0-44ad-b619-642883d6963f">
<img width="1470" alt="Screenshot 2024-12-10 at 7 53 55 PM" src="https://github.com/user-attachments/assets/e62cda6f-64c1-457e-a5d2-1b2f5ba07d07">
<img width="974" alt="Screenshot 2024-12-10 at 7 54 37 PM" src="https://github.com/user-attachments/assets/9aeb9053-d2ee-433d-8ef4-dace9b95b20e">

---

Developed by [Sama Ahmed](https://github.com/26samaahmed), [Boushra Bettir](https://github.com/boushrabettir), [James Owen Sterling](https://github.com/JOwen-ster), [Patrick Smith](https://github.com/thisguyblink) ✨

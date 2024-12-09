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
   To ensure smooth operation and compliance with API constraints, there is a cap on the number of songs that can be converted in a single session. This ensures that the app remains efficient even for larger playlists.

---

## 🖼️ Screenshots

*(TBD)*

---

## How to Run the Project

*(TBD)*

---

## Key Features

- **Easy Playlist Transfer:** Move your music effortlessly between Spotify and YouTube with minimal input.
- **Accurate Song Matching:** Leverages song titles and artist names to find the closest matches on YouTube.
- **Dynamic Playlist Creation:** Automatically generates and saves a YouTube playlist with the selected songs.
- **Responsive Design:** Enjoy a user-friendly interface on both desktop and mobile devices.

---

Developed by [Sama Ahmed](https://github.com/26samaahmed), [Boushra Bettir](https://github.com/boushrabettir), [James Owen Sterling](https://github.com/JOwen-ster), [Patrick Smith](https://github.com/thisguyblink) ✨

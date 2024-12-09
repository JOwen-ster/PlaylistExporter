<script>

</script>

<main class="flex flex-col justify-between h-screen">

  <div>
    <h1 class="text-center text-3xl md:text-6xl mt-8 text-[#1C873E] font-medium">
      Welcome to Playlist Exporter!
    </h1>
    <p class="text-center text-xl md:text-2xl mt-5 text-[#7e7C7C] mb-6">
      Start Converting Your Playlists from Spotify to YouTube
    </p>
    <div class="flex flex-col items-center space-y-4">
      <a href="/auth/spotify" 
         class="md:text-2xl text-center text-white bg-green-500 py-2 px-4 m-5 rounded hover:bg-green-600">
        Login with Spotify
      </a>
      <a href="/auth/youtube" 
         class="md:text-2xl text-center text-white bg-red-500 py-2 px-4 rounded hover:bg-red-600">
        Login with Youtube
      </a>
    </div>
  </div>

  <div class="text-center">
    <p class="md:text-xl text-[#FFAAAA] mb-4">
      Here is a song recommendation while you login!
    </p>
    <iframe 
      class="w-full sm:w-96 h-24 rounded-lg m-auto" 
      src="https://open.spotify.com/embed/track/52dF752HWIsv2CpSuTX3p2?utm_source=generator" 
      frameborder="0" 
      allowfullscreen 
      allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
      loading="lazy" 
      title="Spotify Song Player">
    </iframe>
  </div>
</main>

<style>
  :global(body) {
    background-color: black;
    font-family: "Alegreya Sans", sans-serif;
  }

  a {
    transition: all 0.3s;
  }

  a:hover {
    text-decoration: underline;
  }
</style>
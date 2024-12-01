<svelte:head>
  <title>Playlist Exporter</title>
  <meta name="description" content="Export your Spotify playlists to Youtube">
  <meta name="keywords" content="Spotify, Youtube, Playlist, Export">
  <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,100;0,300;0,400;0,500;0,700;0,800;0,900;1,100;1,300;1,400;1,500;1,700;1,800;1,900&display=swap" rel="stylesheet">

</svelte:head>

<script>

</script>

<main>
  <h1 class="text-center text-6xl mt-8 text-[#1C873E] font-medium ">Welcome to Playlist Exporter!</h1>
  <p class="text-center text-2xl mt-5 text-[#7e7C7C] mb-6">Start Converting Your Playlists from Spotify to YouTube</p>
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
  

  <p class="text-center md:text-xl mt-16 mb-5 text-[#FFAAAA]">
    Here is a song recommendation while you login!
  </p>

  <iframe 
  style="border-radius:12px; display:block; margin:auto;" 
  class="w-full sm:w-96"
  src="https://open.spotify.com/embed/track/52dF752HWIsv2CpSuTX3p2?utm_source=generator" 
  height="100"
  frameBorder="0" 
  allowfullscreen 
  allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
  loading="lazy" 
  title="Spotify Song Player">
</iframe>

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
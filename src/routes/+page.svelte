<svelte:head>
  <title>Playlist Exporter</title>
  <meta name="description" content="Export your Spotify playlists to Youtube">
  <meta name="keywords" content="Spotify, Youtube, Playlist, Export">

</svelte:head>

<script>

</script>

<main>
  <h1 class="text-center text-6xl mt-5 ">Playlist Exporter</h1>
  <p class="text-center text-2xl mt-5">Start Converting Your Playlists here!</p>
  <div class="bg-white opacity-50 w-1/2 h-96 mx-auto mt-5 rounded-lg flex flex-row justify-between p-10 m-auto">
    <div class=" h-full">
      <a href="/auth/spotify" class="text-2xl text-center text-black">Login with Spotify</a>
    </div>

    <div class=" h-full">
      <a href="/auth/youtube" class="text-2xl text-center text-black">Login with Youtube</a>
    </div>

  </div>

  <p class="text-center text-xl mt-16 mb-5">
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
    background: rgb(193,255,215);
    background: linear-gradient(90deg, rgba(193,255,215,1) 40%, rgba(255,171,171,1) 65%);
    font-family: "Antonio", sans-serif;
  }

  a {
    transition: all 0.3s;
  }

  a:hover {
    text-decoration: underline;
  }
</style>
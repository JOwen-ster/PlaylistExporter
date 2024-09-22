<svelte:head>
  <title>Playlist Exporter</title>
  <meta name="description" content="Export your Spotify playlists to Youtube">
  <meta name="keywords" content="Spotify, Youtube, Playlist, Export">

</svelte:head>

<script>

</script>

<main>
  <h1 class="text-center text-6xl mt-5 text-white">Playlist Exporter</h1>
  <p class="text-center text-2xl mt-5 text-white">Start Converting Your Playlists here!</p>
  <div class="bg-white opacity-50 w-1/2 h-96 mx-auto mt-5 rounded-lg flex flex-row justify-between p-10 m-auto">
    <div class=" h-full">
      <a href="/auth/spotify" class="text-2xl text-center text-black">Login with Spotify</a>
    </div>

    <div class=" h-full">
      <a href="/auth/youtube" class="text-2xl text-center text-black">Login with Youtube</a>
    </div>

  </div>

</main>


<style>
  :global(body) {
    background: rgb(193,255,215);
    background: linear-gradient(90deg, rgba(193,255,215,1) 40%, rgba(255,171,171,1) 65%);
    font-family: "Antonio", sans-serif;
  }
</style>
<script>
  import Note from './Note.svelte';

  import { userState } from './stores.svelte.js';
</script>

<div class="btn">
  {#each userState.notes as note, index}
    <Note {note} {index} />
  {/each}
</div>

<style>
  .btn {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;

    height: 50vh;
  }
</style>

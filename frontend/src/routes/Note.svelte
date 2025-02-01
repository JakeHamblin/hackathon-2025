<script>
  import { userState } from './stores.svelte.js';

  let { note, index } = $props();

  let value = $state();

  async function updateNote() {
    userState.notes[index] = value;
  }
</script>

<input bind:value type="text" />
<button onclick={updateNote}>Change note {index} sound</button>
<p>Note: {note}</p>

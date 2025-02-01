<script>
  import { userState } from './stores.svelte.js';

  let { note, index } = $props();

  let value = $state();

  async function updateNote() {
    userState.notes[index].sound = value;

    const res = fetch('/config', {
      method: 'POST',
      body: JSON.stringify(userState),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    const { status } = await res;
  }
</script>

<input bind:value type="text" />
<button onclick={updateNote}>Change note {index} sound</button>

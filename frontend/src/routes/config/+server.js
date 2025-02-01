import { PWD } from '$env/static/private';
import { json } from '@sveltejs/kit';
import { writeFile } from 'fs';

export async function POST({ request }) {
  const conf = await request.json();

  writeFile('./src/lib/config.json', JSON.stringify(conf), (err) => {
    if (err) {
      console.error(err);
      return json({ err }, { status: 500 });
    }
  });

  return json({ body: 'success' }, { status: 201 });
}

import { useEffect, useState } from 'react'
import { createEntry, getEntries } from './services/services'
import type { JournalEntry, NewJournalEntry } from './types/types'

function App() {
  const [entries, setEntries] = useState<JournalEntry[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string>('')
  const [postingEntry, setPostingEntry] = useState<boolean>(false)

  useEffect(() => {
    getEntries()
      .then(setEntries)
      .catch((error: unknown) =>
        setError(error instanceof Error ? error.message : 'Could not load journal entries.'))
      .finally(() => setLoading(false))
  }, [])

  async function submitEntry(data: FormData) {
    setError('')
    setPostingEntry(true)

    try {
      const newEntry: NewJournalEntry = {
        content: String(data.get('content') ?? ''),
      }
      const entry = await createEntry(newEntry)
      setEntries((current) => [entry, ...current])
    } catch (error: unknown) {
      setError(error instanceof Error ? error.message : 'Could not post your entry.')
    } finally {
      setPostingEntry(false)
    }
  }

  return (
    <main className=" min-h-screen">
      <header className="pt-20">
        <h1 className="text-6xl text-center">
          My Journal
        </h1>
      </header>

      <section className="mx-auto my-10 w-1/2 rounded-lg border border-zinc-300 bg-zinc-200 p-3">
        <form className="grid grid-cols-1 gap-4" action={submitEntry}>
          <textarea className="w-full rounded-lg border border-zinc-300 bg-rose-100 p-3 focus:outline-none" id="entry-content" name="content" rows={4} placeholder="What’s on your mind?" required maxLength={5000} />
          <button className="w-24 justify-self-end rounded-lg bg-rose-100 px-3 py-1 text-lg border border-zinc-300 hover:bg-rose-200 disabled:opacity-50" type="submit" disabled={postingEntry}>
            {postingEntry ? 'Posting…' : 'Post'}
          </button>
        </form>
      </section>

      {error && <p>{error}</p>}

      <section className="mx-auto my-10 w-1/2 rounded-lg border border-zinc-300 bg-zinc-200 p-3">
        {loading ? (
          <p className="">Loading entries…</p>
        ) : entries.length === 0 ? (
          <p className="">No entries yet. Be the first to write one.</p>
        ) : (
          entries.map((entry) => (
            <article className="py-4" key={entry.id}>
              <time className="text-xs text-gray-600">{entry.created_at}</time>
              <p className="p-2 text-justify">{entry.content}</p>
            </article>
          ))
        )}
      </section>
    </main>
  )
}

export default App

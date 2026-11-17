import type { JournalEntry, NewJournalEntry } from '../types/types'

export async function getEntries(): Promise<JournalEntry[]> {
  const response = await fetch('/api/entries')

  if (!response.ok)
    throw new Error(`Could not load entries (${response.status})`)

  return (await response.json()) as JournalEntry[]
}

export async function createEntry(entry: NewJournalEntry): Promise<JournalEntry> {
  const response = await fetch('/api/entries', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(entry),
  })

  if (!response.ok)
    throw new Error(`Could not create entry (${response.status})`)

  return (await response.json()) as JournalEntry
}

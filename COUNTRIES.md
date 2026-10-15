# Adding a country to Lernova content

Every country uses the same structure, so the app needs no new code for a new country.

1. In index.json add a grade entry with a "country" code (US, IR, DE ...):
   {"grade": 9, "subject": "Mathematics", "country": "IR", "chapters": [ {"id": "ir9m-ch1", "title": "Sets", "lessons": [ {"id": "ir9m-ch1-l1", "title": "Sets and subsets"} ] } ]}
   Entries without "country" are treated as US.
2. Ids: <country><grade><subject letter>-ch<N>-l<M> (lowercase, unique forever).
3. Files (same names for every country):
   summaries/<chapterId>.json   short summary layer, { "lesson title": "text" }
   details/<lessonId>.md        detailed layer
   banks/<chapterId>.txt        exam bank (50 questions, 4 options, E/M/H header)
4. Lesson and chapter titles must match the app's list for that country exactly.
5. Every topic in every country shows the same four buttons: Summary, Detailed, Exam, Notes (+ Ask AI). A missing layer shows "Coming soon" until its file is uploaded.
6. Never delete old files; add new ids instead (students may need last year's material).

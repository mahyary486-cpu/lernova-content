# Lernova Content

Public lesson content for the Lernova app (US math curriculum).

- `version.json` : bump the number whenever content changes; the app refreshes when it sees a new number.
- `index.json` : grades, chapters and lesson titles.
- `summaries/<chapter>.json` : short topic summaries shown inside the app.
- `details/<lesson>.md` : full explanations with worked examples.
- `banks/<chapter>.txt` : 50 multiple-choice questions per chapter (question|A|B|C|D|answer index|explanation). The first line lists each question's level: E easy, M medium, H hard.

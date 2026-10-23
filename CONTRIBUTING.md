# Rules for adding content (read this before every session)

Many people and Claude accounts add countries to this repo. Follow these rules so nobody overwrites anybody.

1. **Start every session with `git pull --rebase`.** Never work from an old zip or an old copy of the repo.
2. **Only touch your own country.** Your files are `banks/<id>*`, `summaries/<id>*` and `details/<id>*`, where the chapter/lesson ids start with your country's prefix (for example `ir9m-…`, `de…`).
3. **Never commit `manifest.json` or anything in `packs/`.** The GitHub Action "Build manifest" creates them from `index.json` after every push. If you run `tools/build_manifest.py` to test, undo it before committing: `git checkout -- manifest.json packs`.
4. **Never replace `index.json` with your own copy.** Edit it with a small script that reads the current file, adds or changes only your country's entries, and writes it back. Keep every other country untouched.
5. **Do not delete files.** Add new ids instead (the app relies on old ids staying valid).
6. **`version.json`:** after `git pull --rebase`, add 1 to the number that is in the file at that moment.
7. **Push with the safety check:**
   `git pull --rebase && python3 tools/check_countries.py && git push origin main`
8. **Wait for the green tick of the Action before the next push**, then run `git pull -q && python3 tools/verify_content.py`.
9. After the push, close the Lernova app completely and open it again, so the new country flag appears.

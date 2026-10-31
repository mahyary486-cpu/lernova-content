#!/data/data/com.termux/files/usr/bin/bash
# Publish the French content. Only index.json (FR entries) and fr-* files are touched;
# packs/FR.json and manifest.json are rebuilt by the bot (tools/build_manifest.py).
# Run from the repo root:  bash tools/fr_push.sh "FR: Mathématiques Seconde"
set -e
MSG="${1:-FR: content update}"
BR=$(git rev-parse --abbrev-ref HEAD)
FILES="banks/fr-* summaries/fr-* details/fr-* index.json tools/fr_*_part.json tools/fr_index.py tools/fr_push.sh tools/README_FR.md"

sync() {
  if ! git pull --rebase origin "$BR"; then
    # only index.json is shared: keep the upstream copy, the FR entries are re-applied afterwards
    git checkout --ours index.json 2>/dev/null || true
    git add index.json
    GIT_EDITOR=true git rebase --continue || { echo "Unexpected conflict. Run: git rebase --abort  and ask for help."; exit 1; }
  fi
}

# the old merge tool wrote packs/FR.json by hand; the bot does it now
git rm -q --ignore-unmatch tools/fr_merge.py
python3 tools/fr_index.py
git add $FILES
git commit -m "$MSG" || echo "Nothing new to commit."
for i in 1 2 3 4 5; do
  sync
  python3 tools/fr_index.py
  git add index.json
  git commit --amend --no-edit -q || true
  if git push origin "$BR"; then echo "PUSHED"; exit 0; fi
  echo "Push rejected (another account or the bot pushed first). Retry $i/5 ..."
done
echo "Could not push after 5 tries."; exit 1

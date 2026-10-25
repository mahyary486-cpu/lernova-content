#!/data/data/com.termux/files/usr/bin/bash
# Publish the French content without touching other countries.
# Run from the repo root:  bash tools/fr_push.sh "FR: Mathématiques 3e"
set -e
MSG="${1:-FR: content update}"
BR=$(git rev-parse --abbrev-ref HEAD)
FILES="banks/fr-* summaries/fr-* details/fr-* packs/FR.json manifest.json tools/fr_math9_part.json tools/fr_merge.py tools/fr_push.sh tools/README_FR.md"

sync() {
  if ! git pull --rebase origin "$BR"; then
    git checkout --ours manifest.json 2>/dev/null || true
    git add manifest.json
    GIT_EDITOR=true git rebase --continue || { echo "Unexpected conflict. Run: git rebase --abort  and ask for help."; exit 1; }
  fi
}

python3 tools/fr_merge.py
git add $FILES
git commit -m "$MSG" || { echo "Nothing new to commit."; }
for i in 1 2 3 4 5; do
  sync
  python3 tools/fr_merge.py
  git add manifest.json packs/FR.json
  git commit --amend --no-edit -q || true
  if git push origin "$BR"; then echo "PUSHED"; exit 0; fi
  echo "Push rejected (another account pushed first). Retry $i/5 ..."
done
echo "Could not push after 5 tries."; exit 1

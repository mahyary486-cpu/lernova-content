#!/data/data/com.termux/files/usr/bin/bash
# Publish the Argentine (AR) content. Touches only index.json (AR entries) and ar-* files;
# packs/AR.json and manifest.json are rebuilt by the GitHub Action.
# Run from the repo root:  bash tools/ar_push.sh "AR: grade 9"
# The GitHub token is asked here (hidden) and is NEVER saved in the repo or in git config.
set -e
MSG="${1:-AR: content update}"
REPO="github.com/mahyary486-cpu/lernova-content.git"
BR=$(git rev-parse --abbrev-ref HEAD)
FILES="banks/ar-* summaries/ar-* details/ar-* index.json tools/ar_*_part.json tools/ar_index.py tools/ar_push.sh tools/README_AR.md"

printf "GitHub token: "; read -rs TOKEN; echo
[ -n "$TOKEN" ] || { echo "No token entered."; exit 1; }
URL="https://x-access-token:${TOKEN}@${REPO}"

sync() {
  if ! git pull --rebase "$URL" "$BR"; then
    git checkout --ours index.json 2>/dev/null || true
    git add index.json
    GIT_EDITOR=true git rebase --continue || { echo "Unexpected conflict. Run: git rebase --abort"; exit 1; }
  fi
}
bump() {
  python3 - <<'P'
import json,datetime
d=json.load(open("version.json"));d["version"]+=1;d["updated"]=datetime.date.today().isoformat()
open("version.json","w").write(json.dumps(d,indent=2)+"\n")
P
}

python3 tools/ar_index.py
git add $FILES
git commit -m "$MSG" || echo "Nothing new to commit."
for i in 1 2 3 4 5; do
  sync
  python3 tools/ar_index.py
  git add index.json
  git commit --amend --no-edit -q || true
  git checkout -q origin/"$BR" -- version.json 2>/dev/null || true
  bump; git add version.json; git commit --amend --no-edit -q || true
  python3 tools/check_countries.py || { echo "Safety check failed. Nothing pushed."; exit 1; }
  if git push "$URL" "$BR"; then echo "PUSHED. Wait for the GitHub Action, then: python3 tools/verify_content.py"; unset TOKEN URL; exit 0; fi
  echo "Push rejected (someone pushed first). Retry $i/5 ..."
done
echo "Could not push after 5 tries."; exit 1

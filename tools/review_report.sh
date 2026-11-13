#!/bin/sh
echo "##### PART 1: content check"
cd ~/lernova-content && python3 tools/check_us.py
echo
echo "##### PART 2: feedback button in the app"
cd ~/Learnova || exit 0
grep -rniE "feedback|فید ?بک|بازخورد" lib | head -80
for f in $(grep -rliE "feedback|فید ?بک|بازخورد" lib); do
  echo
  echo "##### FILE $f ($(wc -c < "$f") bytes)"
  if [ "$(wc -c < "$f")" -lt 90000 ]; then cat "$f"; else grep -niE -C 45 "feedback|فید ?بک|بازخورد" "$f"; fi
done
echo
echo "##### PART 3: app file list"
ls lib lib/* 2>/dev/null | head -120

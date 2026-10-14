#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p .hyperframes
npx hyperframes render --quality delivery --fps 30 --workers 4 --gpu --output .hyperframes/delivery.mp4
ffmpeg -y -hide_banner -i .hyperframes/delivery.mp4 \
  -c:v libx264 -preset medium -crf 22 -pix_fmt yuv420p \
  -af loudnorm=I=-18:TP=-1.5:LRA=9 -c:a aac -b:a 192k -ar 48000 \
  -t 77 -movflags +faststart ../../assets/videos/kujo-intro.mp4
python3 - <<'PY'
from pathlib import Path
import re
Path('../../assets/videos/kujo-intro.vtt').write_text('WEBVTT\n\n'+re.sub(r'(?<=\d),(?=\d{3})', '.', Path('captions.srt').read_text()))
PY

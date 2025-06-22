#!/usr/bin/env bash
# start.sh — start your HTTP server in CGI mode

# make sure the CGI script is executable
chmod +x cgi-bin/deepfake_quiz.cgi

# launch the server (Render will set $PORT)
exec python3 -m http.server "${PORT:-8000}" --cgi
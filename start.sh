cat > start.sh <<'EOF'
#!/usr/bin/env bash
# start.sh — Launch Python built-in server in CGI mode

# Ensure the CGI script is executable
chmod +x cgi-bin/deepfake_quiz.cgi

# Start HTTP server on PORT (or default 8000) with CGI support
exec python3 -m http.server "${PORT:-8000}" --cgi
EOF
chmod +x start.sh
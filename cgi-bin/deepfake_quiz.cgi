cat > cgi-bin/deepfake_quiz.cgi <<'EOF'
#!/usr/bin/env bash
# deepfake_quiz.cgi — Bash CGI script for scoring the quiz

# 1) HTTP header
echo "Content-Type: text/html; charset=UTF-8"
echo ""

# 2) Correct answers array (0=Real, 1=Fake)
ANS=(1 0 1 0 1)
score=0
total=${#ANS[@]}

# 3) Pull q1…q5 from QUERY_STRING and score
for i in $(seq 1 $total); do
  val=$(echo "$QUERY_STRING" \
        | sed -n "s/.*q$i=\([^&]*\).*/\1/p")
  if [ "$val" = "${ANS[$((i-1))]}" ]; then
    score=$((score+1))
  fi
done

# 4) Emit result HTML
cat <<HTML
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Quiz Results</title></head>
<body style="font-family:sans-serif;text-align:center;padding:2em;">
  <h1>Your Quiz Results</h1>
  <p style="font-size:2em;">You scored <strong>$score</strong> out of <strong>$total</strong>.</p>
  <a href="/quiz/index.html" style="display:inline-block;margin-top:1em;
     padding:0.6em 1.2em;background:#3366cc;color:#fff;
     text-decoration:none;border-radius:4px;">Try Again</a>
</body>
</html>
HTML
EOF
chmod 755 cgi-bin/deepfake_quiz.cgi
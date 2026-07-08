from pathlib import Path
from flask import Flask, render_template_string, request, redirect, url_for
import qrcode

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>QR Code Generator</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #f7f9fc; }
    .card { max-width: 500px; margin: auto; background: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    input { width: 100%; padding: 10px; margin-top: 8px; margin-bottom: 16px; }
    button { background: #2563eb; color: white; border: none; padding: 10px 16px; border-radius: 8px; cursor: pointer; }
    img { margin-top: 20px; max-width: 100%; }
  </style>
</head>
<body>
  <div class="card">
    <h2>QR Code Generator</h2>
    <p>Enter a URL and generate a QR code for students.</p>
    <form method="post">
      <label for="url">Website URL</label>
      <input id="url" name="url" placeholder="https://example.com" required>
      <button type="submit">Generate QR Code</button>
    </form>
    {% if qr_path %}
      <h3>QR Code</h3>
      <img src="{{ qr_path }}" alt="Generated QR code">
    {% endif %}
  </div>
</body>
</html>
"""


def create_qr_code(url: str, output_path: str | Path = "static/qr.png") -> Path:
    """Create a simple QR code image for a given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output)
    return output


@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url:
            output_file = create_qr_code(url, "static/qr.png")
            qr_path = url_for("static", filename="qr.png")
            return render_template_string(HTML_TEMPLATE, qr_path=qr_path)
    return render_template_string(HTML_TEMPLATE, qr_path=None)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

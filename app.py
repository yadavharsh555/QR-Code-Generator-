from flask import Flask, render_template, request, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            # Convert to Base64 for displaying in HTML
            img_io = BytesIO()
            img.save(img_io, format="PNG")
            img_base64 = base64.b64encode(img_io.getvalue()).decode("utf-8")
            qr_url = f"data:image/png;base64,{img_base64}"

            return render_template("qr.html", qr_url=qr_url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

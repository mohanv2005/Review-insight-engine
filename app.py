import logging
import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from main import run_pipeline

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY", "dev-change-me-in-production"
)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
ALLOWED_EXTENSIONS = {"csv"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def _allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def _report_path() -> Path:
    return Path(OUTPUT_FOLDER) / "report.html"


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file is None or file.filename == "":
        flash("No file selected.", "error")
        return redirect(url_for("home"))

    if not _allowed_file(file.filename):
        flash("Please upload a CSV file.", "error")
        return redirect(url_for("home"))

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    safe_name = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], safe_name)
    file.save(filepath)

    try:
        run_pipeline(filepath, OUTPUT_FOLDER)
    except Exception:
        logger.exception("Pipeline failed for upload %s", safe_name)
        flash(
            "Analysis failed. Check that your CSV has the required columns "
            "(e.g. movie, review_text) and try again.",
            "error",
        )
        return redirect(url_for("home"))

    if not _report_path().is_file():
        logger.error("Report missing after successful pipeline run: %s", _report_path())
        flash("Report could not be generated. Please try again.", "error")
        return redirect(url_for("home"))

    return redirect(url_for("show_report"))


@app.route("/report")
def show_report():
    path = _report_path()
    if not path.is_file():
        flash("No report is available. Upload a CSV to generate one.", "warning")
        return redirect(url_for("home"))

    html_content = path.read_text(encoding="utf-8")
    return html_content, 200, {"Content-Type": "text/html; charset=utf-8"}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)

"""Manual LinkedIn connection review from a CSV or Excel participant list.

Does not log in, scrape, inspect account state, or send invitations.
You review each profile yourself and record the outcome.

Usage:
    python linkedin_connection_review.py linkedin_database.csv
    python linkedin_connection_review.py participant_list.xlsx

If no path is specified, searches for linkedin_database.csv alongside this script.
URLs are read from the fourth spreadsheet column to match the original script.
"""

from pathlib import Path
import sys
import webbrowser
from urllib.parse import urlsplit

import pandas as pd

MESSAGE = (
    "Hi! I'd love to connect, exchange ideas, support each other's journeys, "
    "and stay in touch beyond the program. Looking forward to connecting!"
)
URL_COLUMN_INDEX = 3  # 0-based: fourth column, as in the original script
DONE_STATUSES = {"sent", "connected", "pending", "skipped", "invalid_url", "duplicate"}
CHOICES = {
    "s": "sent", "c": "connected", "p": "pending", "k": "skipped",
    "e": "error", "q": "quit",
}


def normalize_profile_url(raw):
    if pd.isna(raw):
        return ""
    url = str(raw).strip().strip('"\'')
    if not url:
        return ""
    if url.startswith(("linkedin.com/", "www.linkedin.com/")):
        url = "https://" + url
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"} or host not in {"linkedin.com", "www.linkedin.com"}:
        return ""
    path = parsed.path.rstrip("/")
    if not path.lower().startswith("/in/") or path.lower() == "/in":
        return ""
    return "https://www.linkedin.com" + path.lower() + "/"


def load_table(path):
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    if path.suffix.lower() in {".xlsx", ".xlsm"}:
        return pd.read_excel(path, dtype=str, keep_default_na=False)
    raise ValueError("Use a .csv or .xlsx file")


def main():
    default = Path(__file__).resolve().parent / "linkedin_database.csv"
    source = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else default
    if not source.is_file():
        print(f"Input file not found: {source}")
        print('Example: python linkedin_connection_review.py "C:\\Users\\Prerana\\Downloads\\my_list.xlsx"')
        return

    results = source.with_name(source.stem + "_review_results.csv")
    # Resume after stopping; keep outcome history unless the user deletes the results file.
    table = load_table(results if results.exists() else source)
    if table.shape[1] <= URL_COLUMN_INDEX:
        print("The file must have at least four columns; the fourth must contain LinkedIn URLs.")
        return

    if "review_status" not in table.columns:
        table["review_status"] = ""
    if "review_url" not in table.columns:
        table["review_url"] = ""

    url_col = table.columns[URL_COLUMN_INDEX]
    print(f"Reading profile URLs from column: {url_col}")
    print("This script only opens profile pages. You check status and click Send yourself.")
    print("Your approved message:\n" + MESSAGE + "\n")
    print("After manually reviewing each profile, type:")
    print("  s=invitation sent, c=already connected, p=invitation pending")
    print("  k=skipped, e=error, q=save and quit\n")

    seen = set()
    for index in table.index:
        url = normalize_profile_url(table.at[index, url_col])
        table.at[index, "review_url"] = url
        status = str(table.at[index, "review_status"]).strip().lower()

        if not url:
            table.at[index, "review_status"] = "invalid_url"
            table.to_csv(results, index=False, encoding="utf-8-sig")
            continue
        if url in seen:
            table.at[index, "review_status"] = "duplicate"
            table.to_csv(results, index=False, encoding="utf-8-sig")
            continue
        seen.add(url)
        if status in DONE_STATUSES:
            continue

        print(f"\nRow {index + 2}: {url}")
        webbrowser.open(url, new=2)
        while True:
            choice = input("Review in browser, then enter s/c/p/k/e/q: ").strip().lower()
            if choice in CHOICES:
                break
            print("Enter one of: s, c, p, k, e, q")
        if choice == "q":
            table.to_csv(results, index=False, encoding="utf-8-sig")
            print(f"Saved progress: {results}")
            return
        table.at[index, "review_status"] = CHOICES[choice]
        table.to_csv(results, index=False, encoding="utf-8-sig")

    print(f"Finished. Saved results: {results}")
    print(table["review_status"].value_counts(dropna=False).to_string())


if __name__ == "__main__":
    main()

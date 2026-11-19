<div align="center">

<img src="assets/connection-toolkit-banner.png" alt="LinkedIn Connection Toolkit: Connect with confidence — spreadsheet and networking illustration" width="100%" />

<br />

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-CSV%20%26%20Excel-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Optional-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-0F766E?style=for-the-badge&logo=readthedocs&logoColor=white)

**A small Python project for keeping LinkedIn connection outreach organized, one profile at a time.**

[Get started](#-getting-started) · [How it works](#-how-it-works) · [Request the optional auto-invite code](#-request-the-optional-auto-invite-code) · [Contact](#-contact)

</div>

---

## 👋 Welcome

Networking is easier when you can focus on people instead of juggling tabs and remembering whom you have already contacted.

I put this toolkit together to make connection outreach from a participant list or spreadsheet a little more manageable. It helps you prepare profile links, avoid duplicates, keep track of your progress, and return to the list without starting over.

The **public review script** opens profiles for you to review. **It does not send LinkedIn invitations automatically.** An optional Selenium-based invitation helper is discussed separately below.

## ✨ What this project does

| | Feature | What it means for you |
|:---:|---|---|
| 📊 | **CSV & Excel support** | Bring an existing `.csv`, `.xlsx`, or `.xlsm` participant list. |
| 🔗 | **Profile URL validation** | Skip empty or invalid links rather than opening them. |
| 🧹 | **Duplicate detection** | Avoid reviewing the same LinkedIn URL twice. |
| 👀 | **Human review** | Check each person's profile and invitation status before acting. |
| 📝 | **Progress tracking** | Save your decisions in a separate results CSV. |
| 🔄 | **Resume later** | Continue a review using the saved results instead of beginning again. |
| 🔐 | **No stored passwords** | The public review script uses your regular browser; it does not request credentials. |

## 🧭 How it works

```mermaid
flowchart LR
    A[📄 CSV or Excel list] --> B[🔗 Check profile URLs]
    B --> C{Duplicate or invalid?}
    C -->|Yes| D[⏭️ Record and skip]
    C -->|No| E[👤 Open profile for review]
    E --> F[✅ Choose an outcome]
    D --> G[📊 Save results CSV]
    F --> G
```

**Example input:** Your spreadsheet needs **at least four columns**. The script reads LinkedIn profile links from **column D**, the fourth column (index `3`).

| A · Name | B · Group | C · Notes | D · LinkedIn URL |
|---|---|---|---|
| Example Person | Learning Cohort | Met during program | `https://www.linkedin.com/in/your-profile-slug/` |

> The URL above is a placeholder, not a real participant profile. Use your own authorized participant list. To read URLs from another column, change `URL_COLUMN_INDEX = 3` in the Python script (`0` means column A).

## 🚀 Getting started

### 1. Download the project

On GitHub, choose **Code → Download ZIP**, then extract the folder. If you use Git, you can clone the repository instead.

Your project folder will look something like this:

```text
linkedin-connection-toolkit/
├── README.md
├── requirements.txt
├── commands.txt
├── linkedin_connection_review.py
├── assets/
│   └── connection-toolkit-banner.png
└── linkedin_database.csv         # your private input; do not upload to GitHub
```

### 2. Check your Python installation

Open **Windows Command Prompt** in the project folder and run:

```bat
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/). A currently supported Python version with compatible packages is recommended.

### 3. Create a virtual environment (recommended)

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install the requirements

```bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The requirements file contains the direct dependencies `pandas`, `openpyxl`, and `selenium`. Selenium is only needed for the separate, optional browser-automation helper.

### 5. Add your spreadsheet

Put your input file in the same folder as the script. It can be named `linkedin_database.csv` or anything you prefer.

**Please don't commit real participant data, email addresses, or connection histories to a public repository.**

### 6. Start your connection review

For a CSV:

```bat
python linkedin_connection_review.py "linkedin_database.csv"
```

For an Excel file:

```bat
python linkedin_connection_review.py "participants.xlsx"
```

The script opens each valid, unique profile in your default browser. **You** check the profile and decide whether to send a request using LinkedIn's own interface.

When the terminal asks for a result, type one of these codes:

| Type | Record as | When to use it |
|:---:|---|---|
| `s` | `sent` | You manually sent an invitation. |
| `c` | `connected` | You are already connected. |
| `p` | `pending` | A request is already pending. |
| `k` | `skipped` | You don't want to invite this person. |
| `e` | `error` | Something went wrong; revisit later. |
| `q` | Save and quit | You want to stop for now. |

Your progress is saved next to the source file, for example:

```text
linkedin_database_review_results.csv
```

Run the same command again to resume your review. Check the recorded statuses before making further changes.

## 💌 A connection note you can adapt

Here's a friendly note for meeting people through a course, program, or community:

> Hi! I'd love to connect, exchange ideas, support each other's journeys, and stay in touch beyond the program. Looking forward to connecting!

Make it your own wherever possible. A short, relevant note usually feels more personal than a generic introduction.

## 🤖 Request the optional auto-invite code

Interested in the **optional Selenium-based invitation helper** that attempts to attach a note when sending a connection invitation?

✉️ **Email:** [preranapandit07@gmail.com](mailto:preranapandit07@gmail.com?subject=LinkedIn%20Auto-Invite%20Code%20Request)

Please use **“LinkedIn Auto-Invite Code Request”** as the subject and briefly tell me how you plan to use it. I can share more information about the code and its limitations.

**Important:** That helper is **not part of the public review walkthrough** and is not an official LinkedIn integration. LinkedIn may restrict accounts for unauthorized automated activity. UI changes, verification prompts, invitation limits, or unavailable “Add a note” options can stop automation. Never bypass access controls, and do not assume an invitation was delivered simply because a button was clicked.

## 🛠️ Troubleshooting

<details>
<summary><strong>“FileNotFoundError: No such file or directory”</strong></summary>

Make sure your spreadsheet is in the folder where you run the command, or provide its complete path:

```bat
python linkedin_connection_review.py "C:\Users\YourName\Downloads\participants.xlsx"
```

</details>

<details>
<summary><strong>“ModuleNotFoundError: No module named pandas”</strong></summary>

Install the dependencies into the Python environment used by your terminal:

```bat
python -m pip install -r requirements.txt
```

</details>

<details>
<summary><strong>“The file must have at least four columns”</strong></summary>

Add the profile URLs in column D, or edit the `URL_COLUMN_INDEX` variable in the script to match your file. Column numbering starts at zero in Python.

</details>

<details>
<summary><strong>Do I need Firefox or a browser driver?</strong></summary>

Not for `linkedin_connection_review.py`: it opens URLs in your default browser. The optional Selenium-based helper uses Firefox and may need a compatible browser driver (often managed automatically by Selenium).

</details>

<details>
<summary><strong>Does the public script detect whether we're already connected?</strong></summary>

No. It checks URL formatting and duplicates. **You** inspect the LinkedIn profile and record `connected`, `pending`, or another status. This avoids pretending that the script can reliably inspect your private LinkedIn account.

</details>

## 🛡️ Privacy and responsible use

- Use participant data you have permission to process, and avoid publishing personal data or private connection histories.
- Keep passwords, session cookies, tokens, and `.env` files **out of your repository**.
- Respect LinkedIn's terms and invitation limits. This toolkit is independent and is **not affiliated with or endorsed by LinkedIn**.
- Prefer relevant, consensual networking over unsolicited mass outreach.

## 📁 Suggested files for GitHub

| File | Purpose |
|---|---|
| `README.md` | Project introduction and instructions (this page). |
| `assets/connection-toolkit-banner.png` | Banner image displayed above. |
| `linkedin_connection_review.py` | Public, review-first workflow. |
| `requirements.txt` | Python packages needed to run the scripts. |
| `commands.txt` | Handy terminal commands. |
| `.gitignore` | Helps keep local lists, environments, and results out of Git. |

## 📬 Contact

Have a question, found a bug, or want to ask about the optional invitation helper? I'd love to hear from you.

**[📧 preranapandit07@gmail.com](mailto:preranapandit07@gmail.com?subject=LinkedIn%20Connection%20Toolkit)**

---

<div align="center">

**Connect thoughtfully. Keep track. Make it meaningful.** ✨

<sub>A community-friendly Python toolkit for organizing outreach — not an official LinkedIn product.</sub>

</div>

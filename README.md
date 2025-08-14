# 🚀 OLX PL Ad Reposter

A powerful Python tool that **automates the scraping and reposting of OLX ads** between multiple accounts.

---

## ✨ Features

* 📦 **Scrape Ads** — Extracts listings from OLX including images, descriptions, prices, and contact info.
* 🔄 **Repost Between Accounts** — Seamlessly transfers and reposts ads between multiple OLX accounts.
* 🧠 **Database Integration** — Stores ad information for easy management and repost tracking.
* ⚡ **Asynchronous & Fast** — Built with asyncio for non-blocking, high-performance scraping/posting.
* 🧭 **Browser Automation** — Uses [DrissionPage](https://github.com/g1879/DrissionPage/) for Chrome-based automation.

---

## 🧰 Prerequisites

* Python 3.8 or higher
* Chrome browser installed
* [UV](https://github.com/astral-sh/uv) (Python package manager)
* Environment variables configured (see below)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kravchenski/olx-repost-python.git
   cd olx-repost-python
   ```

2. **Create virtual environment and install dependencies:**

   ```bash
   pip install uv
   python -m uv venv
   ```

3. **Set up environment variables**<br>
   If you're using POSTGRES:

   ```ini
   EMAIL_CONFIG_JSON='{
     "emails": [
         "test@weq.com",
         "test1@cvb.uio"
     ]
   }'
   EMAIL_PASSWORD = yourpass
   FIRST_NAME = Nowak
   LAST_NAME = Kowalski
   
   
   POSTGRES_HOST = localhost
   POSTGRES_USER = postgres
   POSTGRES_PASSWORD = root
   POSTGRES_DATABASE = olx_db
   ```
      If you're using MYSQL:

   ```ini
   EMAIL_CONFIG_JSON='{
     "emails": [
         "test@weq.com",
         "test1@cvb.uio"
     ]
   }'
   EMAIL_PASSWORD = yourpass
   FIRST_NAME = Nowak
   LAST_NAME = Kowalski
   
   
   MYSQL_HOST = localhost
   MYSQL_USER = mysql
   MYSQL_PASSWORD = root
   MYSQL_DATABASE = olx_db
   ```

---

## 🚦 Usage

### Run main scripts:

#### POSTGRES
```bash
python -m uv run collect_ads_pg.py
python -m  uv run transfer_to_acc_pg.py
```
#### MYSQL
```bash
python -m uv run collect_ads_mysql.py
python -m  uv run transfer_to_acc_mysql.py

```

### Example use cases:

* Reposting your business ads regularly to keep them visible
* Cloning successful listings across multiple OLX accounts
* Archiving and reusing ad data with image support

---

## 📚 Technologies Used

* Python 🐍
* Asyncio 🧵
* DrissionPage 🌐
* asyncpg 📁
* UV package manager ⚙️
* dotenv 🔐

---

## 🤝 Contributing

Pull requests and contributions are welcome! Please open an issue first to discuss your idea.

---

## 📄 License

[MIT License](LICENSE)

---

## 👤 Author

* **[@kravchenski](https://github.com/kravchenski)** — original creator

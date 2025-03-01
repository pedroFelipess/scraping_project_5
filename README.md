# scraping_project_5
Pichau Monitor Scraper

This project extracts data from the monitor department of the Pichau store, capturing the name and price of the available products on the website.

## 🛠 Technologies Used

- **Selenium**: For web automation and data extraction.
- **Pandas**: For data manipulation and organization.

## 📌 Features

- Accesses Pichau's monitor page.
- Captures the name and price of each listed monitor.
- Organizes the data into a Pandas DataFrame.
- Exports the data to a CSV file for easy analysis.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/pedroFelipess/scraping_project_5.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## 📂 Project Structure

```
📁 pichau_scraper
│── 📄 main.py  # Main scraper code
│── 📄 requirements.txt  # Project dependencies
│── 📄 README.md  # Project documentation
│── 📄 pichau_monitors.csv  # Generated file with extracted data
```

## 📌 Requirements

- Python 3.x
- Google Chrome and a compatible ChromeDriver

## 📈 Sample Output

| Monitor Name | Price   |
| ------------ | ------- |
| Monitor X    | R\$999  |
| Monitor Y    | R\$1299 |

## 📜 License

This project is licensed under the MIT License. Feel free to use and contribute!

---

💡 **Tip:** If Pichau's website structure changes, you may need to update the Selenium selectors to ensure correct data extraction.


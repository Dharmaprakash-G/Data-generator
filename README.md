📦 Dummy Data Generator

A schema-based dummy / synthetic data generator for developers who need realistic test data without downloading datasets from the internet.

Perfect for:

Hackathons

MVP development

Backend & frontend testing

Personal projects

Learning & demos

🚀 What This Tool Does

Instead of searching for datasets, you simply:

Define your own table name

Define column names & data types

Choose number of rows

Generate realistic dummy data

Export as CSV (more formats coming)

✨ Key Features

🔧 Schema-driven (you control everything)

📄 Generate realistic fake data (names, emails, cities, dates, etc.)

🧪 Ideal for testing when real data doesn’t exist

⚡ Fast & lightweight

🛠 Easy to extend (JSON, SQL, API, UI)

📁 Project Structure
dummy_data_tool/
│
├── generator/
│   ├── engine.py        # Core data generation logic
│   ├── types.py         # Data type → faker mapping
│
├── exporters/
│   └── csv_exporter.py  # CSV export logic
│
├── schema.json          # Example schema
├── main.py              # CLI entry point
├── requirements.txt
└── README.md

🧩 Schema Format

You define your dataset using a simple JSON schema.

Example: schema.json
{
  "table_name": "users",
  "rows": 10,
  "columns": [
    { "name": "id", "type": "int", "min": 1, "max": 1000 },
    { "name": "name", "type": "full_name" },
    { "name": "email", "type": "email", "unique": true },
    { "name": "age", "type": "int", "min": 18, "max": 60 },
    { "name": "city", "type": "city" },
    { "name": "created_at", "type": "date" }
  ]
}

🛠 Supported Data Types (v1)
Type	Description
int	Random integers (min/max supported)
full_name	Realistic full names
email	Fake but valid emails
city	City names
date	Random date (last 2 years)
uuid	UUID v4
boolean	true / false

More types can be added easily.

⚙️ Installation
1. Clone the repository
git clone https://github.com/USERNAME/dummy-data-generator.git
cd dummy-data-generator

2. Install dependencies
pip install -r requirements.txt

▶️ Usage

Run the generator using the CLI:

python main.py schema.json output.csv

Output
✅ Generated 10 rows into output.csv

📄 Sample Output (CSV)
id,name,email,age,city,created_at
101,Rahul Sharma,rahul@gmail.com,28,Mumbai,2024-02-12
102,Ananya Verma,ananya@gmail.com,35,Delhi,2023-11-08

🧠 Why This Project?

Most dummy data tools:

Force predefined schemas

Don’t match real project needs

Require internet datasets

This tool lets you:

Define your own schema and instantly generate production-like data.

🚧 Roadmap

Planned features:

 JSON export

 SQL export (MySQL / PostgreSQL)

 Table relationships (foreign keys)

 FastAPI REST API

 Web UI

 AI-assisted schema generation

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a feature branch

Commit changes

Open a pull request

📜 License

MIT License
Free to use, modify, and distribute.

🙌 Author

Built by DP
For developers who want control over their test data.

⭐ If you find this useful

Give the repo a star — it helps more developers discover it!

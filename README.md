# GeneratorX

A schema-based dummy / synthetic data generator for developers who need realistic test data without downloading datasets from the internet. Perfect for hackathons, MVP development, backend & frontend testing, personal projects, and learning demos.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.7+ and pip installed on your system. Check your Python version:

```bash
python --version
```

### Installing

Follow these steps to get a development environment running:

**Step 1:** Clone the repository

```bash
git clone https://github.com/USERNAME/dummy-data-generator.git
cd dummy-data-generator
```

**Step 2:** Install dependencies

```bash
pip install -r requirements.txt
```

**Step 3:** Create your schema file (or use the provided example)

```bash
# Use the included schema.json or create your own
cat schema.json
```

**Step 4:** Generate your first dataset

```bash
python main.py schema.json output.csv
```

You should see output like:

```
✅ Generated 10 rows into output.csv
```

## Running the tests

Explain how to run the automated tests for this system (coming soon)

### Break down into end to end tests

End-to-end tests will verify the complete data generation pipeline from schema parsing to CSV export.

```bash
# Example (future implementation)
python -m pytest tests/test_e2e.py
```

### And coding style tests

Coding style tests ensure code quality and consistency using flake8 and black.

```bash
# Example (future implementation)
flake8 generator/ exporters/
black --check .
```

## Deployment

This tool is designed for local development use. For production deployment:

* **API Version**: Deploy the FastAPI REST API (roadmap feature) using Docker or cloud services like AWS/GCP
* **Web UI**: Host the web interface (roadmap feature) on platforms like Vercel or Netlify
* **CLI Tool**: Package as a PyPI package for easy installation via `pip install dummy-data-generator`

## Built With

* [Faker](https://faker.readthedocs.io/) - Python library for generating fake data
* [Python](https://www.python.org/) - Core programming language
* [JSON](https://www.json.org/) - Schema definition format

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

**Quick contribution guide:**
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/USERNAME/dummy-data-generator/tags).

## Authors

* **DP** - *Initial work* - [USERNAME](https://github.com/USERNAME)

See also the list of [contributors](https://github.com/USERNAME/dummy-data-generator/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to the Faker library for making realistic data generation simple
* Inspired by the need for better developer tooling in hackathons
* Thanks to all contributors and users who help improve this project

---

## 📁 Project Structure

```
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
```

## 🧩 Schema Format

Define your dataset using a simple JSON schema:

```json
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
```

## 🛠 Supported Data Types

| Type | Description |
|------|-------------|
| `int` | Random integers (min/max supported) |
| `full_name` | Realistic full names |
| `email` | Fake but valid emails |
| `city` | City names |
| `date` | Random date (last 2 years) |
| `uuid` | UUID v4 |
| `boolean` | true / false |

## 📄 Sample Output

```csv
id,name,email,age,city,created_at
101,Rahul Sharma,rahul@gmail.com,28,Mumbai,2024-02-12
102,Ananya Verma,ananya@gmail.com,35,Delhi,2023-11-08
```

## 🚧 Roadmap

- [ ] JSON export
- [ ] SQL export (MySQL / PostgreSQL)
- [ ] Table relationships (foreign keys)
- [ ] FastAPI REST API
- [ ] Web UI
- [ ] AI-assisted schema generation

---

⭐ **If you find this useful, give the repo a star — it helps more developers discover it!**

# The Mon Language Dictionary Database

Open-source centralized SQL-based Mon dictionary database with translation for Thai, Burmese, English and more.

## Project Overview

This project implements a multilingual dictionary database with support for:
- Mon language entries with IPA (International Phonetic Alphabet)
- Thai translations and definitions
- Burmese translations and definitions
- Categorized word relationships
- Synonym linking system
- Author attribution tracking

## Directory Structure

```
├── app-py/                    # Python applications
│   └── services/
│       └── alphabets/        # Mon language alphabet utilities
├── dist/                     # Web distribution files
├── docs/                     # Documentation and web interface
│   ├── assets/              # Static assets
│   │   ├── database/        # Database content
│   │   └── css/            # Styling
│   └── services/           # JavaScript services
└── sql/                    # Database schemas and SQL scripts
```

## Database Schema

The database consists of the following main tables:

### Word Table
```sql
CREATE TABLE Word (
    id INT AUTO_INCREMENT PRIMARY KEY,
    synonym_word_id INT,
    word VARCHAR(200) NOT NULL,
    ipa VARCHAR(1000) NULL,
    th VARCHAR(1000) NULL,
    lang_code VARCHAR(3) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT
)
```

### Definition Table
```sql
CREATE TABLE Definition (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word_id INT NOT NULL,
    lang_code VARCHAR(3) NOT NULL,
    pos_code VARCHAR(10) NOT NULL,
    category_id INT NULL,
    definition TEXT NOT NULL,
    example TEXT NOT NULL,
    created_at TIMESTAMP,
    author_id INT
)
```

## Setup Instructions

### Database Setup

1. Create the database:
```sql
CREATE DATABASE TheMonLanguageDictionary
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

2. Run the schema creation script:
```bash
mysql -u your_username -p TheMonLanguageDictionary < sql/db_creation_v1.sql
```

### Python Environment Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install mysql-connector-python
```

### Web Interface Setup

1. Navigate to the docs directory:
```bash
cd docs
```

2. Start a local server:
```bash
python -m http.server 8000
```

3. Access the web interface at `http://localhost:8000`

## Usage Examples

### Python Database Operations

```python
from app_py.services.db.word_crud import WordCRUD

# Initialize the database connection
word_db = WordCRUD(
    host='localhost',
    user='your_username',
    password='your_password',
    database='TheMonLanguageDictionary'
)

# Create a new word entry
word_id = word_db.create_word(
    word='မင်္ဂလာပါ',
    ipa='mɪ̀ɴɡəlà bà',
    th='สวัสดี',
    lang_code='my',
    author_id=1
)
```

### Web Interface Usage

The project includes a web-based interface for:
- Browsing the dictionary
- Searching words in Mon, Thai, or Burmese
- Viewing word relationships and categories
- Managing dictionary entries (with authentication)

Access the web interface by opening `docs/index.html` in a web browser.

## Language Codes

- `mn`: Mon
- `my`: Burmese (Myanmar)
- `th`: Thai

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Contributors to the Mon language documentation
- Mon language experts and native speakers
- Open-source tools and libraries used in this project

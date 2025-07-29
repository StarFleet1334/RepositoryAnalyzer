# 🚀 GitHub Repository Optimizer with Pareto Analysis

## 📖 Overview

In most software repositories, a small number of files or contributors typically account for the majority of changes. This project leverages **Pareto Analysis (the 80/20 rule)** to quickly identify:

* The **top 20% of files** that contribute to **80% of the repository changes**.
* The **top 20% of contributors** responsible for about **80% of the commits**.

Understanding these critical files and key contributors helps prioritize resources effectively, enhances code quality, and improves overall project management.

## 🎯 Objectives

* Analyze commit data to determine which files are most frequently changed.
* Identify which contributors make the majority of commits.
* Clearly highlight the most impactful files and contributors using Pareto Analysis.

## 🛠 How It Works

1. **Data Collection**

   * Counts occurrences of file changes across all commits.
   * Counts the number of commits per contributor.

2. **Data Processing**

   * Sorts collected data in descending order based on frequency.
   * Calculates cumulative frequency and percentage.

3. **Pareto Analysis**

   * Identifies the smallest subset of files/contributors that collectively represent at least 80% of the total changes or commits.

4. **Reporting**

   * Generates clearly formatted summaries indicating critical files and key contributors.


## 🚦 Getting Started

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/github-pareto-optimizer.git
cd github-pareto-optimizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### ⚙️ Configuration

Create or update the configuration file (`config.py`):

```python
# config.py
GITHUB_OWNER = 'your-github-username'
GITHUB_REPO = 'repository-name'
GITHUB_TOKEN = 'your-personal-access-token'
```

### 🚀 Running the Optimizer

Execute the main script:

```bash
python client.py
```

## 📊 Example Output

```
📂 Summary of File Changes Across All Commits:

Filename           | Count | Cumulative Frequency | Cumulative Frequency Percentage (%)
-------------------|-------|----------------------|------------------------------------
main.py            |    12 |                   12 |                             40.00%
utils.py           |     9 |                   21 |                             70.00%
README.md          |     3 |                   24 |                             80.00%

👤 Summary of Contributors Across All Commits:

Contributor Name   | Count | Cumulative Frequency | Cumulative Frequency Percentage (%)
-------------------|-------|----------------------|------------------------------------
ilialataria        |    15 |                   15 |                             50.00%
johndoe            |     8 |                   23 |                             76.67%
janesmith          |     3 |                   26 |                             86.67%
```

## 🧩 Project Structure

```
.
├── config
│   └── config.py
├── file_filter_strategy
│   └── dependencyFileFilter.py
├── formatter
│   └── outputFormatter.py
├── github_api
│   └── github_api.py
├── processor
│   └── commitProcessor.py
│   └── ParetoAnalyzer.py
├── client.py
├── .env
└── requirements.txt
```

## 📄 License

This project is licensed under the MIT License.

# Amazon Fulfillment Center Employee Voice Analytics

Exploratory people and operations analytics portfolio project using Python, Pandas, NLP sentiment classification, and rule-based workplace theme detection.

## Business question

Which workplace issues appear alongside negative employee feedback about Amazon fulfillment-center jobs, and which interventions would merit further operational testing?

## Dataset and method

- 138 selected Glassdoor reviews and 10 selected YouTube videos.
- Glassdoor pros and cons remain separate. YouTube transcripts are divided into overlapping approximately 80-word passages.
- RoBERTa sentiment classification: `cardiffnlp/twitter-roberta-base-sentiment-latest`.
- Baseline evaluation on 40 manually reviewed passages: **70.0% accuracy**, macro F1 about **0.70**, negative recall **63.2%**. The small curated set does not validate performance on every entry.
- Nine workplace themes detected using auditable keyword matching. A record counts at most once for each theme and sentiment flag, limiting repeated YouTube passage effects.

## Preliminary findings

| Theme | Records mentioning theme | Records with negative theme-matched passage | Share |
|---|---:|---:|---:|
| Scheduling | 53 | 23 | 43.4% |
| Workload | 29 | 21 | 72.4% |
| Management | 27 | 15 | 55.6% |
| Compensation | 79 | 11 | 13.9% |
| Safety | 12 | 8 | 66.7% |
| Training | 13 | 4 | 30.8% |

### Data Visualizations

#### Negative Feedback by Workplace Theme

![Negative Feedback by Theme](figures/negative_feedback_by_theme.png)

#### Negative Sentiment Rate by Workplace Theme

![Negative Sentiment Rate](figures/negative_sentiment_rate.png)

These percentages are **not measured employee dissatisfaction rates**. A model classifies the entire passage, which may refer to multiple themes. Also, public-source reviews are not representative of all workers. Training was the focus of an earlier proposal, but these exploratory results offer stronger preliminary support for investigating workload and scheduling.

## Operational proposals

1. Test task rotation and review physical workload, tracking fatigue and safety outcomes.
2. Assess shift predictability, overtime, and breaks, tracking employee feedback and hours.
3. Pilot manager coaching and check-ins, tracking communication and engagement measures.

Measure retention effects only with internal employee records and a comparison group. This project does not observe actual employee departures or demonstrate a causal relationship.


## Repository guide

- `notebooks/employee_voice_analysis.ipynb`: Organized Python analysis workflow.
- `scripts/check_outputs.py`: Data integrity verification script.
- `figures/`: Visualizations of workplace themes and negative sentiment.
- `final_theme_summary.csv`: Workplace theme frequencies and negative sentiment results.
- `source_comparison.csv`: Glassdoor and YouTube comparisons.
- `employment_comparison.csv`: Regular and part-time employee comparisons.
- `business_recommendations.csv`: Proposed operational improvements and success metrics.
- `requirements.txt`: Python dependencies.

Original employee review text and transcripts are excluded from the public repository.


## Reproduce

1. Create a Python environment and install dependencies: `pip install -r requirements.txt`.
2. Open the repository root as the working directory, then run `notebooks/employee_voice_analysis.ipynb` in order. In Colab, upload the repository files or mount Drive and set the working directory to the project root.
3. Run `python scripts/check_outputs.py` to inspect the included archived outputs.

Hugging Face model downloads require network access the first time. Model outputs may shift with package/model versions. This portfolio includes previous exported results for inspection; the notebook is an executable workflow, not a guarantee of byte-identical reproduction.

## Data use

Treat text as third-party public commentary, not verified employee statements. Confirm platform terms and permissions before republishing text publicly, and avoid exposing personal identifiers. The bundled source-text and transcript exports are for local project review. Review and remove them from a public GitHub upload if you lack redistribution permission. A public repository may instead include derived aggregate figures and code only.

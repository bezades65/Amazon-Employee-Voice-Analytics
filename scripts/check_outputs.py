"""Verify the included exported outputs have coherent structure."""
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
d = root / "data" / "processed"
combined = pd.read_csv(d / "combined_reviews.csv")
passages = pd.read_csv(d / "analysis_passages.csv")
evaluation = pd.read_csv(d / "sentiment_evaluation.csv")
summary = pd.read_csv(d / "final_theme_summary.csv")
assert len(combined) == 148
assert combined["record_id"].nunique() == 148
assert len(passages) == 739
assert len(evaluation) == 40 and evaluation["human_sentiment"].notna().all()
assert summary["records_with_negative"].le(summary["records_mentioning_theme"]).all()
print("Basic exported-data checks passed.")

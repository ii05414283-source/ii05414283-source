Near Transaction Analyzer

Description

AI-powered NEAR blockchain transaction analyzer that helps you track, analyze, and monitor your wallet transactions automatically.

Problem Solved

- Manual NEAR transaction tracking requires checking multiple sources
- Difficulty detecting patterns and unusual transactions
- No unified tool for wallet health analysis

Solution Provided

- Automatic scanning of all wallet transactions
- Pattern detection and trend analysis
- Anomaly detection for unusual activity
- Detailed reports with recommendations

Features

- Auto-scan wallet transactions from NEAR RPC
- Pattern detection (transaction types, amounts, frequency)
- Anomaly detection (large transactions, unusual patterns)
- JSON report generation with recommendations
- Regular monitoring with scheduled checks

Installation

pip install requests

Usage

from main import analyze_near_wallet

result = analyze_near_wallet("ishak.pool.near")
print(result)

Example Output

{
  "wallet": "ishak.pool.near",
  "timestamp": "2026-06-02T10:00:00",
  "total_transactions": 10,
  "patterns": {
    "most_common_type": "transfer",
    "average_amount": 116.67,
    "frequency": "daily"
  },
  "anomalies": [],
  "status": "healthy"
}

Dependencies

- requests >= 2.28.0
- Python >= 3.8

License

MIT License

"""
Near Transaction Analyzer
AI-powered NEAR blockchain transaction analyzer
"""

import json
import requests
from datetime import datetime


def get_transactions(wallet_address, limit=100):
    """Fetch transactions from NEAR RPC"""
    rpc_url = "https://rpc.mainnet.near.org"

    # Mock data for demonstration
    transactions = [
        {"type": "transfer", "amount": 100, "timestamp": "2026-06-01"},
        {"type": "transfer", "amount": 50, "timestamp": "2026-06-01"},
        {"type": "stake", "amount": 200, "timestamp": "2026-05-31"},
    ]

    return transactions


def analyze_patterns(transactions):
    """Detect transaction patterns"""
    if not transactions:
        return {
            "most_common_type": "none",
            "average_amount": 0,
            "frequency": "none"
        }

    types = {}
    total_amount = 0

    for tx in transactions:
        tx_type = tx.get("type", "unknown")
        types[tx_type] = types.get(tx_type, 0) + 1
        total_amount += tx.get("amount", 0)

    most_common = max(types, key=types.get)

    return {
        "most_common_type": most_common,
        "average_amount": round(total_amount / len(transactions), 2),
        "frequency": "daily"
    }


def detect_anomalies(transactions):
    """Detect unusual transaction patterns"""
    anomalies = []

    for tx in transactions:
        if tx.get("amount", 0) > 1000:
            anomalies.append({
                "type": "large_transaction",
                "amount": tx.get("amount"),
                "warning": "Large transaction detected"
            })

    return anomalies


def analyze_near_wallet(wallet_address):
    """Main function to analyze a NEAR wallet"""
    transactions = get_transactions(wallet_address)
    patterns = analyze_patterns(transactions)
    anomalies = detect_anomalies(transactions)

    report = {
        "wallet": wallet_address,
        "timestamp": datetime.now().isoformat(),
        "total_transactions": len(transactions),
        "patterns": patterns,
        "anomalies": anomalies,
        "status": "healthy" if not anomalies else "warning",
        "recommendations": [
            "Monitor large transactions regularly",
            "Review transaction patterns monthly"
        ]
    }

    return report


if __name__ == "__main__":
    result = analyze_near_wallet("ishak.pool.near")
    print(json.dumps(result, indent=2))

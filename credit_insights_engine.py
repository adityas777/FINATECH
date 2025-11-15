
import pandas as pd
import numpy as np
import os

def parse_transaction_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext != ".csv":
        raise ValueError("Please upload a CSV file exported from Paytm/PhonePe/GooglePay.")

    df = pd.read_csv(file_path)
    df.columns = [c.strip().title() for c in df.columns]

    expected = ["Date", "Transaction_Id", "Type", "Amount", "Status", "Description"]
    for col in expected:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}. Expected columns: {expected}")

    df["Amount"] = df["Amount"].replace("[₹,]", "", regex=True).astype(float)
    df = df[df["Status"].str.contains("Success", case=False, na=False)]

    return df

def compute_transaction_insights(df):
    total_txn = len(df)
    total_sent = df[df["Type"].str.contains("Send", case=False, na=False)]["Amount"].sum()
    total_received = df[df["Type"].str.contains("Receive", case=False, na=False)]["Amount"].sum()
    avg_txn = df["Amount"].mean()
    refund_rate = len(df[df["Type"].str.contains("Refund", case=False, na=False)]) / total_txn * 100

    peer_txn = len(df[df["Description"].str.contains("Friend|Transfer", case=False, na=False)])
    merchant_txn = total_txn - peer_txn
    peer_ratio = round((peer_txn / total_txn) * 100, 2)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_txn = df.groupby("Month")["Amount"].sum()
    txn_stability = max(0, 100 - (np.std(monthly_txn) / (np.mean(monthly_txn)+1)) * 100)

    cashflow_balance = total_received - total_sent
    cash_flow_score = min(100, 100 * (total_received / (total_sent + 1)))

    failure_rate = len(df[df["Status"].str.contains("Fail", case=False, na=False)]) / total_txn * 100 if "Fail" in df["Status"].values else 0
    payment_reliability = max(0, 100 - (refund_rate + failure_rate))

    spending_discipline = max(0, 100 - (np.std(df["Amount"]) / (np.mean(df["Amount"]) + 1)) * 100)
    digital_behavior = (0.5 * peer_ratio) + (0.5 * (100 - refund_rate))

    insights = {
        "Total Transactions": total_txn,
        "Total Sent (₹)": round(total_sent, 2),
        "Total Received (₹)": round(total_received, 2),
        "Average Transaction (₹)": round(avg_txn, 2),
        "Refund Rate (%)": round(refund_rate, 2),
        "Peer-to-Peer Ratio (%)": peer_ratio,
        "Cashflow Balance (₹)": round(cashflow_balance, 2),
        "Transaction Stability Score": round(txn_stability, 2),
        "Cash Flow Score": round(cash_flow_score, 2),
        "Payment Reliability Score": round(payment_reliability, 2),
        "Spending Discipline Score": round(spending_discipline, 2),
        "Digital Behavior Score": round(digital_behavior, 2)
    }

    return insights

def calculate_credit_score(metrics):
    TCS = metrics["Transaction Stability Score"]
    CF = metrics["Cash Flow Score"]
    PR = metrics["Payment Reliability Score"]
    SD = metrics["Spending Discipline Score"]
    DB = metrics["Digital Behavior Score"]

    score = 9 * (0.25*TCS + 0.2*CF + 0.2*PR + 0.15*SD + 0.2*DB)
    score = int(min(900, max(300, score)))

    explanations = []
    if CF > 80: explanations.append("✅ Positive cashflow – you receive more than you spend.")
    else: explanations.append("⚠️ Spending exceeds inflows – try saving more monthly.")

    if PR > 85: explanations.append("✅ Reliable transactions – very few refunds or failures.")
    else: explanations.append("⚠️ Multiple failed or refunded transactions detected.")

    if SD > 75: explanations.append("✅ Consistent spending pattern.")
    else: explanations.append("⚠️ High variance in transaction amounts – spending spikes observed.")

    if DB > 70: explanations.append("✅ Strong digital activity and peer usage.")
    else: explanations.append("⚠️ Low digital peer engagement detected.")

    return score, explanations

def save_to_excel(df, insights, score, explanations):
    output_excel = "transaction_insights.xlsx"
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Raw Data", index=False)
        pd.DataFrame(list(insights.items()), columns=["Metric", "Value"]).to_excel(writer, sheet_name="Insights", index=False)
        summary = pd.DataFrame({
            "Digital Credit Score (0–900)": [score],
            "Interpretation": ["Excellent" if score>=750 else "Good" if score>=650 else "Fair" if score>=550 else "Poor"]
        })
        summary.to_excel(writer, sheet_name="Credit Score", index=False)
        pd.DataFrame({"Explanation": explanations}).to_excel(writer, sheet_name="XAI_Insights", index=False)
    print("\n✅ Insights and Credit Score saved to 'transaction_insights.xlsx'\n")

if __name__ == "__main__":
    print("🔹 Digital Credit Insights Engine")
    file_path = input("Enter your UPI transaction CSV file path: ").strip()

    df = parse_transaction_file(file_path)
    insights = compute_transaction_insights(df)
    score, explanations = calculate_credit_score(insights)

    print("\n📊 --- FINANCIAL INSIGHTS ---")
    for k, v in insights.items():
        print(f"{k}: {v}")

    print(f"\n💳 Digital Credit Score: {score} / 900")
    print("\n🧠 Explanation:")
    for e in explanations:
        print(" -", e)

    save_to_excel(df, insights, score, explanations)

import psycopg2          # Library to connect Python to PostgreSQL
import random             # To randomly pick values from lists
from datetime import datetime, timedelta  # To generate spread-out dates

# ──────────────────────────────────────────────
# 1. DATABASE CONNECTION
# ──────────────────────────────────────────────
# These are the same credentials you use in psql
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="support_analytics",
    user="support_user",
    password="support_password"   # change this if yours is different
)

# A cursor is how Python sends SQL commands to the database
cursor = conn.cursor()

# ──────────────────────────────────────────────
# 2. REALISTIC DATA POOLS
# ────────────────────────────────────────────so──
# These lists mirror exactly what your AI returns

categories = [
    "Billing",
    "Claims",
    "Policy Change",
    "Technical Issue",
    "Account Access",
    "General Inquiry"
]

priorities = ["High", "Medium", "Low"]

sentiments = ["Positive", "Neutral", "Negative"]

# Routing logic matches your n8n workflow
team_map = {
    "Billing":          "Billing Team",
    "Claims":           "Claims Team",
    "Policy Change":    "Policy Team",
    "Technical Issue":  "Technical Support Team",
    "Account Access":   "Account Support Team",
    "General Inquiry":  "General Support Team"
}

# Fake customer names and emails for realistic data
customers = [
    ("Alice Johnson",   "alice.johnson@email.com"),
    ("Bob Smith",       "bob.smith@email.com"),
    ("Carol White",     "carol.white@email.com"),
    ("David Brown",     "david.brown@email.com"),
    ("Emma Davis",      "emma.davis@email.com"),
    ("Frank Miller",    "frank.miller@email.com"),
    ("Grace Wilson",    "grace.wilson@email.com"),
    ("Henry Moore",     "henry.moore@email.com"),
    ("Isabel Taylor",   "isabel.taylor@email.com"),
    ("James Anderson",  "james.anderson@email.com"),
]

summaries = [
    "Customer is experiencing login issues and cannot access their account.",
    "Customer is disputing a charge on their latest invoice.",
    "Customer wants to upgrade their current policy plan.",
    "Customer reported a system error when submitting a claim form.",
    "Customer forgot their password and needs account recovery.",
    "Customer is asking about coverage details for their plan.",
    "Customer received an incorrect bill amount this month.",
    "Customer wants to add a dependent to their existing policy.",
    "Customer is unable to download their policy documents.",
    "Customer is requesting a refund for a cancelled service.",
]

# ──────────────────────────────────────────────
# 3. GENERATE AND INSERT 100 TICKETS
# ──────────────────────────────────────────────
# range(100) means: repeat this block 100 times (i goes from 0 to 99)
for i in range(100):

    # Pick random values from our pools above
    category  = random.choice(categories)
    priority  = random.choice(priorities)
    sentiment = random.choice(sentiments)
    customer  = random.choice(customers)
    summary   = random.choice(summaries)

    customer_name  = customer[0]   # First item in the tuple
    customer_email = customer[1]   # Second item in the tuple

    # Look up the assigned team based on category (same as your n8n routing logic)
    assigned_team = team_map[category]

    # Escalation rule: High priority = escalated (same as your n8n logic)
    escalated = priority == "High"   # This returns True or False

    # Spread tickets across the last 30 days so charts show trends over time
    # random.randint(0, 30) picks a random number between 0 and 30
    days_ago   = random.randint(0, 30)
    created_at = datetime.now() - timedelta(days=days_ago)

    # Fake Zendesk ticket ID (starts at 1000 + row number)
    zendesk_ticket_id = 1000 + i

    # ── INSERT SQL ──
    # %s are placeholders — psycopg2 safely fills them in (prevents SQL injection)
    cursor.execute("""
        INSERT INTO support_tickets (
            zendesk_ticket_id,
            customer_name,
            customer_email,
            category,
            priority,
            sentiment,
            assigned_team,
            escalated,
            summary,
            created_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        zendesk_ticket_id,
        customer_name,
        customer_email,
        category,
        priority,
        sentiment,
        assigned_team,
        escalated,
        summary,
        created_at
    ))

# ──────────────────────────────────────────────
# 4. SAVE AND CLOSE
# ──────────────────────────────────────────────
# commit() saves all inserts to the database (like pressing Save)
# Without this, nothing is actually saved
conn.commit()

print("✅ 100 tickets inserted successfully.")

# Always close your cursor and connection when done
cursor.close()
conn.close()
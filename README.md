# AI Customer Support Automation

AI-powered customer support automation platform built using:

- n8n
- OpenAI API
- Zendesk
- Docker

## Overview

This project demonstrates an end-to-end AI-driven customer support workflow designed to automate ticket triage, routing, and escalation processes. The system analyzes incoming support requests using OpenAI, enriches tickets with structured metadata, and automatically creates tickets in Zendesk for the appropriate support teams.

## Features

- AI-powered ticket classification
- Priority detection
- Sentiment analysis
- AI-generated response drafts
- Automated team assignment
- Dynamic ticket routing
- Zendesk ticket creation
- Escalation detection for high-priority tickets
- Structured JSON-based workflow processing
- Webhook-based integrations

## Workflow

1. Customer submits a support request via a contact form.
2. A webhook triggers an n8n workflow.
3. OpenAI analyzes the ticket content.
4. AI determines:
   - Category
   - Priority
   - Sentiment
   - Ticket summary
   - Suggested customer response
5. The workflow parses the AI response into structured JSON.
6. Tickets are routed to the appropriate support team:
   - Billing Team
   - Claims Team
   - Policy Team
   - Technical Support Team
   - Account Support Team
   - Customer Service Team
7. Zendesk automatically creates a support ticket with AI-generated insights.
8. High-priority tickets are flagged for escalation.
9. Support agents receive enriched tickets containing AI-generated summaries and recommended responses.

## Architecture

<p align="center">
  <img src="images/architecture.png" alt="Architecture Diagram" width="600"/>
</p>

## Example AI Output

```json
{
  "category": "Account Access",
  "priority": "High",
  "sentiment": "Negative",
  "summary": "Customer is locked out of their account and needs urgent access.",
  "draft_reply": "We understand your concern and will assist you as quickly as possible."
}
```

## Technologies Used

- OpenAI API
- Zendesk API
- n8n Workflow Automation
- REST APIs
- Webhooks
- JSON Processing
- Docker

## Project Architecture

```text
Customer Support Form
          │
          ▼
       Webhook
          │
          ▼
   OpenAI Analysis
          │
          ▼
 JSON Response Parsing
          │
          ▼
 Ticket Classification
          │
          ▼
 Team Assignment
          │
          ▼
 Zendesk Ticket Creation
          │
          ▼
 Escalation Detection
          │
          ▼
 Email Notifications (Upcoming)
```

## Future Enhancements

- Automated email notifications for escalated tickets
- PostgreSQL analytics and reporting
- SLA monitoring and tracking
- Dashboard for operational metrics
- Multi-channel support integrations (Email, Chat, CRM)
- AI-powered knowledge base suggestions

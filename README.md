# AI Customer Support Automation

AI-powered customer support automation platform built using:

- n8n
- OpenAI
- Zendesk
- Docker

## Features

- Ticket classification
- Priority detection
- Sentiment analysis
- AI-generated response drafts
- Automated routing

## Architecture

<p align="center">
  <img src="images/architecture.png" alt="Architecture Diagram" width="900"/>
</p>

### Workflow

1. Customer creates a ticket in Zendesk
2. Zendesk triggers an n8n workflow
3. n8n sends ticket content to OpenAI
4. OpenAI analyzes sentiment, intent, and priority
5. AI generates a suggested response
6. n8n updates the ticket and routes it to the appropriate team

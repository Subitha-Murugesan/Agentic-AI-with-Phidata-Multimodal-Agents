# Agentic-AI-with-Phidata - Multimodal-Agents
This project demonstrates an Agentic AI system using Phidata, where multiple autonomous multimodal agents collaborate to handle complex analytical tasks. Each agent is powered by a Groq LLM and specialized tools like YFinance and Google Search, enabling intelligent information retrieval, analysis, and summarization.

The system is designed to:
  Retrieve real-time financial data
  Extract latest news insights 
  Combine multi-source information via LLM reasoning 
  Provide stock recommendations and summarized insights

## Components

## 1. Finance Agent:

Purpose: Analyze market data and analyst recommendations

Tool: YFinanceTools

Model: Groq (meta-llama/llama-4-scout-17b-16e-instruct)

Output: Tabular stock insights

## 2. News Agent:

Purpose: Fetch and summarize latest news

Tool: GoogleSearch / DuckDuckGo

Model: Groq (meta-llama/llama-4-scout-17b-16e-instruct)

Output: 4 unique news articles with summaries

## Multimodal Coordinator Agent:

Combines Finance and News Agent outputs into one unified response

## User Query:

“Summarize analyst recommendations and share the latest news of AAPL.”

## Process:

News Agent fetches recent Apple-related news

Finance Agent gathers stock data and analyst ratings

Coordinator Agent fuses both results into a clear, contextual summary

## Final Output Includes:

Analyst recommendation table (Buy/Hold/Sell)

4 latest news headlines with sources

Final LLM-generated summary and recommendation

<img width="976" height="526" alt="image" src="https://github.com/user-attachments/assets/13d69f79-6294-45fd-95d7-8732551433c1" />
<img width="976" height="426" alt="image" src="https://github.com/user-attachments/assets/ab338ddb-93c2-49d0-8bf5-800138383139" />

| Tool                      | Purpose                                      |
| ------------------------- | -------------------------------------------- |
| Phidata                   | Agentic AI orchestration framework           |
| Groq (Meta LLaMA 4 Scout) | LLM backbone for reasoning and summarization |
| GoogleSearch / DuckDuckGo | Real-time web data retrieval                 |
| YFinanceTools             | Financial data and stock insights            |    



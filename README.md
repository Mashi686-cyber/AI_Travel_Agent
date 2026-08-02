# 🇱🇰 Ceylon AI Travel Assistant

## AI Based Sri Lanka Travel Planning Application

Ceylon AI Travel Assistant is a web application that helps users create personalized travel plans for Sri Lanka.

Users can enter details such as destination, number of days, budget, travel type, interests, number of travelers, and transport preference. The system uses AI agents to generate a suitable travel plan with recommended hotels, restaurants, activities, transport options, and budget advice.

This project was developed using Agentic AI concepts with LangGraph, RAG, and Groq LLM.

---

## Project Features

- Create personalized travel plans
- Recommend hotels based on selected destinations
- Suggest restaurants and local foods
- Recommend activities based on user interests
- Provide transport details
- Check whether the selected budget is suitable
- Retrieve travel information from a knowledge base

---

## Technologies Used

- Python
- Streamlit
- LangGraph
- LangChain
- Groq LLM
- Retrieval Augmented Generation (RAG)
- ChromaDB

---

## System Workflow

The application uses multiple AI agents to generate the final travel plan.

User Input
↓
Profile Agent
↓
LangGraph Workflow
↓
Destination Agent
Hotel Agent
Restaurant Agent
Activity Agent
Transport Agent
↓
Planner Agent
↓
Final Travel Plan


---

## AI Agents Description

### Destination Agent

Provides information about the selected travel destination.

### Hotel Agent

Provides suitable hotel recommendations according to the destination.

### Restaurant Agent

Suggests restaurants and local food options.

### Activity Agent

Recommends activities and attractions based on user interests.

### Transport Agent

Provides transport routes and travel information.

### Planner Agent

Combines all information from other agents and creates the final itinerary.

---

## Project Structure

```
AI_Travel_Agent

├── agents
│ ├── destination_agent.py
│ ├── hotel_agent.py
│ ├── restaurant_agent.py
│ ├── activity_agent.py
│ ├── transport_agent.py
│ └── planner_agent.py
│
├── tools
│ └── rag_pipeline.py
│
├── data
│ └── sri_lanka_knowledge.txt
│
├── assets
│ ├── background.jpg
│ └── destination images
│
├── graph.py
├── app.py
├── main.py
└── requirements.txt

```
## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/Mashi686-cyber/AI_Travel_Agent.git
```

## 2. Navigate to Project Folder
```
cd AI_Travel_Agent
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```


## 4. Add API Key
Create a .env file in the project folder.
```env
GROQ_API_KEY=your_api_key
```

## 5. Run Application
```bash
streamlit run app.py
```


## Live Application
Streamlit URL:
https://aitravelagent-wdwp-c8zfuhrrozqequ44pv.streamlit.app


## Example
### User Input
Destination: Ella
Duration: 2 Days
Budget: LKR 50000
Travel Type: Solo
Interest: Adventure
Transport Preference: Train

### Generated Output
The system generates:
- Daily travel itinerary
- Hotel recommendations
- Restaurant suggestions
- Local food recommendations
- Activities
- Transport plan
- Budget advice


## AI and RAG Implementation
The application uses Retrieval Augmented Generation (RAG) to retrieve relevant Sri Lanka travel information from a knowledge base.
The retrieved information is provided to AI agents, and the Planner Agent generates the final personalized travel plan.

## Deployment
The application is deployed using Streamlit Cloud.

Live Demo:
https://aitravelagent-wdwp-c8zfuhrrozqequ44pv.streamlit.app

## Developer
Mashi686-cyber
---

## Purpose
This project was developed as an academic project to demonstrate the use of Agentic AI, RAG, and Large Language Models for travel planning.

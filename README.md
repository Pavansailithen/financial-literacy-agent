# 🤖 AI Agent for Digital Financial Literacy

This project is an AI-powered agent designed to improve digital financial literacy, built for the "AI for Good" challenge. It helps users understand essential financial tools and practices in a safe, accessible, and inclusive way.

## 🎯 Problem Statement

The agent addresses the challenge of providing reliable and accessible financial information to a diverse population. It aims to empower users with knowledge about digital finance, protect them from fraud, and build their confidence in using tools like UPI.

## ✨ Key Features

-   **Retrieval-Augmented Generation (RAG):** The agent uses a RAG pipeline to provide answers grounded in a reliable knowledge base, preventing misinformation.
-   **Authoritative Knowledge Base:** The agent's knowledge comes exclusively from trusted sources like government portals (RBI, NPCI), major banking websites, and educational platforms.
-   **Multilingual Support:** Users can interact with the agent in their preferred language, ensuring cultural and linguistic inclusivity.
-   **Core Topics Covered:** UPI usage, avoiding online scams, understanding interest rates, budgeting, and personal finance management.
-   **Powered by IBM Cloud:** The entire backend is built and deployed on IBM Cloud, using Watsonx.ai and the Granite foundation model.

## 🏛️ Architecture

The agent is built on a two-phase RAG architecture running on IBM Cloud:

1.  **Knowledge Ingestion (Offline):**
    -   **Data Sourcing:** Python scripts scrape content from trusted financial websites.
    -   **Chunking & Embedding:** The scraped text is cleaned and split into small chunks. Each chunk is converted into a vector embedding using an IBM embedding model on Watsonx.ai.
    -   **Vector Storage:** The embeddings are stored in a vector index, which is managed within the IBM Cloud environment.

2.  **User Interaction (Real-time):**
    -   A user asks a question (e.g., "How do I use UPI?").
    -   The user's question is converted into an embedding.
    -   A similarity search retrieves the most relevant text chunks from the vector store.
    -   The retrieved chunks and the original question are passed as context to the **IBM Granite LLM**.
    -   The Granite model generates a safe, fact-based answer based *only* on the provided context.


## 🛠️ Technology Stack

-   **Cloud Platform:** IBM Cloud
-   **AI/LLM Service:** IBM Watsonx.ai
-   **Foundation Model:** IBM Granite
-   **Compute:** IBM Code Engine
-   **Client:** Python (`requests` library)

## 🚀 How to Run This Project

This repository contains the Python client to interact with the deployed agent.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/financial-literacy-agent.git](https://github.com/YOUR_USERNAME/financial-literacy-agent.git)
    cd financial-literacy-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

3.  **Set Environment Variables:**
    You need to set your IBM Cloud API Key. It's recommended to do this as an environment variable for security. You also need to add the agent's endpoint URL in the `app.py` script.

4.  **Run the client:**
    ```bash
    python app.py
    ````

### **Step 5: Upload Your Project to GitHub**

Now, you'll use the Git commands to upload the two files (`app.py` and `README.md`) from your computer to your GitHub repository.

Open a terminal or command prompt inside your `financial-literacy-agent` folder and run these commands one by one:

```bash
# 1. Initialize a new Git repository in your folder
git init

# 2. Add all the files in the folder to be tracked by Git
git add .

# 3. Commit the files with a descriptive message
git commit -m "Initial commit: Create financial literacy agent client and README"

# 4. Rename the default branch to 'main' (a modern standard)
git branch -M main

# 5. Connect your local folder to the GitHub repository you created
# (Copy the URL from your GitHub repository page)
git remote add origin [https://github.com/YOUR_USERNAME/financial-literacy-agent.git](https://github.com/YOUR_USERNAME/financial-literacy-agent.git)

# 6. Push your local files up to GitHub
git push -u origin main
```

**That's it!** If you refresh your GitHub repository page, you will see your `app.py` and `README.md` files. You now have a professional, well-documented project that you can share with your internship manager and add to your resume.

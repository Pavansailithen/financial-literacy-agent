import requests
import os
import json

# --- Configuration ---
# It's best practice to get your API key from an environment variable
# instead of writing it directly in the code.
IBM_API_KEY = os.getenv("IBM_API_KEY", "cpd-apikey-IBMid-697001123I") 
IAM_URL = "https://iam.cloud.ibm.com/identity/token"
# This is the "Endpoint for inferencing" from Step 48 of your PDF.
AGENT_API_URL = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ecdfb112-a168-46fc-a29a-768cd9e03d1e/ai_service?version=2021-05-01"

def get_iam_token(api_key):
    """Gets an IAM token from IBM Cloud."""
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"
    
    try:
        response = requests.post(IAM_URL, headers=headers, data=data)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        print(f"Error getting IAM token: {e}")
        return None

def ask_agent(token, agent_url, question):
    """Sends a question to the deployed AI agent and gets a response."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": question
    }
    
    try:
        response = requests.post(agent_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("output", "Sorry, I couldn't get a response.")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with agent: {e}")
        return "An error occurred."

def main():
    """Main function to run the financial literacy agent chat."""
    print("🤖 Welcome to the Digital Financial Literacy AI Agent!")
    print("   Ask questions about UPI, scams, interest rates, and more.")
    print("   Type 'exit' to quit.")

    print("\nAuthenticating with IBM Cloud...")
    iam_token = get_iam_token(IBM_API_KEY)
    
    if not iam_token:
        print("Could not authenticate. Please check your API key.")
        return
        
    print("Authentication successful!")

    while True:
        user_question = input("\nYou: ")
        if user_question.lower() == 'exit':
            print("Goodbye! Stay financially savvy!")
            break
        
        agent_response = ask_agent(iam_token, AGENT_API_URL, user_question)
        print(f"\nAgent: {agent_response}")

if __name__ == "__main__":
    main()
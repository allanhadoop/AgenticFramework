                                  The UI (Gradio)
                                      |
                Agent Framework (with memory and logging)
                                      |
                               Planning Agent 
                                      |
                ---------------------------------------------
                |                     |                     |
        Scanner agent           Ensemble agent           Msg agent 
      (identify deals)        (estimate price       Send push notifications
                           using multiple models)
                                      |
                     ------------------------------------ 
                     |                |                 |
              Frontier Agent    Specialized Agent       Neural Network Agent
              (RAG pricer)       (Estimate price)       (Estimate price)

# MODAL.COM is to deploy LLMs. for inference . Modal.com is basically an AI-focused cloud platform that lets you run GPU-heavy Python/LLM workloads without managing servers

>> Get MODAL.COM API token from their site and also add hugging face HF_TOKEN under secrets on MODAL.COM

>> Before using Ensemble model for reducing error rate for prediction, we tried all of below models and methods and their error rates given . Check result.py for more details 
    ("Constant", "gray", 106.18),
    ("Linear Regression", "gray", 101.56),
    ("NLP + LR", "gray", 76.81),
    ("Random Forest", "gray", 72.28),
    ("XGBoost", "gray", 68.23),
    ("Human (Ed)", "black", 87.62),
    ("Neural Network", "orange", 63.97),
    ("GPT 4.1 Nano", "slateblue", 62.51),
    ("Grok 4.1 Fast", "slateblue", 57.62),
    ("Gemini 3 Pro", "slateblue", 50.54),
    ("Claude 4.5 Sonnet", "slateblue", 47.10),
    ("GPT 5.1", "slateblue", 44.74),
    ("GPT 4.1 Nano (Fine-tuned)", "skyblue", 75.91),
    ("Deep Neural Network", "orange", 46.49),
    ("Base Llama 3.2 4 bit", "darkred", 110.72),
    ("Fine-tuned Lite", "red", 65.40),
    ("Fine-tuned Full", "red", 39.85),
    ("GPT 5.1 RAG", "green", 30.19),
    ("Ensemble", "purple", 29.9)                  <---------------------Best one among all models ---------------->



#---------------Structured Output --------------------------------------

When LLM responds we can take that typical natual language response and convert into a object as below and structure it
1. We define a Python class as a subclass of Pydantic BaseModel (JSON schema)
2. The model outputs an instance of this class
3. OpenAI includes the JSON schema in the system prompt - "You must respond with JSON according to this schema"
4. OpenAI client library creates an instance of the Pydantic class and populates with the JSON
5. Inference time constrained decoding = OpenAI always make sure the probablity of next token is always comply with the JSON schema


#------------------The hallmarks of an Agentic AI Solution ------------------------------
1. Breaking a larger problem into smaller steps carried out by indiviual processes/models
2. Using tools.function calls.structured output 
3. An agent environment in which Agents can collaborate 
4. A planning agent that cordinates activities
5. Autonomy and Memory - Existing beyond a chat with a human


Finally Run the App - The price is right -- 

!uv run price_is_right.py
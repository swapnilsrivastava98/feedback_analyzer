from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config import llm

prompt = ChatPromptTemplate.from_messages([
("system", """You are an AI assistant that analyzes customer feedback.
Analyze the message and respond ONLY with a valid JSON object with these exact fields:
{{
    "summary": "Brief 1-2 sentence summary of the message",
    "sentiment": <integer from 0 (very negative) to 10 (very positive)>,
    "category": "One of: complaint, inquiry, compliment, suggestion",
    "response": "A professional suggested response to this customer based on the sentiment and category"
}}
Return ONLY the JSON object. 
Do NOT use markdown. 
Do NOT use code blocks. 
Do NOT use backticks.
"""),
    ("human", "{user_message}")
])

parser = JsonOutputParser()

chain = prompt | llm | parser

def analyze_feedback(user_message: str) -> dict:
    result = chain.invoke({"user_message": user_message})
    return result
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from load_env import load_env_file
from llm_factory import LLMFactory

load_env_file()

example_prompt = PromptTemplate.from_template("Pregunta: {question}\nRespuesta: {answer}")
prompt = example_prompt.invoke({"question": "What is the capital of France?", "answer": "Paris"})
print("Example prompt:")
print(prompt.text)


examples = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
]

prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Pregunta: {input}",
    input_variables=["input"],
)
prompt = prompt_template.invoke({"input": "¿Cuál es la capital de Francia?"})
print("Few shot prompt:")
print(prompt.text)


llm = LLMFactory.create_llm(
    provider="gemini",
    model="gemini-2.5-flash",
    temperature=0.7,
)

llm_chain = prompt_template | llm
response = llm_chain.invoke({"input": "¿Cuál es la capital de Francia?"})
print("Response:")
print(response.content)

# Codigos de ejemplos
# Create the examples list of dicts
examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]
# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)
llm = LLMFactory.create_llm(
    provider="gemini",
    model="gemini-2.5-flash",
    temperature=0.7,
)
# Create and invoke the chain
llm_chain = prompt_template | llm
response = llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp, based on his completed courses?"})
print("Response llm_chain:")
print(response.content)

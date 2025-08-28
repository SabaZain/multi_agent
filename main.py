from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled
from my_tools.tools import get_weather,add,subtract,multiply

set_tracing_disabled(True)

key=config("GEMINI-API-KEY")
#print(key)

client=AsyncOpenAI(api_key=key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)

agent:Agent=Agent(
    name="Multi Agent Tool",
    instructions="You are a helpful multi agent.Use tool when needed.",
    model=model,
    tools=[get_weather,add,subtract,multiply]
)

print("Welcome to Multi agent tools!")
user_input=input("Ask your question? ")
result=Runner.run_sync(starting_agent=agent, input=user_input)
print("Answer: ", result.final_output)
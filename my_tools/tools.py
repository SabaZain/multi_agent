from agents import function_tool

@function_tool
async def get_weather(city:str)->str:
    """Return mock weather temperature for the given city."""
    mocked_temperature = {
        "Karachi": 32,
        "Islamabad": 29,
        "Lahore": 38,
        "China": 22,
        "Oman": 40,
        "Sydney": 18
    }
    temperature = mocked_temperature.get(city)
    
    if temperature:
        return f"The temperature in {city} is {temperature} degree celcius."
    else:
        return f"Sorry, I Dont have weather data for {city}."
    
@function_tool
async def add(a:int,b:int)->str:
    """Add two numbers"""
    return a + b
@function_tool
async def subtract(a:int,b:int)->str:
    """Subtract two numbers"""
    return a - b
@function_tool
async def multiply(a:int,b:int)->str:
    """Multiply two numbers"""
    return a * b
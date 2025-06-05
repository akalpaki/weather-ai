# weather-ai

Experimenting with creation of AI agents using python and Langchain/Langgraph.
Goal of this agent is to accept a location as input and provide a short weather forecast.

### Setup
This project uses Python version 3.10.17.

This agent assumes you're using `Ollama` with `llama3.2:3b` model.
More info on setting up and working with `Ollama` can be found [here](https://ollama.com/).

The agent uses Tavilly search for querying the internet for weather data,
so it required that you set up an account [here](https://www.tavily.com/) and provide a `.env`
file with the environment variable `TAVILLY_API_KEY`.

### Dependencies

- [langchain](https://github.com/langchain-ai/langchain)
- langchain-ollama
- [langchain-community](https://github.com/langchain-ai/langchain-community)
- [tavily-python](https://github.com/tavily-ai/tavily-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

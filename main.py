from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage

from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

from src.agent import WeatherReporter

load_dotenv()


def main() -> None:
    agent = WeatherReporter()
    agent.report_weather("Thessaloniki")


if __name__ == "__main__":
    main()

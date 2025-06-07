from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from src.cache import Cache
from src.city_picker import pick_random_city


class WeatherReporter:
    _config: RunnableConfig = {
        "configurable": {"thread_id": "123"},
    }

    _prompt_template: str = """
        You are a weather forecaster. Your job is to provide
        weather forecasts in an informative and concise manner.
        Here is an example you can use as a reference for how you
        can format your response:

        "report": 'The weather in Athens today is X degrees Celsius (Y degrees Farenheit),
        with clear sky. A perfect day for a picnic!',
        "location": (the location the user provided or the one chosen at random via the pick_random_city tool)

        Do not use the example exactly, but mimic its style. In the actual response, use "report" and "location"
        as fields of a JSON object you will provide.
        Give me the weather report for {location}. If the user does not provide a location, choose a random one using
        pick_random_city.
        """

    def __init__(self) -> None:
        self._tools = [
            TavilySearchResults(max_results=1),
            pick_random_city,
        ]
        self._model: ChatOllama = ChatOllama(model="llama3.2:3b")
        self._agent: CompiledGraph = create_react_agent(
            model=self._model,
            tools=self._tools,
        )
        self._cache: Cache = Cache()

    def report_weather(self, location: str | None = None) -> str:
        location = location if location is not None else "None"

        if location is not None:
            cached_response = self._cache.get(location)
            if cached_response:
                return cached_response.report

        raw_result = self._agent.invoke(
            input={
                "messages": [
                    HumanMessage(
                        content=self._prompt_template.format(location=location),
                    )
                ],
            },
            config=self._config,
            stream_mode="values",
        )
        result: str = raw_result["messages"][-1].content

        # self._cache.set(
        #     location=result.location,
        #     result=result.report,
        #     ttl=None,
        # )

        return result

import typer
from dotenv import load_dotenv
from typing_extensions import Annotated

from src.agent import WeatherReporter

_ = load_dotenv()


def main(location: Annotated[str | None, typer.Argument()] = None) -> None:
    agent = WeatherReporter()
    res = agent.report_weather(location)
    print(res)


if __name__ == "__main__":
    typer.run(main)

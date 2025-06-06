import typer
from dotenv import load_dotenv

from src.agent import WeatherReporter

_ = load_dotenv()


def main(location: str) -> None:
    agent = WeatherReporter()
    res = agent.report_weather(location)
    print(res)


if __name__ == "__main__":
    typer.run(main)

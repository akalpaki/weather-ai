from dotenv import load_dotenv

from src.agent import WeatherReporter

_ = load_dotenv()


def main() -> None:
    agent = WeatherReporter()
    res = agent.report_weather("Thessaloniki")
    print(res)


if __name__ == "__main__":
    main()

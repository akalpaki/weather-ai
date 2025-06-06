from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import shelve

DEFAULT_TTL = 3600  # one hour
DEFAULT_PATH = "weather.cache"


@dataclass
class Report:
    location: str
    report: str
    created_at: datetime
    ttl: int = DEFAULT_TTL

    @property
    def expires_at(self):
        return self.created_at + timedelta(seconds=self.ttl)

    @property
    def is_expired(self):
        return datetime.now(timezone.utc) > self.expires_at


class Cache:
    """
    A shelve based cache used to store key-value pairs
    of location to weather report with a ttl of one hour.
    """

    def __init__(self, cache_path: str | None = None):
        self._path: str = cache_path or DEFAULT_PATH

    def set(self, location: str, result: str, ttl: int | None):
        with shelve.open(self._path) as cache:
            report = Report(
                location=location,
                report=result,
                created_at=datetime.now(timezone.utc),
                ttl=ttl or DEFAULT_TTL,
            )
            cache[location] = report

    def get(self, location: str) -> Report | None:
        with shelve.open(self._path) as cache:
            if location not in cache:
                return None

            report: Report = cache[location]

            if report.is_expired:
                del cache[location]
                return None

            return report

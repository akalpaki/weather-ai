@dataclass
class Report:
    location: str
    report: str
    ttt: int  # ttl in minutes


class Cache:
    # TODO: provide configuration option for cache file path
    _path = "s"

    def __init__(self) -> None:
        # TODO: implement me!
        pass

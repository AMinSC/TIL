class Event:
    def __init__(self, row_data):
        self.row_data = row_data

        @staticmethod
        def meets_condition(event_data: dict) -> bool:
            return False


class UnknownEvent(Event):
    """데이터만으로 식별할 수 없는 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict):
        return "데이터만으로 식별할 수 없는 이벤트"


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )


class SystemMonitor:
    """시스템에서 발생한 이벤트 분류"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue

        return UnknownEvent(self.event_data)


class TransactionEvent(Event):
    """시스템에서 발생한 트랜잭션 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["after"].get("transaction") is not None


if __name__ == "__main__":
    eleven = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    eleven.identify_event().__class__.__name__

    twelve = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    twelve.identify_event().__class__.__name__

    thirteen = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    thirteen.identify_event().__class__.__name__

    fourteen = SystemMonitor({"after": {"transaction": "Tx001"}})
    fourteen.identify_event().__class__.__name__


class Event:
    _controller = None
    _types = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.type_ in Event._types:
            Event._types[cls.type_].append(cls())
        else:
            Event._types[cls.type_] = [cls()]


class EventController:
    def __init__(self, window):
        self.window = window
        Event._controller = self
        self.event_handlers = Event._types

    def distribute(self, event):
        type_ = event.type
        if type_ not in self.event_handlers:
            return None
        for handler in self.event_handlers[type_]:
            handler(**event.__dict__)
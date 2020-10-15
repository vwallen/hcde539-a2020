import time

# Handler wraps a function and internally tracks
# the time since the wrapped function was last called.
# If enough time has passed since the last call, it will
# call the wrapped function. This allows event handlers
# to each sample at a different rate
class Handler:

    def __init__(self, cpx, function, interval):
        self.cpx = cpx
        self.function = function
        self.interval = interval
        self.deltatime = 0

    def __call__(self, deltatime):
        dt = self.deltatime + deltatime
        if dt < self.interval:
            self.deltatime = dt
        else:
            self.deltatime = 0
            self.function(self.cpx)


# Dispatcher abstracts some of the state handling associated
# with the board controls, and defines ways to register event
# handlers to respond to changes. Handlers can be registered
# to respond at different intervals.
class Dispatcher:

    UPDATE = 'update'
    CLICK_A = 'click_a'
    CLICK_B = 'click_b'
    SWITCH_ON = 'switch_on'
    SWITCH_OFF = 'switch_off'

    def __init__(self, cpx):
        self._cpx = cpx
        self._handlers = dict()
        self._button_a_down = False
        self._button_b_down = False
        self._switch_on = None

    def _dispatch(self, event, deltatime):
        handlers = self._handlers.get(event, [])
        for handler in handlers:
            handler(deltatime)

    def _update(self, deltatime):

        # Check for button A click event
        if self._cpx.button_a:
            self._button_a_down = True
        else:
            if self._button_a_down:
                self._dispatch(Dispatcher.CLICK_A, deltatime)
            self._button_a_down = False

        # Check for button B click event
        if self._cpx.button_b:
            self._button_b_down = True
        else:
            if self._button_b_down:
                self._dispatch(Dispatcher.CLICK_B, deltatime)
            self._button_b_down = False

        # Check for switch change events
        # Dispatch on start for starting position
        if self._cpx.switch:
            if not self._switch_on:
                self._dispatch(Dispatcher.SWITCH_ON, deltatime)
            self._switch_on = True
        else:
            # _switch_on is initialized with None to allow this
            # to trigger in cases where the device boots in the
            # switch "off" position
            if self._switch_on or self._switch_on is None:
                self._dispatch(Dispatcher.SWITCH_OFF, deltatime)
            self._switch_on = False

        # Dispatch the update event every tick
        self._dispatch(Dispatcher.UPDATE, deltatime)

    def register(self, event, function, interval = 0):
        self.unregister(event, function)
        handlers = self._handlers.get(event, [])
        handlers.append(Handler(self._cpx, function, interval))
        self._handlers[event] = handlers

    def unregister(self, event, function):
        handlers = self._handlers.get(event, [])
        for i, handler in enumerate(handlers):
            if handler.function == function:
               handlers.remove(handler)

    def unregisterAll(self, *args):
        keys = args if (len(args) > 0) else self._handlers.keys()
        for k in keys:
            self._handlers[k] = []

    def start(self, interval=0):
        tick = time.monotonic() * 1000
        while True:
            tock = time.monotonic() * 1000
            self._update(tock - tick)
            tick = tock
            time.sleep(interval/1000)
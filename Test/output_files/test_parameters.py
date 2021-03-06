import beam
import nexus

class test_parameters:
    def __init__(self, service_clients, param1, param2, param3, param4, param5, param6, param7, param8):
        self.service_clients = service_clients
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        self.param6 = param6
        self.param7 = param7
        self.param8 = param8
        self.state = None
        self.tasks = beam.RoutineTaskQueue()
        self.completion_queue = beam.Queue()

    def start(self):
        self.tasks.push(self.S0)

    def wait(self):
        self.completion_queue.top()

    def S0(self):
        self.state = 0
        if self.C0():
            return self.S1()

    def S1(self):
        self.state = 1

    def C0(self):
        pass


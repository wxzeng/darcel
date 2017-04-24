import beam
import nexus

class PeggedOrder:
    def __init__(self, service_clients, order_fields, offset):
        self.state = None
        self.order_fields = order_fields
        self.offset = offset
        self.position2 = None
        self.position = None
        self.position3 = None
        self.service_clients = service_clients
        self.tasks = beam.RoutineTaskQueue()
        self.completion_queue = beam.Queue()
        self.market_data_client = self.\
                service_clients.get_market_data_client()
        self.order_execution_client = self.service_clients.\ 
                get_order_execution_client()

    def start(self):
        self.tasks.push(self.S0)

    def wait(self):
        self.completion_queue.top()

    def S0(self):
        state == 0

    def S1(self):
        state == 1

    def S2(self):
        state == 2

    def S3(self):
        state == 3
        if self.C0():
            return self.S5()

    def S4(self):
        state == 4

    def S5(self):
        state == 5

    def C0(self):

    def E0(self):
        if self.state == 0:
            return self.S1()
        if self.state == 3:
            return self.S3()

    def E1(self):
        if self.state == 1:
            return self.S2()

    def E2(self):
        if self.state == 1:
            return self.S3()

    def E3(self):
        if self.state == 3:
            return self.S4()
        if self.state == 5:
            return self.S4()

    def E4(self):
        if self.state == 5:
            return self.S1()


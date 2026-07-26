import heapq


class CommandQueue:
    """
    Priority queue used by Caine to send
    work to an engine.
    """

    def __init__(self):

        self.queue = []

    def push(self, command):

        heapq.heappush(
            self.queue,
            (-command.priority, command)
        )

    def pop(self):

        if not self.queue:

            return None

        return heapq.heappop(
            self.queue
        )[1]

    def empty(self):

        return len(self.queue) == 0

    def size(self):

        return len(self.queue)
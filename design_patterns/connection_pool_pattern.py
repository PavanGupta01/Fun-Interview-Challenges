"""
Note about thread safety concept used here.

Thread safety is a concept in programming that ensures that a piece of code or data structure 
functions correctly when accessed by multiple threads simultaneously. 
In a multithreaded environment, multiple threads can execute concurrently, 
and if they access shared resources (such as variables, data structures, or hardware),
it can lead to race conditions, data corruption, or unexpected behavior.

Thread-safe code ensures that shared resources are accessed 
and modified in a controlled and predictable manner, 
typically by using synchronization mechanisms 
such as locks, mutexes, semaphores, or other concurrency control techniques.
"""

import threading


class Connection:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Connection {self.id}"


class ConnectionPool:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety
    _pool = []
    _max_connections = 5
    _current_connections = 0

    def __new__(cls):
        if not cls._instance:
            with cls._lock:  # Ensure only one thread initializes the instance
                if not cls._instance:
                    cls._instance = super(ConnectionPool, cls).__new__(cls)
        return cls._instance

    def get_connection(self):
        with self._lock:  # Ensure only one thread can execute this block at a time
            if self._pool:
                return self._pool.pop(0)
            elif self._current_connections < self._max_connections:
                connection = Connection(self._current_connections)
                self._current_connections += 1
                return connection
            else:
                raise Exception("Max connections reached")

    def release_connection(self, connection):
        with self._lock:  # Ensure only one thread can execute this block at a time
            self._pool.append(connection)


# Example usage
if __name__ == "__main__":
    pool = ConnectionPool()
    connections = []

    # Get 5 connections
    for _ in range(5):
        connections.append(pool.get_connection())

    # Print connections
    for conn in connections:
        print(conn)

    # Try to get a 6th connection (this should raise an exception)
    try:
        pool.get_connection()
    except Exception as e:
        print(e)

    # Release a connection back to the pool
    pool.release_connection(connections[0])

    # Get a new connection (should succeed since one was released)
    conn = pool.get_connection()
    print(conn)

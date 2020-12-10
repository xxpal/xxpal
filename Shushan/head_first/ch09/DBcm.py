import mysql.connector


# If a class defines __enter__ and __exit__, it's regarded as a context manager,
# as a consequence, can hook into (and be used with) "with".
class UseDatabase:
    # Although defining __init__ is not essential for a context manager,
    # it's useful to do so, as it helps separate any initialization from any setup
    def __init__(self, config: dict) -> None:     # __init__ runs before __enter__ to perform initialization if needed
        self.configuration = config

    def __enter__(self) -> 'cursor':    # Perform any setup activities
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:     # Perform any teardown/tidying-up activities
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

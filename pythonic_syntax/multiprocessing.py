# Python program to illustrate
# the concept of race condition
# in multiprocessing
import multiprocessing
import subprocess
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(processName)s] %(message)s",
    handlers=[logging.FileHandler("multiprocessing.log"), logging.StreamHandler()],
)

logger = logging.getLogger()


def worker_function(command: str, queue: multiprocessing.Queue):
    try:
        logger.info(f"Worker {command} started.")

        # Simulating an error for demonstration purposes
        result = subprocess.run(["open", "-a", "Notes"], capture_output=True, text=True)
        # Check for successful execution
        if result.returncode == 0:
            logger.info(f"Worker {command} finished successfully.")
            queue.put((command, "success"))
            return result.stdout.strip()  # Remove trailing newline
        else:
            logger.error(f"Worker {command} failed.")
            queue.put((command, "error"))
            raise subprocess.CalledProcessError(result.returncode, command)

    except Exception as e:
        queue.put((command, "error"))
        logger.error(f"Exception in worker {command}: {e}", exc_info=True)


def upgrade_firmware():
    queue = multiprocessing.Queue()
    MAX_PROCESS = 5

    # Device info
    processName = multiprocessing.Value("i", 100)

    # creating new processes
    processes = []

    for x in range(MAX_PROCESS):
        process = multiprocessing.Process(target=worker_function, args=(processName, queue))
        processes.append(process)
        process.start()

    # wait until processes are finished
    for x in range(MAX_PROCESS):
        processes[x].join()


if __name__ == "__main__":
    # for _ in range(10):

    # perform same transaction process 10 times
    upgrade_firmware()

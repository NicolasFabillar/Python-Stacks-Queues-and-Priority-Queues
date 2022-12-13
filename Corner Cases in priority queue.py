from dataclasses import dataclass
from PriorityQueues import PriorityQueue

@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

print(wipers < hazard_lights)

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)
messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

# Will return error since comparison between message and message is not supported.
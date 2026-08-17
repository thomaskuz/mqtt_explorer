# Python Learning Scripts for IoT Development

These scripts teach Python concepts needed for IoT development, from basics to advanced topics.

## Scripts Overview

### 1. Variables and Types
**File:** `01_variables_and_types.py`

Learn about Python's basic data types: integers, floats, strings, booleans, and None.

**Topics:**
- Creating variables
- Different data types
- Type conversion
- Using variables in IoT context

**Run:** `python3 tests/01_variables_and_types.py`

---

### 2. Functions
**File:** `02_functions.py`

Learn how to write reusable code blocks that do one job.

**Topics:**
- Defining functions
- Parameters and returns
- Single and multiple inputs
- Functions that print vs return values

**Run:** `python3 tests/02_functions.py`

**Key Insight:** Functions follow DRY (Don't Repeat Yourself) — write once, use many times.

---

### 3. Dictionaries
**File:** `03_dictionaries.py`

Learn how to organize data with named keys and values.

**Topics:**
- Creating dictionaries
- Accessing values
- Adding and modifying data
- Looping through dictionaries
- Lists of dictionaries (common in IoT!)

**Run:** `python3 tests/03_dictionaries.py`

**Key Insight:** Dictionaries are perfect for sensor data — self-documenting and JSON-ready.

---

### 4. Lists and Loops
**File:** `04_lists_and_loops.py`

Learn how to handle multiple items without repeating code.

**Topics:**
- Creating lists
- Accessing items
- Looping through lists
- List operations (append, remove, sort)
- Finding max, min, average
- Filtering lists

**Run:** `python3 tests/04_lists_and_loops.py`

**Key Insight:** Loops let you handle any number of sensors without changing code.

---

### 5. Classes and Objects
**File:** `05_classes_and_objects.py`

Learn how to organize code around real-world things (objects).

**Topics:**
- Creating classes (blueprints)
- Creating objects (instances)
- Attributes (data)
- Methods (functions on objects)
- The `self` keyword
- When to use classes vs functions

**Run:** `python3 tests/05_classes_and_objects.py`

**Key Insight:** Classes let you model a sensor, broker, or any real thing in your system.

---

### 6. Methods vs Functions
**File:** `06_methods_vs_functions.py`

Understand the crucial difference between functions and methods.

**Topics:**
- Functions: standalone code
- Methods: code attached to objects
- Calling differences
- When to use each
- Real IoT examples

**Run:** `python3 tests/06_methods_vs_functions.py`

**Key Insight:** Methods have access to object state via `self`; functions don't.

---

### 7. Callbacks
**File:** `07_callbacks.py`

Learn how callbacks work — crucial for MQTT!

**Topics:**
- Passing functions as parameters
- Event-driven programming
- Multiple callbacks
- MQTT-style callbacks (on_connect, on_disconnect)
- Real MQTT simulation

**Run:** `python3 tests/07_callbacks.py`

**Key Insight:** Callbacks = "When X happens, call THIS function" — the foundation of MQTT.

---

### 8. Imports and Libraries
**File:** `08_imports_and_libraries.py`

Learn how to use code others wrote instead of writing everything from scratch.

**Topics:**
- Standard library modules (random, json, datetime, time)
- Importing specific items
- Common IoT libraries
- Import organization best practices

**Run:** `python3 tests/08_imports_and_libraries.py`

**Key Insight:** Good libraries save you weeks of work.

---

### 9. Event Loops
**File:** `09_event_loops.py`

Learn how event loops work — **CRUCIAL for MQTT!**

**Topics:**
- What event loops are
- Why event loops matter
- Simple event loop examples
- MQTT event loop (client.loop())
- Blocking vs non-blocking loops
- Polling event loops
- Multiple event sources
- Event loop patterns

**Run:** `python3 tests/09_event_loops.py`

**Key Insight:** Your MQTT client IS an event loop — it waits for events and calls callbacks.

---

## How to Use These Scripts

### Learning Path

1. **Start with basics:** 01 → 02 → 03 → 04
   - Learn variables, functions, data structures, and loops

2. **Learn objects:** 05 → 06
   - Understanding classes and when to use them

3. **Learn events:** 07 → 09
   - Callbacks and event loops — the foundation of MQTT!

4. **Learn tools:** 08
   - How to use libraries and save time

### For Each Script

1. **Run it:** `python3 tests/XX_filename.py`
2. **Read the output:** See examples working
3. **Read the code:** Understand how it works
4. **Try exercises:** At the end of each script
5. **Modify it:** Experiment, break things, fix them

### Recommended Schedule

**Day 1:** Scripts 01-02 (Basics)
**Day 2:** Scripts 03-04 (Data structures)
**Day 3:** Scripts 05-06 (Objects)
**Day 4:** Scripts 07, 09 (Callbacks and event loops - MQTT core!)
**Day 5:** Script 08 (Libraries and tools)

Don't rush! Understanding is more important than speed.

---

## Connection to Your MQTT Project

Here's how these concepts appear in your `sensor_mqtt_publisher.py`:

| Script | Concept | Used In |
|--------|---------|---------|
| 01 | Variables | `MQTT_BROKER`, `INTERVAL_SECONDS` |
| 02 | Functions | `generate_reading()` |
| 03 | Dictionaries | Sensor reading data structure |
| 04 | Loops | Main event loop with `while True` |
| 05 | Classes | `SensorReading` (Pydantic class) |
| 06 | Methods | `client.publish()`, `.model_dump_json()` |
| 07 | Callbacks | `on_connect()`, `on_disconnect()` |
| 08 | Imports | `paho.mqtt`, `pydantic`, `json`, `datetime` |
| 09 | Event Loops | `while True: client.loop()` — the entire publisher! |

---

## Practice Strategy

### Level 1: Run and Understand
- Run each script
- Read the output
- Understand what's happening

### Level 2: Modify
- Change variables
- Try different values
- See what breaks and why

### Level 3: Exercises
- Do the exercises at the end of each script
- Try to solve them without looking at examples

### Level 4: Create
- Write your own scripts combining concepts
- Build small projects

### Level 5: Apply
- Apply concepts to your MQTT project
- Refactor existing code with new understanding

---

## Common Questions

**Q: Why so many small scripts instead of one big file?**
A: Smaller, focused scripts are easier to understand and practice with. You can run them independently and focus on one concept.

**Q: Do I need to memorize all this?**
A: No! Use these as references. Real learning comes from writing code, making mistakes, and fixing them.

**Q: What if I don't understand something?**
A: That's normal! Read the explanation, run the examples, modify the code, and ask questions. Understanding takes time.

**Q: Can I skip any scripts?**
A: Not really. Each builds on previous ones. Especially don't skip 05 (Classes) and 07 (Callbacks) — they're crucial for IoT.

---

## Next Steps After Learning

1. **Expand your MQTT project:**
   - Add more sensors
   - Create subscriber scripts
   - Build monitoring systems

2. **Write your own modules:**
   - Create a `sensors.py` module with sensor classes
   - Create a `utils.py` with utility functions
   - Organize your code properly

3. **Learn more advanced topics:**
   - Async programming
   - Testing
   - Error handling
   - Design patterns

4. **Build real projects:**
   - Home automation
   - Environmental monitoring
   - IoT data collection
   - Real sensor integration

---

## Tips for Success

✓ **Run the scripts** — seeing output helps understanding
✓ **Modify the code** — change values and see what happens
✓ **Do the exercises** — practice is how you learn
✓ **Take breaks** — learning in short bursts is better
✓ **Ask questions** — confusion is part of learning
✓ **Build projects** — real code teaches better than exercises

---

## File Structure

```
tests/
├── 01_variables_and_types.py
├── 02_functions.py
├── 03_dictionaries.py
├── 04_lists_and_loops.py
├── 05_classes_and_objects.py
├── 06_methods_vs_functions.py
├── 07_callbacks.py
├── 08_imports_and_libraries.py
├── 09_event_loops.py
└── README_PYTHON_LEARNING.md (this file)
```

---

---

## Important Note: Event Loops Are The Core of MQTT

Your entire `sensor_mqtt_publisher.py` is built around an event loop:

```python
while True:                           # The event loop
    client.loop(timeout=0.1)          # Process MQTT events

    if time.time() - last_publish >= INTERVAL_SECONDS:
        # Publish sensor data (your event handler)
        client.publish(MQTT_TOPIC, payload)
```

**This is why script 09 (Event Loops) is so important.** It's not just theory — it's the exact pattern you're using right now!

Understanding event loops = Understanding how your MQTT project works.

---

**Start with script 01, run it, and learn step by step. You've got this! 🚀**

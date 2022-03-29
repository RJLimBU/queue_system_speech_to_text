# queue_system_speech_to_text

### Description

convert speech to text using queuing and multiprocessing/multithreading.

### Design

- Make 1 process per API. <br />
- Should split processing of API into multiple threads <br />
- The number of API calls depends on the processor, should experiment on the <br />
CPU to determine how many API calls it can handle simultaneously <br />

### Phase 1 Queue System

- "queueMultiProc.py": stub function with multiprocessing and queue

- "queueMultiThread.py": stub function with multithreading and queue

- "multiprocTest.py": stub function with multiprocessing

### phase 2 speech to text

- "speech2Text.py": convert speech to text using google cloud

- "s2tMultiThread.py": speech to text with multi-threading
	
	The "s2tMultiThread.py" convert the example audios to text message using multi-threading and queue



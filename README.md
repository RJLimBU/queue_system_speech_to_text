# queue_system_speech_to_text

### Description

convert speech to text using queuing and multiprocessing/multithreading.

### Design

- Make 1 process per API. <br />
- Should split processing of API into multiple threads <br />
- The number of API calls depends on the processor, current thought <br />
is running 4 API calls simultaneously. <br />

### Phase 1 Queue System

- "queueMultiProc.py": stub function with multiprocessing and queue

- "queueMultiThread.py": stub function with multithreading and queue

- "multiprocTest.py": stub function with multiprocessing

### phase 2 speech to text

- "speech2Text.py": convert speech to text using google cloud

- "s2tMultiThread.py": speech to text with queue and multi-threading
	
	The "s2tMultiThread.py" convert the example audios to text message using multi-threading and queue

#### Speech to Text with Multi-threading

- The idea for implementing speech to text with multi-threading is that one separates a speech 
to many small pieces of sentences,then put each piece of sentences in a queuing list. The process 
of converting a piece of sentences into text is handle with threads. The queuing process is based 
on the order of sentences. The script uses google cloud to convert speech to text.

### Example

- The example shows the result after running the speech to text with queue and multi-threading.
>![Screenshot](./images/s2tMultiThr.png)






# queue_system_speech_to_text

### Description

convert speech to text using queuing and multiprocessing/multithreading.

### Design

- Make 1 process per API. <br />
- Should split processing of API into multiple threads <br />
- The number of API calls depends on the processor, should experiment on the <br />
CPU to determine how many API calls it can handle simultaneously <br />



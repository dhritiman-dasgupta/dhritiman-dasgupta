<h1 align="center">Dhritiman Dasgupta</h1>

<p align="center">
  <b>Embedded systems and applied ML — from the PCB and the firmware up to the cloud that receives the data.</b>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/dhritiman-dasgupta-27aa55243"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white"></a>
  <a href="https://www.instagram.com/dhritiman.dasgupta"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white"></a>
  <a href="https://dhritiman-dasgupta.github.io"><img alt="Website" src="https://img.shields.io/badge/dhritiman--dasgupta.github.io-24292F?logo=githubpages&logoColor=white"></a>
</p>

<p align="center">
  <img alt="Embedded" src="https://img.shields.io/badge/embedded-ESP32%20%C2%B7%20nRF%20%C2%B7%20Jetson-0E9488">
  <img alt="Edge AI" src="https://img.shields.io/badge/edge%20AI-on--device%20STT%2FTTS-7A34F5">
  <img alt="Backend" src="https://img.shields.io/badge/backend-Kafka%20%C2%B7%20Docker%20%C2%B7%20AWS-E8730B">
  <img alt="Hardware" src="https://img.shields.io/badge/hardware-KiCad%20%C2%B7%20DFM-B32340">
</p>

---

### What I build

I work across the whole stack of a connected device: schematic and PCB layout, firmware on the
microcontroller, the radio or cellular link, and the server that has to survive a few hundred of
them talking at once. Most of my projects sit at that seam — where an embedded constraint decides
a backend design, or the other way round.

Recurring themes:

- **Audio and voice on constrained hardware** — Opus over cellular links, wake-word detection that
  runs in a browser or on a Jetson, on-device TTS with a cloned voice
- **Vision and biosignals** — document capture and OCR, ECG and PPG acquisition, custom detection models
- **Pipelines that hold up** — event-driven ingest, load generators honest enough to prove a claim

### Selected work

| Project | What it is |
|---|---|
| **[opusfleet](https://github.com/dhritiman-dasgupta/opusfleet)** | Kafka-backed ingest for Opus/RTP audio from device fleets, with a 500-device simulator. Measured at 25k frames/s with zero drops. |
| **[jetson-avatar-studio](https://github.com/dhritiman-dasgupta/jetson-avatar-studio)** | On-device talking avatar for a Jetson Orin Nano — cloned voice TTS, STT, LLM and hotword, all local. |
| **[overhead-scanner](https://github.com/dhritiman-dasgupta/overhead-scanner)** | Browser app for an overhead document camera: capture, deskew, clean up, OCR, searchable PDF. No uploads, no build step. |
| **[overhead-scanner-py](https://github.com/dhritiman-dasgupta/overhead-scanner-py)** | The desktop counterpart — full-resolution 16 MP capture, auto page detection, perspective correction. |
| **[hey-kiki-wakeword-web](https://github.com/dhritiman-dasgupta/hey-kiki-wakeword-web)** | A trained openWakeWord ONNX model running fully client-side with onnxruntime-web and the mic. |
| **[ECG-ANALYSIS](https://github.com/dhritiman-dasgupta/ECG-ANALYSIS)** | ECG acquisition and analysis, including a 12-lead conversion API and the IoT device that feeds it. |

### Toolbox

<p>
  <img alt="C" src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white">
  <img alt="C++" src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white">
  <img alt="ESP-IDF" src="https://img.shields.io/badge/ESP--IDF-E7352C?logo=espressif&logoColor=white">
  <img alt="Zephyr" src="https://img.shields.io/badge/nRF%20Connect-00A9CE?logo=nordicsemiconductor&logoColor=white">
  <img alt="KiCad" src="https://img.shields.io/badge/KiCad-314CB0?logo=kicad&logoColor=white">
</p>
<p>
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white">
  <img alt="Kafka" src="https://img.shields.io/badge/Kafka-231F20?logo=apachekafka&logoColor=white">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white">
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white">
  <img alt="ONNX" src="https://img.shields.io/badge/ONNX-005CED?logo=onnx&logoColor=white">
</p>

---

<p align="center">
  <a href="https://github.com/dhritiman-dasgupta?tab=repositories">Repositories</a> ·
  <a href="https://dhritiman-dasgupta.github.io">dhritiman-dasgupta.github.io</a> ·
  <a href="https://www.linkedin.com/in/dhritiman-dasgupta-27aa55243">LinkedIn</a> ·
  <a href="https://www.instagram.com/dhritiman.dasgupta">Instagram</a>
</p>

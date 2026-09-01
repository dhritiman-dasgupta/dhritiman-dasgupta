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
| **[slo-gated-delivery](https://github.com/dhritiman-dasgupta/slo-gated-delivery)** | A Kubernetes delivery platform where a bad release rolls itself back — an Argo Rollouts canary gated on Prometheus error-budget queries, on modular Terraform. Fault injection at 8% returned 181 × 200 / 19 × 500, emitting exactly the series the AnalysisTemplate reads. |
| **[opusfleet](https://github.com/dhritiman-dasgupta/opusfleet)** | Kafka-backed ingest for Opus/RTP audio from device fleets. 25,000 frames/s sustained (500 × 50), 0 dropped and 0 reconnects, against a *simulated* fleet speaking the real wire format. Segments are re-muxed, not re-encoded — 28 MB/h against 345 MB/h for WAV. |
| **[esp32-p4-video-recorder](https://github.com/dhritiman-dasgupta/esp32-p4-video-recorder)** | ESP32-P4 firmware: MIPI camera → the chip's hardware H.264 encoder → a Wi-Fi live stream a browser decodes with WebCodecs, never transcoded. The first working stream ran at 2.9 fps; the cause was a recording-oriented QP preset, not the encoder — widening it for the streaming path took the average frame from ~4 KB to 342 B and the stream to 14.6 fps, a 5× gain. |
| **[jetson-avatar-studio](https://github.com/dhritiman-dasgupta/jetson-avatar-studio)** | Hear, understand and reply in a cloned voice, entirely on an 8 GB Jetson Orin — whisper.cpp, llama.cpp and NeuTTS behind a C++ orchestrator, with the microphone audio never leaving the board. All three models stay resident (~8 s a turn against ~12 s when evicting); the q8 TTS codec is pinned to CPU because on GPU it swap-thrashes into an OOM reboot. |
| **[virtual-tryon](https://github.com/dhritiman-dasgupta/virtual-tryon)** | A FastAPI service wrapping FLUX.2 klein 9B and fal's virtual-try-on LoRA on ComfyUI, with the batch pipeline and QA harness. 172 generations in 26.9 min on one RTX 4090, mean 9.4 s, seed pinned so results differ only by their inputs. |
| **[overhead-scanner-py](https://github.com/dhritiman-dasgupta/overhead-scanner-py)** | A desktop document scanner built around measured camera limits: Chrome's stream caps at 1598 × 1200 and its 16 MP mode needs 66 s to a first frame, so this drives the sensor directly and keeps a live preview beside 16 MP stills. |
| **[hey-kiki-wakeword-web](https://github.com/dhritiman-dasgupta/hey-kiki-wakeword-web)** | A trained openWakeWord ONNX model running fully client-side with onnxruntime-web and the microphone — no server, no upload, no build step. [Try it live](https://dhritiman-dasgupta.github.io/hey-kiki-wakeword-web/). |

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

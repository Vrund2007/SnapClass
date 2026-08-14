# 📱 SnapClass — AI Attendance Web Application

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vrundsnapclass.streamlit.app/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Supabase](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com)
[![DeepFace](https://img.shields.io/badge/AI%20Model-DeepFace-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://github.com/serengil/deepface)

**The core interactive AI attendance engine with multi-face detection, instant biometric verification, and classroom management.**

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Application Architecture](#-application-architecture)
- [Teacher Workflow & Capabilities](#-teacher-workflow--capabilities)
- [Student Workflow & Capabilities](#-student-workflow--capabilities)
- [AI Pipelines Deep Dive](#-ai-pipelines-deep-dive)
  - [1. Face Recognition Pipeline (`face_pipeline.py`)](#1-face-recognition-pipeline-face_pipelinepy)
  - [2. Voice Recognition Pipeline (`voice_pipeline.py`)](#2-voice-recognition-pipeline-voice_pipelinepy)
- [Database Schema & Queries](#-database-schema--queries)
- [UI Components & Dialogs](#-ui-components--dialogs)
- [Local Installation & Setup](#-local-installation--setup)
- [Deployment to Streamlit Cloud](#-deployment-to-streamlit-cloud)
- [Troubleshooting & FAQs](#-troubleshooting--faqs)

---

## 📖 Overview

The **SnapClass AI Web Application** is built with **Streamlit** for seamless real-time reactivity and state management, integrated with **DeepFace / OpenCV** for biometric face recognition, and powered by a cloud-hosted **Supabase PostgreSQL** database.

---

## 🏗️ Application Architecture

```
ai-attendance-project-app/
├── app.py                         # Application entrypoint & URL query parameter routing
├── schema.sql                     # Supabase SQL DDL definition
├── requirements.txt               # Python package dependencies
├── packages.txt                   # Linux OS-level dependencies for OpenCV & libGL
├── src/
│   ├── components/                # Modular UI components & dialog popups
│   │   ├── dialog_add_photo.py    # Camera snapshot & photo uploader modal
│   │   ├── dialog_attendance_results.py # Present/absent results confirmation modal
│   │   ├── dialog_auto_enroll.py  # Instant enrollment modal from ?join-code URL
│   │   ├── dialog_create_subject.py # New subject creation dialog
│   │   ├── dialog_enroll.py       # Student manual code enrollment dialog
│   │   ├── dialog_share_subject.py# QR code generator & invite link dialog
│   │   ├── header.py / footer.py  # Brand header and footer components
│   │   └── subject_card.py        # High-contrast subject summary card
│   │
│   ├── database/                  # Supabase database operations
│   │   ├── config.py              # Supabase client instantiation
│   │   └── db.py                  # CRUD queries for teachers, students, subjects, attendance
│   │
│   ├── pipelines/                 # Machine learning & audio analysis
│   │   ├── face_pipeline.py       # DeepFace multi-face detection & embedding verification
│   │   └── voice_pipeline.py      # SpeechRecognition audio pipeline
│   │
│   ├── screens/                   # Top-level screen views
│   │   ├── home_screen.py         # Role selector landing (Teacher or Student)
│   │   ├── teacher_screen.py      # Complete Teacher Dashboard & management tabs
│   │   └── student_screen.py      # Complete Student Dashboard & attendance metrics
│   │
│   └── ui/                        # Styling & themes
│       └── base_layout.py         # Global CSS stylesheet & high-contrast UI tokens
└── README.md                      # This file
```

---

## 👨‍🏫 Teacher Workflow & Capabilities

1. **Authentication:** Sign up or log in securely with username and password.
2. **Manage Subjects:**
   - Create new courses (e.g. `CS101`, `Python Programming`, Section `A`).
   - Overview of enrolled students and total lectures conducted.
   - Click **Share Code** to open the **Share Class Link Modal** with an auto-generated QR code (`segno`) and direct invite link (`https://vrundsnapclass.streamlit.app/?join-code=CS101`).
3. **Take AI Attendance:**
   - Select a subject.
   - Click **Add Photos** to capture live classroom snapshots via webcam (`st.camera_input`) or upload photos from device storage.
   - Click **Mark Attendance**: The `face_pipeline.py` executes, extracts facial embeddings for everyone in the frame, matches them against enrolled student biometrics, and presents an interactive attendance verification modal.
   - Alternatively, use **Voice Attendance** for spoken roll calls.
4. **Attendance Records:**
   - View historical timestamped records with student names, roll numbers, status, and confidence scores.

---

## 👨‍🎓 Student Workflow & Capabilities

1. **Biometric Profile Setup:**
   - Enter Full Name and Roll Number.
   - Capture a clear frontal face reference photo. SnapClass computes a **128-dimensional biometric embedding** and securely stores it in Supabase `students.face_encoding`.
2. **Class Enrollment:**
   - Scan teacher's QR code or click an invite link to auto-enroll via URL query parameters (`?join-code=...`).
   - Or manually type the 6-character subject code in the student dashboard.
3. **Personal Attendance Tracking:**
   - Real-time statistics: Total attended lectures, missed classes, and attendance percentages with visual color indicators.

---

## 🧠 AI Pipelines Deep Dive

### 1. Face Recognition Pipeline (`face_pipeline.py`)

- **Detection Model:** OpenCV / RetinaFace / SSD.
- **Biometric Model:** DeepFace (VGG-Face / Facenet / ArcFace).
- **Matching Algorithm:** Cosine Distance Thresholding.
  $$\text{Cosine Similarity} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$
- **Multi-Face Batch Processing:** When a wide classroom photo is passed, the pipeline locates all bounding boxes, extracts individual face crops, generates embeddings, and compares them against enrolled student encodings in memory.

### 2. Voice Recognition Pipeline (`voice_pipeline.py`)

- **Audio Engine:** `SpeechRecognition` library.
- **Processing:** Transcribes audio speech stream, parses student names or roll numbers spoken by the educator, and correlates them with enrolled rosters.

---

## 🗄️ Database Schema & Queries

Defined in [`schema.sql`](file:///ai-attendance-project-app/schema.sql):

| Table | Primary Key | Description | Key Relationships |
|---|---|---|---|
| `public.teachers` | `id` (UUID) | Stores teacher credentials & names | Referenced by `subjects.teacher_id` |
| `public.students` | `student_id` (UUID) | Stores student names, roll numbers & face encodings | Referenced by `subject_students`, `attendance_logs` |
| `public.subjects` | `subject_id` (UUID) | Subject codes, names, sections | `teacher_id` -> `teachers.id` |
| `public.subject_students` | `id` (UUID) | Many-to-Many student enrollment mapping | Foreign keys to `subjects` and `students` |
| `public.attendance_logs` | `log_id` (UUID) | Timestamped attendance logs | Foreign keys to `subjects` and `students` |

---

## 💻 Local Installation & Setup

### Prerequisites
- **Python 3.11** (`py -3.11` recommended)
- A **Supabase** account and project

### Steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vrund2007/SnapClass.git
   cd SnapClass/ai-attendance-project-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   py -3.11 -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in `ai-attendance-project-app/.env`:
   ```env
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-publishable-key
   ```

5. **Initialize Database Tables:**
   - Open your [Supabase SQL Editor](https://supabase.com/dashboard).
   - Copy the contents of `schema.sql` and run the script.

6. **Launch the application:**
   ```bash
   streamlit run app.py
   ```
   Open **`http://localhost:8501`** in your browser!

---

## ☁️ Deployment to Streamlit Cloud

1. Push your repository to GitHub (`git push origin main`).
2. Visit **[share.streamlit.io](https://share.streamlit.io)** and log in.
3. Click **"New App"** and configure:
   - **Repository:** `YourUsername/SnapClass`
   - **Branch:** `main`
   - **Main file path:** `ai-attendance-project-app/app.py`
4. In **Advanced settings** ➔ **Secrets**, paste:
   ```toml
   SUPABASE_URL = "https://your-project.supabase.co"
   SUPABASE_KEY = "your-supabase-publishable-key"
   ```
5. Click **Deploy!**

> **Note:** The `packages.txt` file in this directory contains `libgl1`, `libglib2.0-0`, and `ffmpeg` to ensure OpenCV and audio decoders run seamlessly on Streamlit Cloud's Linux containers.

---

## ❓ Troubleshooting & FAQs

- **Q: Why does webcam permission fail in the browser?**
  - Make sure you allow camera access in your browser prompt. On remote deployments, camera access requires an `https://` secure connection.
- **Q: How to reset student face embeddings?**
  - Delete the student entry from the `students` table in Supabase or have the student re-register with a clear, well-lit frontal face photo.
- **Q: Camera snapshot not detecting students in low light?**
  - Ensure the classroom is well illuminated and the camera photo is sharp and in focus.

---

<div align="center">
Part of the <b>SnapClass</b> ecosystem.
</div>
# 🎓 SnapClass — Next-Gen AI-Powered Classroom Attendance System

<div align="center">

![SnapClass Logo](https://i.ibb.co/YTYGn5qV/logo.png)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vrundsnapclass.streamlit.app/)
[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=flat&logo=vercel)](https://snapclass-landing.vercel.app)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Supabase Database](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com)
[![DeepFace AI](https://img.shields.io/badge/AI%20Engine-DeepFace-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://github.com/serengil/deepface)

**Automate attendance in seconds using multi-face AI detection, voice recognition, and instant QR enrollment.**

[Explore Live Web App](https://vrundsnapclass.streamlit.app/) • [Landing Page](https://snapclass-landing.vercel.app) • [Database Schema](#-database-architecture) • [Quick Start](#-quick-start-guide)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Repository Structure](#-repository-structure)
- [System Architecture](#-system-architecture)
- [Database Architecture](#-database-architecture)
- [Quick Start Guide](#-quick-start-guide)
  - [Prerequisites](#prerequisites)
  - [Environment Variables Setup](#environment-variables-setup)
  - [Running the AI Attendance Streamlit App](#1-running-the-ai-attendance-streamlit-app)
  - [Running the Flask Landing Page](#2-running-the-flask-landing-page)
- [Deployment Guide](#-deployment-guide)
  - [Deploying Streamlit App to Streamlit Cloud](#deploying-streamlit-app-to-streamlit-community-cloud)
  - [Deploying Landing Page to Vercel](#deploying-landing-page-to-vercel)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Overview

**SnapClass** is a full-stack, enterprise-ready AI attendance automation platform designed for modern schools, universities, and educational institutions. Traditional attendance wastes 10–15 minutes of every lecture. With SnapClass:

1. **Teachers** take a quick wide-angle classroom photo or upload camera snapshots.
2. The **Deep Learning Face Recognition Engine** detects and identifies all enrolled students simultaneously in milliseconds.
3. Attendance is securely recorded in real-time in a cloud **PostgreSQL database (Supabase)** with instant analytics for teachers and students.

---

## ✨ Key Features

### 👨‍🏫 Teacher Portal
- **🔐 Secure Authentication:** Fast signup & login with cryptographic password hashing.
- **📚 Course & Subject Management:** Create and manage classes, sections, and subject codes (`CS101`, `MATH201`).
- **🔗 Instant QR & Direct Link Sharing:** Auto-generates dynamic high-res QR codes and instant join links (`?join-code=...`) to enroll students on the fly.
- **📸 Multi-Angle AI Photo Attendance:** Capture live webcam snapshots or upload batch classroom photos. SnapClass detects all faces in the crowd and marks present students instantly.
- **🎙️ Voice Recognition Attendance:** Alternative voice-activated roll-call attendance processing.
- **📊 Real-time Attendance Logs & Analytics:** Filter, view, and export timestamped class records.

### 👨‍🎓 Student Portal
- **👤 Biometric Face Profile Registration:** Students upload/capture reference face photos to register their facial biometrics in the AI pipeline.
- **⚡ 1-Click Class Enrollment:** Enroll using 6-character subject codes or scan teacher-provided QR codes.
- **📈 Personal Attendance Analytics:** Track classes attended, missed lectures, and real-time attendance percentage per subject.

---

## 📂 Repository Structure

This repository is organized as a clean **monorepo** containing both the AI web application and the public landing page:

```
SnapClass/
├── ai-attendance-project-app/        # 🚀 Core AI Attendance Web Application (Streamlit)
│   ├── app.py                        # Main entrypoint & query parameter router
│   ├── schema.sql                    # Supabase PostgreSQL DDL schema & RLS policies
│   ├── requirements.txt              # App dependencies (Streamlit, DeepFace, Supabase, etc.)
│   ├── packages.txt                  # Linux OS dependencies for Streamlit Cloud (libgl1, etc.)
│   ├── src/
│   │   ├── components/               # Reusable UI cards, dialogs & modals
│   │   │   ├── dialog_add_photo.py   # Webcam & file upload modal
│   │   │   ├── dialog_attendance_results.py # Attendance confirmation modal
│   │   │   ├── dialog_create_subject.py     # New subject creation modal
│   │   │   ├── dialog_enroll.py      # Student subject enrollment dialog
│   │   │   ├── dialog_share_subject.py      # Dynamic QR code & share link modal
│   │   │   ├── header.py / footer.py # Standardized headers and footers
│   │   │   └── subject_card.py       # Subject overview card with live stats
│   │   ├── database/                 # Supabase client & database CRUD queries
│   │   │   ├── config.py             # Supabase initialization with env keys
│   │   │   └── db.py                 # Teachers, Students, Attendance & Subject queries
│   │   ├── pipelines/                # Deep learning & audio processing pipelines
│   │   │   ├── face_pipeline.py      # DeepFace multi-face detection & cosine matching
│   │   │   └── voice_pipeline.py     # Speech-to-text audio processing
│   │   ├── screens/                  # Screen views
│   │   │   ├── home_screen.py        # Role selection portal (Teacher / Student)
│   │   │   ├── teacher_screen.py     # Teacher dashboard, attendance, & subject manager
│   │   │   └── student_screen.py     # Student dashboard & class enrollment
│   │   └── ui/                       # Design system & custom CSS stylesheets
│   │       └── base_layout.py        # High-contrast glassmorphic styling & themes
│   └── README.md                     # Application-specific documentation
│
├── ai-attendance-project-landing/    # 🌐 Public Marketing & Product Landing Page (Flask)
│   ├── app.py                        # Flask server routing to templates
│   ├── vercel.json                   # Vercel deployment & WSGI configuration
│   ├── requirements.txt              # Flask, Gunicorn & Python-dotenv
│   ├── templates/
│   │   └── index.html                # Modern SaaS landing page with SVG vectors & animations
│   ├── static/
│   │   ├── css/style.css             # Glassmorphism, animations, responsive navbar & cards
│   │   ├── js/script.js              # Animated mobile hamburger menu & smooth scrolling
│   │   └── assets/                   # Vector SVGs, icons, and illustrations
│   └── README.md                     # Landing page documentation & Vercel deployment guide
│
└── README.md                         # Monorepo Master Documentation (This file)
```

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([Teacher or Student]) --> LP[Landing Page (Flask on Vercel)]
    LP -->|CTA Click| App[AI Attendance App (Streamlit Cloud)]
    
    subgraph "Streamlit Application"
        App --> Home[Role Router]
        Home -->|Teacher Login| TD[Teacher Dashboard]
        Home -->|Student Login| SD[Student Dashboard]
        
        TD --> AI_Photo[Face Recognition Pipeline]
        TD --> AI_Voice[Voice Recognition Pipeline]
        TD --> Subj[Subject & QR Manager]
        
        SD --> Enroll[1-Click QR Enrollment]
        SD --> Stats[Personal Attendance Tracking]
    end
    
    subgraph "AI Engine"
        AI_Photo --> DF[DeepFace Engine / OpenCV]
        DF --> Match[Cosine Similarity Embedding Matcher]
    end
    
    subgraph "Cloud Backend"
        App <--> DB[(Supabase PostgreSQL Database)]
        DB --- T_Table[(public.teachers)]
        DB --- S_Table[(public.students)]
        DB --- Sub_Table[(public.subjects)]
        DB --- Att_Table[(public.attendance_logs)]
    end
```

---

## 🗄️ Database Architecture

SnapClass uses **Supabase (PostgreSQL)**. All table definitions and relationships are managed via [`schema.sql`](file:///ai-attendance-project-app/schema.sql):

```sql
-- Teachers Table
CREATE TABLE public.teachers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Students Table
CREATE TABLE public.students (
    student_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    face_encoding JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Subjects Table
CREATE TABLE public.subjects (
    subject_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    section TEXT NOT NULL,
    teacher_id UUID REFERENCES public.teachers(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Subject Enrollment Mapping
CREATE TABLE public.subject_students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id UUID REFERENCES public.subjects(subject_id) ON DELETE CASCADE,
    student_id UUID REFERENCES public.students(student_id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(subject_id, student_id)
);

-- Attendance Logs
CREATE TABLE public.attendance_logs (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id UUID REFERENCES public.subjects(subject_id) ON DELETE CASCADE,
    student_id UUID REFERENCES public.students(student_id) ON DELETE CASCADE,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status TEXT DEFAULT 'present',
    confidence FLOAT
);
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.11** installed (`py -3.11 --version` or `python3.11 --version`)
- **Git** installed
- A free **[Supabase](https://supabase.com)** project

---

### Environment Variables Setup

Create a `.env` file in `ai-attendance-project-app/.env`:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-supabase-publishable-key
```

---

### 1. Running the AI Attendance Streamlit App

```bash
# Navigate to the app directory
cd ai-attendance-project-app

# Create virtual environment (Python 3.11 recommended)
py -3.11 -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Streamlit application
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser!

---

### 2. Running the Flask Landing Page

```bash
# Navigate to landing page directory
cd ai-attendance-project-landing

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask development server
python app.py
```
Open **`http://localhost:5002`** in your browser!

---

## ☁️ Deployment Guide

### Deploying Streamlit App to Streamlit Community Cloud

1. Push your monorepo to GitHub.
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in.
3. Click **"Create App"** and configure:
   - **Repository:** `YourUsername/SnapClass`
   - **Branch:** `main`
   - **Main file path:** `ai-attendance-project-app/app.py`
4. Click **Advanced Settings** -> **Secrets** and paste:
   ```toml
   SUPABASE_URL = "https://your-id.supabase.co"
   SUPABASE_KEY = "sb_publishable_..."
   ```
5. Click **Deploy!**

---

### Deploying Landing Page to Vercel

1. Log in to **[vercel.com](https://vercel.com)**.
2. Click **"Add New..."** ➔ **"Project"** ➔ Import **`YourUsername/SnapClass`**.
3. Under **Root Directory**, click **Edit** and choose: 👉 **`ai-attendance-project-landing`**.
4. Under **Environment Variables**, add:
   - `STREAMLIT_APP_URL` = `https://your-streamlit-app-url.streamlit.app/`
5. Click **Deploy!**

---

## 🛠️ Tech Stack

| Domain | Technology |
|---|---|
| **Frontend & App Framework** | [Streamlit](https://streamlit.io/) (Dashboard), [Flask](https://flask.palletsprojects.com/) + HTML5/CSS3/JS (Landing) |
| **AI / Biometrics Engine** | [DeepFace](https://github.com/serengil/deepface) (Facial Embeddings & Verification), [OpenCV](https://opencv.org/) |
| **Database & Auth** | [Supabase](https://supabase.com/) (PostgreSQL Database & Row Level Security) |
| **QR Code Generation** | [Segno](https://github.com/heuer/segno) |
| **Styling & Design** | Modern Glassmorphism, Google Fonts (`Outfit`, `Climate Crisis`), Vector SVGs |
| **Deployment & Hosting** | [Streamlit Community Cloud](https://streamlit.io/cloud) & [Vercel](https://vercel.com/) |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

<div align="center">
Made with ❤️ for modern educators and students worldwide.
</div>

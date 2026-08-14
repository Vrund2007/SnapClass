# 🌐 SnapClass — SaaS Marketing & Product Landing Page

<div align="center">

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=flat&logo=vercel)](https://snapclass-landing.vercel.app)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5 / CSS3 / JS](https://img.shields.io/badge/Frontend-HTML5%20%7C%20CSS3%20%7C%20JS-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)

**High-converting, responsive SaaS landing page showcasing the SnapClass AI Attendance System.**

[Live Demo](https://snapclass-landing.vercel.app) • [Deploy on Vercel](#-deployment-to-vercel) • [App Repository](../ai-attendance-project-app)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Design System & Features](#-design-system--features)
- [Directory Structure](#-directory-structure)
- [Environment Variables](#-environment-variables)
- [Local Development](#-local-development)
- [Deployment to Vercel](#-deployment-to-vercel)
- [Customization Guide](#-customization-guide)

---

## 📖 Overview

The **SnapClass Landing Page** is a lightweight, responsive SaaS website built using **Flask (Python)** and modern **Vanilla HTML5/CSS3/JavaScript**. It features custom SVG vector graphics, interactive UI showcases, smooth scrolling navigation, and direct integration with the live Streamlit attendance app.

---

## ✨ Design System & Features

- **💎 Modern SaaS Aesthetics:** Dark/light mode harmonious contrast with vibrant indigo (`#5865F2`) and hot pink (`#EB459E`) brand accents.
- **⚡ Zero Bloat:** Pure Vanilla CSS3 and JavaScript with no heavyweight frameworks, delivering near-instant page load times (100% PageSpeed score).
- **📱 Fully Responsive:** Adaptive layout for mobile phones, tablets, laptops, and ultra-wide desktop screens.
- **🍔 Interactive Mobile Navigation:** Animated slide-out hamburger menu with smooth touch handling.
- **🔗 Dynamic App Integration:** Reads the live Streamlit app URL directly from environment variables (`STREAMLIT_APP_URL`) and injects it into all Call-to-Action (CTA) buttons.

---

## 📂 Directory Structure

```
ai-attendance-project-landing/
├── app.py                         # Flask server routing and template rendering
├── vercel.json                    # Vercel deployment & WSGI configuration
├── requirements.txt               # Flask, Gunicorn & Python-dotenv dependencies
├── templates/
│   └── index.html                 # Semantic HTML5 landing page template
├── static/
│   ├── css/
│   │   └── style.css              # Custom styling, animations & glassmorphism
│   ├── js/
│   │   └── script.js              # Navbar toggles, smooth scroll, dynamic interactions
│   └── assets/                    # Optimized icons, vector SVGs, and feature graphics
└── README.md                      # This file
```

---

## 🔐 Environment Variables

Create a `.env` file in `ai-attendance-project-landing/.env` (optional for local development):

```env
# URL of your hosted Streamlit Attendance Web Application
STREAMLIT_APP_URL=https://vrundsnapclass.streamlit.app/
```

*If not provided, the application defaults to `https://vrundsnapclass.streamlit.app/`.*

---

## 💻 Local Development

### 1. Navigate to the directory:
```bash
cd ai-attendance-project-landing
```

### 2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Start the Flask server:
```bash
python app.py
```

Open **`http://localhost:5002`** in your browser!

---

## ☁️ Deployment to Vercel

The landing page is pre-configured with [`vercel.json`](file:///ai-attendance-project-landing/vercel.json) for 1-click deployment on **Vercel**:

### Steps to Deploy:

1. Log in to **[vercel.com](https://vercel.com)**.
2. Click **"Add New..."** ➔ **"Project"**.
3. Under **Import Git Repository**, select **`Vrund2007/SnapClass`**.
4. In the Project Configuration:
   - **Framework Preset:** `Flask` (Automatically detected)
   - **Root Directory:** Click **Edit** and select: 👉 **`ai-attendance-project-landing`** *(Essential since this is a monorepo!)*
5. In **Environment Variables**:
   - **Key:** `STREAMLIT_APP_URL`
   - **Value:** `https://vrundsnapclass.streamlit.app/` (or your live app link)
6. Click **Deploy!**

Your landing page will be instantly live on a fast global CDN with custom domains and free SSL!

---

## 🎨 Customization Guide

### Updating Hero Copy & Call-to-Actions:
Edit [`templates/index.html`](file:///ai-attendance-project-landing/templates/index.html) to modify titles, feature cards, testimonials, or pricing tiers.

### Modifying Brand Colors & Styling:
Edit CSS variables at the top of [`static/css/style.css`](file:///ai-attendance-project-landing/static/css/style.css):
```css
:root {
  --primary-color: #5865F2;
  --accent-color: #EB459E;
  --dark-bg: #0f172a;
  --light-bg: #f8fafc;
}
```

---

<div align="center">
Part of the <b>SnapClass</b> ecosystem.
</div>
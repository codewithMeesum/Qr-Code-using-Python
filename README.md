<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Python%20QR%20Code%20Generator&fontSize=40&fontColor=ffffff"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Project-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-Mini%20Project-purple?style=for-the-badge"/>
</p>

# 🔳 Python QR Code Generator

<p align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="90">
</p>

<p align="center">
A simple and practical <b>Python mini project</b> that generates a QR code from any URL and saves it as a <b>PNG image file</b> using external libraries.
</p>

---

#  Project Overview

This project demonstrates how to generate a QR code using Python in just a few lines of code.

It converts a URL into a QR image file that can be scanned using any smartphone camera.

Example used in this project:

```
Instagram Page → Learning Daily AI
```

Generated Output:

```
qrcode.png
```

---

# ✨ Features

✔ Generate QR code from any URL
✔ Save QR code as PNG image
✔ Lightweight Python script
✔ Uses external Python libraries
✔ Beginner-friendly automation tool

---

# 🧠 Concepts Demonstrated

| Concept          | Implementation      |
| ---------------- | ------------------- |
| Python Libraries | `qrcode`            |
| Image Processing | `Pillow`            |
| Automation       | URL → QR conversion |
| File Handling    | Saving PNG image    |

---

# 📦 Libraries Used

### 1️⃣ qrcode

Used to generate QR code from text or URL input.

Install with:

```
pip install qrcode
```

---

### 2️⃣ Pillow

Used for image processing and saving QR code as PNG format.

Install with:

```
pip install pillow
```

---

# ⚙️ How It Works

The program follows three simple steps:

1️⃣ Import the qrcode library
2️⃣ Generate QR code from URL
3️⃣ Save QR code as PNG image

---

# 🖥️ Example Code

```python
import qrcode

qr = qrcode.make("https://www.instagram.com/learningdailyai/")
qr.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
```

---

# 📂 Project Structure

```
Python_QR_Code_Generator
│
├── generate_qr.py
├── qrcode.png
└── README.md
```

---

# ▶️ How To Run

### Step 1 — Install dependencies

```
pip install qrcode
pip install pillow
```

### Step 2 — Run script

```
python generate_qr.py
```

After running the script:

```
qrcode.png
```

will be generated automatically.

---

# 🖼️ Output Preview

Add your generated QR screenshot here:

```
![QR Code Output](qrcode.png)
```

---

# 💡 Use Cases

This script can be used for:

📱 Sharing social media profiles
🌐 Website links
📂 File download links
🎓 Educational resources
📊 Quick-access project demos

---

# 🛠️ Tech Stack

<p align="center">
<img src="https://skillicons.dev/icons?i=python,vscode,git,github"/>
</p>

---

# 🌐 Connect With Me

<p align="center">

<a href="https://instagram.com/mesum_mukhtar">
<img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/>
</a>

<a href="https://leetcode.com/c2ktwf5gnt">
<img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/>
</a>

<a href="mailto:mesummukhtar3@gmail.com">
<img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/mesummukhtar/">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</p>

---

# 👨‍💻 Author

**Mesum Mukhtar**

Built as part of continuous learning and exploration in Python automation projects.

<p align="center">
⭐ If you like this project, consider giving it a star ⭐
</p>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=120&section=footer"/>
</p>

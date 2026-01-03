# Running the Face Scripts with Anaconda (Tutorial)

This tutorial explains how to run two Python scripts that:

1. **Align faces** in a set of images
2. **Draw facial landmark points** on those faces

No prior experience with computer vision is required.

---

## 1. Install Anaconda

1. Go to: [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Download **Anaconda for your operating system** (Windows / macOS / Linux)
3. Install it using the default options

After installation, you should have:

* **Anaconda Navigator**
* **Anaconda Prompt** (Windows) or **Terminal** (macOS/Linux)

---

## 2. Create a New Conda Environment

This keeps everything clean and avoids conflicts.

Open **Anaconda Prompt / Terminal**, then type:

```bash
conda create -n enviroment_name python=3.9
```

Press **Y** when asked.

Activate the environment:

```bash
conda activate enviroment_name
```

You should now see `(enviroment_name)` at the beginning of the line.

---

## 3. Install Required Libraries

Run these commands **one by one**:

```bash
conda install -c conda-forge dlib
conda install opencv numpy
pip install imutils
```

⚠️ `dlib` may take a few minutes to install — this is normal.

---

## 4. Download the Face Landmark Model

These scripts need a pre-trained face model.

1. Download this file:
   [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
2. Unzip it
3. Place the file
   `shape_predictor_68_face_landmarks.dat`
   in the **same folder** as the Python scripts

---

## 5. Organise the Project Folder

Your folder should look like this:

```
face-project/
├── face-aligner.py
├── face-points.py
├── shape_predictor_68_face_landmarks.dat
├── input/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
```

* Put **portrait photos** (JPG or PNG) inside the `input` folder
* Images should contain **one face per image**

---

## 6. Run the Face Aligner

In the terminal, navigate to your project folder:

```bash
cd path/to/face-project
```

Then run:

```bash
python face-aligner.py
```

This will:

* Detect faces
* Rotate and center them
* Save the results into a new folder called:

```
faces/
```

---

## 7. Run the Face Points Script

Now run:

```bash
python face-points.py
```

This will:

* Read the aligned faces
* Detect facial landmarks
* Draw colored points on the face
* Save the results into:

```
faces-points/
```

---

## 8. Final Output

After everything runs, you should have:

```
faces/          → normalized portraits  
faces-points/   → portraits with facial landmarks
```

These images show how a face is interpreted **not as an identity**, but as a **set of measurable points**.

---

## Common Problems (Quick Fixes)

* **Nothing happens** → Check that images are inside `input/`
* **No face detected** → Use clearer, front-facing portraits
* **dlib install fails** → Make sure Anaconda is updated:

```bash
conda update conda
```

---

## Conceptual Note (for students)

What you are running is not *face recognition*.
It is a **normalization and abstraction process**, similar to how archives:

* standardize objects
* erase context
* make comparison possible

You are watching an archive being **produced by code**.

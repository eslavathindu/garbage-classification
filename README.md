.

🗑️ Garbage Classification using CNN
A Deep Learning approach for automated waste segregation
Author: Eslavath Indu

📌 Overview
Garbage management is one of the major challenges in urban environments. This project uses Convolutional Neural Networks (CNNs) to classify waste images into various categories like plastic, paper, metal, etc., helping in smart and efficient waste segregation.

🧠 What This Project Does
Trains a CNN model to classify garbage images

Predicts the category of a new garbage image

Helps in automating waste management systems

🛠️ Tech Stack
👩‍💻 Python

🤖 TensorFlow / Keras

📊 NumPy, Matplotlib

🧠 CNN (Convolutional Neural Network)

🗂️ Project Structure
bash
Copy
Edit
garbage-classification/
├── dataset/               # Folder containing garbage images (organized by category)
├── train.py               # Model training script
├── predict.py             # Model prediction script (optional)
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
└── LICENSE                # MIT License
🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/eslavathindu/garbage-classification.git
cd garbage-classification
Install requirements

bash
Copy
Edit
pip install -r requirements.txt
Train the model

bash
Copy
Edit
python train.py
(Optional) Predict with an image

bash
Copy
Edit
python predict.py <path_to_image>
📁 Dataset
The dataset/ folder must contain subfolders like:

/plastic

/paper

/metal

/glass

etc.

Each folder must contain images related to that category.

📸 Sample Image Categories
Category	Example
Plastic	Bottles, wrappers
Paper	Newspapers, books
Metal	Cans, wires

📈 Output
Accuracy & loss plotted using matplotlib

Trained model saved as .h5 file

Ready for deployment in mobile/web

👩‍🎓 Author
Eslavath Indu
3rd Year | B.Tech | AI & ML
Malla Reddy Engineering College for Women
✉️ Email: indu01052006@gmail.com


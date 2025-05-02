# Integrating-Sign-Language-and-Visual-Aids
Sign-Language-To-Text-and-Speech-Conversion is a Python-based application designed to bridge communication gaps for the deaf and hard-of-hearing community. By leveraging computer vision and deep learning, the system translates American Sign Language (ASL) gestures into both text and speech, facilitating real-time interaction with individuals who may not be familiar with sign language.

## Key Features:
- Real-Time Gesture Recognition: Utilizes a Convolutional Neural Network (CNN) to identify ASL hand gestures captured via webcam.

- Text Output: Displays the recognized gesture as text on the screen.

- Speech Output: Converts the recognized text into audible speech, aiding communication.

- User-Friendly Interface: Designed to be intuitive, allowing seamless interaction without the need for specialized knowledge.

## Directory Structure
```

IncludeEd-Sign-Language/
├── cnn8grps_rad1_model.h5 # Pre-trained CNN model
├── final_pred.py # Main prediction script
├── prediction_wo_gui.py # Alternate prediction script without GUI
├── data_collection_binary.py # Script to collect binary data
├── data_collection_final.py # Script to collect gesture images
├── AtoZ_3.1.zip # ASL alphabet dataset
├── Output.mp4 # Sample demo video
├── IncludeEd=PROJECT_REPORT.pdf # Full project report
├── IncludeEd=PROJECT_PPT.pptx # Presentation slides
```

## Project Outputs and References
You can view the following resources directly in the repository:

- ### [Output Demo Video](https://github.com/HarshitaCnu/IncludeEd-Sign-Language/blob/main/Output.mp4)
  A video demonstration showcasing the system converting sign language gestures into both text and speech in real time.

- ### [Project Report (PDF)](https://github.com/HarshitaCnu/IncludeEd-Sign-Language/blob/main/IncludeEd%3DPROJECT_REPORT.pdf)
  A comprehensive report detailing the model architecture, dataset preparation, training methodology, and system evaluation.

- ### [Project Presentation (PPTX)](https://github.com/HarshitaCnu/IncludeEd-Sign-Language/blob/main/IncludeEd%3DPROJECT_PPT.pptx)
  A summarized slide deck presenting the project's objectives, implementation steps, results, and future enhancements.

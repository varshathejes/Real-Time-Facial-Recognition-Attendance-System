# Real-Time-Facial-Recognition-Attendance-System
A smart attendance system using real-time face recognition. It identifies individuals via webcam, checks faces against a database, and marks attendance on-screen and displays the reg no and time of attendance in console. If recognized again in the same session, it notes "Already Marked" to prevent duplicates.

aim: This project implements a real-time attendance system using facial recognition technology. The system utilizes a webcam to capture live images, processes them in the frontend, and checks against a pre-stored database of face images. Each recognized face is associated with a unique registration number (Reg No) from the database.
This project integrates facial recognition technology with Firebase to manage and track student attendance. It consists of three main Python scripts:

add_data_to_db.py: Initializes a Firebase Realtime Database and populates it with student data, including names, majors, starting years, attendance counts, and last attendance times.
encoder.py: Processes images from a designated folder to detect and encode student faces using the face_recognition library. These encodings are stored in a local file and the images are uploaded to Firebase Storage for future reference.
main.py: Implements a real-time face recognition system that captures video from a webcam, identifies known faces using the stored encodings, and updates attendance data in Firebase based on face matches. The script also handles user interface updates to display student information on-screen when a face is recognized.
This setup allows for a robust attendance tracking system that can be easily scaled and modified for different use cases, such as monitoring attendance in educational or corporate environments.
Functionality:
Face Detection and Recognition: When the system detects a face through the webcam, it attempts to recognize the face by comparing it with faces stored in the database. Attendance Marking: If a match is found, the system retrieves the corresponding Reg No and marks the attendance for that individual on the frontend display. The system also logs the attendance time and Reg No in the console. Re-attendance Handling: If the same individual appears again, the system will display a message indicating that the attendance is already marked.

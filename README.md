# Hand Gesture Recognizer
#### Recognizer for hand gestures for HackGT5

This is a recognizer for Hand Gestures, specifically 0, 1, or 2, built on Microsoft Azure Cloud Platform's Custom Vision Service Classifier API. Picture data taken from ata used only for these three values to show proof of concept behind developing such an app, but applications are far and wide from being able to dynamically type with hands, to improved accessibility for online classrooms.

In this app, the recognizer performs four simple functions: play, pause, go back, and skip by reading three hand gestures representing four states: pause is one, go back is zero, skip is two, and none of the previous represent an invalid state which is play. As a result, while watching a lecture video or some other intstructional video, the student can merely raise a finger to pause and ponder the question before just bringing their hands down to resume. For online live classrooms, this feature can be modified to perform real-time video analysis for students who can, for example, simulate raising their hands for a question by simply gesturing and grabbing the teacher's attention. While this feature can be real-time for our app by simply catching frames and making API calls, due to limitations of API calls and bandwidth strength, we instead used a manual capture button which then makes an API call and modifies the video accordingly. 

This app also can be adapted to Augmented Reality Viewers like the Microsoft Hololens and then use Azure and more extensive training set to simulate a learning environment where students see a simulated 3D environment and teachers get data from students like gestures and expressions to better understand student response. For Augmented Reality, our idea can be further trained and modified to even perform live-time American Sign Language (ASL) translation. 

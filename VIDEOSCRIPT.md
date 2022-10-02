    Name:

    Motto - Powerful message:

        

    Explanation of the UI design choices, 
        *shown on screen :
            Edit and change some cars control panel to our program and stuff:
        Emphasise that the extra information we provide is:
            Easy to understand
                One of our main goal was creating an interface that is straight forward enough for anyone to understand.
                At any situation, without any prior knowledge.
            Easy to notice
                To make sure any obtrusion is easy to notice, we used bright colours, unique textures and easy to read alerts.
            Accurate
                The visual representation of the sensor placements, car speed and traffic positions are all scaled precisely relative to our car's axlecenter
        Alert System:
            Our software implements the detection of 6 different obstacles: pedestrians, bycicles, motorbikes, cars, tracks car/track or unknown            
            Clear instructions
            Based on other products commercial succes, such as cheap chinese dashcam and volkswagen drive assistance, we made the attention you are too close to the person infront
            starting out from this idea, we thought outside the box, so if someone else tailgates you and is really close in the rear of yo car, you get some notification so u can make safe decisons and avoid sudden braking or dangerous manouvers, it is also helpful if u are overtaking someone and the person behind you also tries to do the same. 

            Distance-based alerts:
                If an object is approaching our car and passes into the alert system's trigger radius, VRHS brings the driver's attention to said object by deploying alert messages.


        Precise simulation:
            Because our system is scaled relatively to the car's axlecenter, our user can easily scale the interface to their liking. 
        Currently for the hackathons purpose/Debugging purpose:
            Menu for testing
                Start/Pause
                Load previous recordings
                Texture change
            Vehicle and object tracking data
                

    Code-Tech:
        Python:
            arcade
            csv
        Starting point:
            We tried to understand the task and the proposed task, so we discused every provided information
            we came to the conclusion that in reality the program we want wont have every data at the same time, so we handle the data with the time field and syncronize the simulation based on that.
        Paradigm:
            For better project scaling aspects we used the object oriented paradigm, so it is easy to add new features


            margin based filtering and time synchronization between databases
        

    Future prospects:
        Our focus for the hackathon was to create something complete and although we had limited time, we tried to optimalize our code as much as possible, but as always, there is room for improvement.
        For more efficient rendering
        We'd implement texture/shape batching or GPU computation for the objects being tracked.
        For faster calculations
        We'd code the heavy parts in c++ and only use python for the UI and the data handling.
        Innovative idea to also present
        We think that based on the data the camera and radar detects, it could be good to collect this data anonymusly and process it with machine learning in a way that we would have statistics about the most dangerous situations, locations and the most common moving patterns. With such proccesed data object movement prediction and danger avoidance could do a leap.
        Recording and storing tracking data matched with dashcam footage.












------------------------------------------------------------------------------------------------------------------

*Read out loud on a smoothing voice:
    Vehicle Radar Help System
    *-dramatic pause of 4s
    Keep everyone safe on the road

    We designed our software based on this principle.
    We implemented an alert system, that helps the driver notice possible dangerous situations
    before they happen.
    
    Although the userinterface might seem crude for the first sight, but it was delibertly designed to be fitted on a cars center panel. Alerts and important information is always clearly readable and it is easy to understand the situation around the car, from just a glance.

    As we vowed to provide a system that accuratly analises the situation, we implented precise simulation that scales every detail to the screen in perfect ratio.
# COVID Vaccine Appointment Search

This block of code pings chosen vaccine portals at selected intervals to check for available appointments.

To avoid issues arising from different providers having different back-end pipelines, this approach takes snapshots of the webpage and uses computer vision to extract relevant text. It then checks for a chosen flag, such as 'No appointments available' to make a decision on whether or not the portal has openings. 

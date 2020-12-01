# P1: Proposal: Catbox Command Center
Victor Allen (vwallen@uw.edu)

> **Catbox Command Center** is a data monitoring and notification unit that installs onto an existing cat litter box to provide up-to-the-minute telemetry on your cat's dirty business. 

### Overview

The CCC will use sensors to track usage and abusage of the litterbox, which will be logged and displayed on the device. The two primary sensors will be a range-finding sensor aimed to register activity inside the box and a VOC (volatile organic compounds) sensor to register cat-supplied odors. These will be contained in a housing attached to the lid of the box, along with the CPX and display. The onboard display wil be two LED strips, one registering the number of usages since the last reset, and one registering the current VOC level.

### System

![system-diagram](/Users/victor/PROJECTS/539-physical-prototyping/hcde539-a2020/final-project/system-diagram.jpg)

### Challenges

- Anything cat-related is always challenging, including this. The housing for the device needs to be strudy enough to stand up to the inevitable investigation and sitting on that will occur. All components must be shielded from investigating paws and teeth while still performing their function. The housing attach securely and hold up to any stresses that occur when the box is serviced.
- There are two options for the cat detecting sensor: a PIR motion sensor (which I have tested before) and a ultrasonic range finder. The latter seems to be more easily calibrated for this purpose and also more accurate. Research is required to test the effect of the ultrasound that close to the cats.
- Battery-life is an issue, and so consumption will need to be tested. This may require a battery pack that is easily swapped / rechargeable, or a wired connection to power.
- The storage capacity of the CPX is limited, and ideally the data collected will be possible to access / reset without dismantling the whole assembly. Exposing a USB port connected to the CPX could solve both the data and power issues.
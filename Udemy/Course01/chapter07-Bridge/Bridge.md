# Bridge

Bridge design pattern is all about connecting components together using abstraction

Why do we need this pattern?

Bridge prevents a problem called **Carterian product** complexity explosion

Bridge is a machanism that decouples an interface (hierarchy) from an implementation (hierarchy).

Lets say,
a. you have a ThreadSchedular
b. It can be preemptive or cooperative
c. IT can run on windows or linux

How do you implement it?


TreadSchedular
- Preemptive
  - Windows
  - Linux
- Cooperative
  - Windows 
  - Linux

Basically you have to implement four different rutines for that. And that is messy.

So, using bridge pattern we can make it simple

WindowsSchedular & Linux Schedular
- Platform Schedular (inherits above)
  
PreemptiveTheadSchedular & Cooperative ThreadSchedular
- ThreadSchedular (Inherits above)

TheatSchedular -> uses PlatformSchedular  

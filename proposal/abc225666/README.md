# Agar backend api

[![hackmd-github-sync-badge](https://hackmd.io/RYp6o8DmTr2QNHb7f-hbCg/badge)](https://hackmd.io/RYp6o8DmTr2QNHb7f-hbCg)


## Basic information
Github repository: https://github.com/abc225666/agar-backend-api

## Problem to solve
Agar is mini game produced by agar.io. People control a circle to competitive with other people. The larger your circle is, the more point you get and your circle is more powerful.

A circle can eat other circles to grow up if it is large enough. Circle can also split it self, send circle out for other circle. With these skill, players need to compete or corporate with others to get high points.

This project would like to supply lots of apis about Agar, like calculating circles growth, players' interaction in a map. It will involve lots of numerical techniques like circle area calculation, coordinate after moving, and scanning for circle overlapping to detect which circle will be eaten. 

## Prospective user
Users who want to build a Agar server could use these apis to decrease the workload in calculate circle's interaction.

## System architecture
#### Class `Circle`
Contains all data related to this circle, including radius, position, the user belongs to.

#### Class `User`
Contains user's data

#### Class `Map`
Contains map's information, might include maximum area of map.

#### Program Flow
When a user join the game, a circle should be assigned to him.  
After every user action, I might scan all possible changes and calculate new data for every circle.

## API description
I will design detailed API when doing project. At this time, I only simply describe what API will be there.
- Function when a user joining the game.
- When a circle eat other circle, calculate new area size of the circle.
- Moving function of a circle.
- Checking circle overlapping, if it matches the condition, one of circles will be eaten.
- Split circle, it will become **2n** circles.
- Function of sending out circles, it will make the circle become small, and a new freedom circle will be send out to map.

## Engineering infrastructure
- Public APIs (Python)
  - Supply api that user can call directly to get calculate result.
- Private APIs (C++)
  - Circle growth calculation
  - Circle eat others
  - Circle split
  - Circle send small circle into map
  - Map related function, generate freedom circles, etc.

** I supply the general design first. The detailed infrastructure will continuously add when developing.

## Schedule
- Week 7 (10/26)
  - Concluding what methods I need to implement in this project
  - Build base architecture of project
- Week 8 (11/2)
  - Implement `Map` class and `User` class
  - Design how circles will move with specific argument, like speed, split size, eating threshold ...
- Week 9 (11/9)
  - Implement function of calculating circle growth and movement
- Week 10 (11/16)
  - Implement function of circles overlapping and technical of eating other circles
- Week 11 (11/23)
  - Implement function of circles splitting and merging, and sending out circles.
- Week 12 (11/30)
  - Implement interaction between map, user and circle
- Week 13 (12/7)
  - Implement Python API front-end
- Week 14 (12/14)
  - Buffer week
  - Prepare for presentation.
- Week 15 (12/21)
  - Prepare for presentation.
# Proposal for Physics Engine

## Basic information

Implement a c++ base physics engine and use python to write a easy physical simulator.

The GitHub repository:
https://github.com/ycchan5566/Physics-Engine

## Problem to solve

Today, the number of physics engine provided by python is still small, so I decide to develop a physics engine in order to enrich the physical library of python.

## Perspective users

1. People who want to develop a game.
2. People who want to simulate physical phenomenon.

## System architecture

1. Read the input (such as: mass, velocity) from users.
2. Compute the result of collision and displacement.
3. Return the result to users.

## API description

- Simple collision detection
- Simple manifold generation
- Impulse resolution

## Engineering infrastructure

C++ codes provide the api of physical caculation, and python codes use these api to get the result then visualize the result.
The visualized result is like the graph of the change of velocity or displacement.

The components will contain:
1. Physical caculator
2. Data visualizer

Everytime I finish one function, I will commit the codes.

## Schedule

week 6 (10/26): Survey documents about physics engine
week 7 (11/02): Survey documents about physics engine
week 8 (11/09): Midterm
week 9 (11/16): Implement physics engine
week 10 (11/23): Implement physics engine
week 11 (11/30): Implement physics engine
week 12 (12/07): Implement physics engine
week 13 (12/14): Prepare presentation


## References

https://gamedevelopment.tutsplus.com/series/how-to-create-a-custom-physics-engine--gamedev-12715
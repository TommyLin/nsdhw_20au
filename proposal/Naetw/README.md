# A simple ray tracer

## Basic information

The GitHub repository: [A-simple-ray-tracer](https://github.com/Naetw/A-simple-ray-tracer)

Recently, I saw the "Ray Tracing in One Weekend" book series. It provides a thorough tutorial on how to implement a ray tracer from a simple one to a serious one. As a result, I think it is a good entry point for me who is not familiar with numerical software.

## Problem to solve

Ray tracing, a rendering technique that is a staple in the movie industry. Some visual effects are too dangerous, expensive, impractical, or time-consuming to capture on films.

Ray tracing is capable of fulfilling the needs of those optical effects by simulating them, such as [reflection](https://www.wikiwand.com/en/Reflection_(physics)), [refraction](https://www.wikiwand.com/en/Refraction), [scattering](https://www.wikiwand.com/en/Light_scattering) and [dispersion](https://www.wikiwand.com/en/Dispersion_(optics)) phenomena.

This technique involves a lot of algorithms or numerical methods such as operations of the vector (e.g., dot product), quadratic equations, trigonometric function, random number generation (for diffusion), Schlick Approximation (for attaining the reflectivity easily), etc.

## Prospective users

Applications that need to have some optical effects and is able to tolerate taking a relatively long time to render can use this library to render some imageries.

## System architecture

### The `Point3` class

This class stores geometric vectors and provides common operations of it, such as dot product.

### The `Color` class

This class stores colors (RGB) and provides a operation for writing a single pixel's color to the standard output stream in the PPM image format.

### The `Ray` class

This class describes a ray which can be thought of a formula $P(t) = A + tb$, where $A$ is the origin and `b` is the ray direction. Different $t$ moves the point along the ray to different positions.

It also provides a method for generating the color seen in the direction of a ray.

### The `HittableObject` class

This is an abstract class used to represent any kind of object that can be hit by a ray. This should provide a hit (virtual?) function that tell the result of whether the given ray hits it.

### The `Sphere` class

> Inherited from class `HittableObject`

This class describes a sphere which is often used in ray tracers since it's quite straightforward to know whether a ray hits it and it's useful for the start.

It also provides a method that calculate the surface normal for the given hit point. This would be useful when we need to shade.

### The `Camera` class

I haven't had a thorough understanding of this component in ray tracing. It seems like a pinhole (observation point) which collects the rays we need and the ray tracer will use that to render the imagery.

### The `Material` class

This class describes the material which is going to be used as an attribute of an object and the key to generate different kinds of scattered ray.

### Misc utility

Ray tracer needs some math constants such as pi, infinity and some utility functions such as translation between degree and radian. This may forms a `Math` class or just a module that places all these hard to be classified stuffs.

### Workflow

1. Have a scene that the imagery would be generated at
2. Have a "world" which describes objects that exist in the scene
3. Use a camera to get the ray that we'd like to observe
4. Use the ray got from step 3 to render the result

## API description

I may design a format for the user to describe the "world" which should be passed to the API (maybe called `generate_image` or something).

I don't have too much time for this recently. I'll leave it until I clarify how much I'm going to extend the ray tracer under the constraint of available time in this semester.

## Engineering infrastructure

For different APIs, I plan to use different testing frameworks.

- Public APIs (Python + C++)
    - pytest
- Private APIs (C++)
    - SkyPat (used before) or Catch2

As for documentation, I'm used to write the documentation first before actually writing some code if I have enough time. So, ideally, I would have a documentation which describes all the abstract information about my system. Besides, since this system is going to have a lot of formulas which is hard to be clearly represented by the code, I intend to write comments depict the formula in a more human-friendly manner for them.

As for the granularity of commits, since the design of the tutorial is great, I may follow it and make a commit for a chapter which may be adding a new module or adding a new feature for a module.

## Schedule

- Week 7 (10/26)
    - Decide how much I'm going to extend my ray tracer (includes the second book?). The following schedule may change a lot according this decision. For now, It's based on the content of the first book
    - Decide the testing framework for private APIs
- Week 8 (11/2)
    - Implement the first three class (`Point3`, `Color`, `Ray`) and corresponding unit tests
- Week 9 (11/9) (hw4)
    - Implement class `Hittable`, `Sphere` and corresponding unit tests
- Week 10 (11/16)
    - Implement class `Camera` and corresponding unit tests
- Week 11 (11/23) (hw5)
    - Implement class `Camera` and corresponding unit tests
    - Implement class `Material` and corresponding unit tests (if available)
- Week 12 (11/30)
    - Implement class `Material` and corresponding unit tests
- Week 13 (12/7) (hw6)
    - Handle some detailed physics attributes which have not been mentioned above
- Week 14 (12/14)
    - Handle some detailed physics attributes which have not been mentioned above (cont)
    - Finalize the public APIs
- Week 15 (12/21)
    - Prepare slides for presentation

## References

List the external references for the information provided in the proposal.

- [_Ray Tracing in One Weekend_](https://raytracing.github.io/books/RayTracingInOneWeekend.html)
- [Ray Tracing (Graphics)](https://www.wikiwand.com/en/Ray_tracing_(graphics))
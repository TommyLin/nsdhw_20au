# Pedometer

## Basic information

GitHub repository : [https://github.com/briansp8210/pedometer](https://github.com/briansp8210/pedometer)

In modern world, people like to quantify their activities to improve quality of life. As an app installed in virtually all smart phones, pedometer becomes one of the necessary tool. In this project, I would like to follow [this elaborate tutorial](http://aosabook.org/en/500L/a-pedometer-in-the-real-world.html) and implement a simple pedometer.

## Problem to solve

* To implement a pedometer, we need to process the given acceleration data, fetch the portion caused by regular movement, and analyze steps count from it
* Filter like infinite impulse response (IIR) can be used to extract user caused acceleration. It can also used to filter out effect from varied terrain

### Perspective users

* People who are familiar with CLI and want to get their step counts
* Developers searching for library for couting steps given sensor data

## System architecture

* Users will provide the data generated from accelerometer in their phones
* `Parser` will convert the data to a standard format, make following processing agnostic to devices
* `Processor` will perform works like filtering, etc. to get rid of external effects and get a clear signal
* `Calculator` will calculate step counts, distances, etc. from this signal
* Output these results to users

## API description

* This project will provide a completed CLI frontend for user to provide data and get results
* Other programs can invoke following C++ API to consume this service:
  * `Result pedometer_entry(const std::string &filename)`
    * `filename`: Path to the phone generated record data
    * `Result` is a structure containing data like step counts, distance, etc.


## Engineering infrastructure

* Build system
  * Make
* Testing framwork
  * For core components, I may use [googletest](https://github.com/google/googletest) to perform unit tests
  * If user interfaces part (in Python), [pytest](https://docs.pytest.org/en/stable/) will be used when tests are necessary
* Documentation
  * Currently, I only plan to write comments for classes and methods of core components
* Version Control
  * I will make a commit when completing a component

## Schedule

* Week 07 (10/26): Read the reference article thoroughly to better understand the background knowledge
* Week 08 (11/02): Implement `Parser` to standardize user input
* Week 09 (11/09): Implement `Processor`
* Week 10 (11/16): Implement `Processor`
* Week 11 (11/23): Implement `Calculator`
* Week 12 (11/30): Implement the user interface (may be in CLI) for displaying results
* Week 13 (12/07): Test my pedometer with those in Google Play
* Week 14 (12/14): Try to optimize the calculation results
* Week 15 (12/21): Prepare for oral presentation
* Week 16 (12/28): Present my project

## References

* [A Pedometer in the Real World](http://aosabook.org/en/500L/a-pedometer-in-the-real-world.html)

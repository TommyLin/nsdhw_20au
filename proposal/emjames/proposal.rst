=========================================
Proposal for Open Data Center Environment
=========================================

Basic information
=================

The GitHub repository (URL) hosting the term project:
https://github.com/emjames/open-data-center-environment

A toolkit for building data center environments and testing them with algorithms to improve data center's energy efficiency.

Problem to solve
================

This project will have a similar approach to the authors found in [2] and [3] it will also bring ideas from [1]. The main difference is that this project aims to have multiple backends available, as well as making it easier to use, test and modify different learning algorithms (think batteries included).

There exist different approaches for modeling data centers.

.. list-table:: Comparison of existing modeling approaches
   :widths: 25 50 50
   :header-rows: 1


   * - Modeling approach
     - Pros
     - Cons
   * - | eQuest
       | EnergyPlus
       | TRNSYS

     - | Conventional
       | Existing research

     - | Imperative programming
       | Math equations are interlaced with numerical solvers (written in source codes, making it difficult to maintain)
       | Difficult to support fast prototyping
       | Difficult to implement new control logic
       | Difficult to perform multi-domain simulation and integration

   * - | Physical models
       | Equations, physical laws

     - Error of 1 ~ 5%

     - | Require extensive measurements
       | Static
       | Extensive assumptions

   * - Data driven models

     - | Don't require known laws
       | Can speed up simulation
       | Simulate data center parts with ML algorithms
     - Need large datasets


The overall objective of the Open Data Center Environment project:

Make environments with different room dimensions, row configurations, fans that are readily available, extensable, and separates concerns so that algorithms and learning models can be applied to find control optimizations that can generalize to different data center environments.

Perspective users
=================

Mechanical engineers and algorithm engineers aiming to improve energy efficiency in data centers.

Users can use the existing environment implementations or create their own implementations from the examples to test new (learning) algorithms on data center environments and find optimal solutions to reduce energy consumption.

Mechanical engineers can focus on the parametrization and validity of the models and algorithm engineers can focus on the design, implementation, profiling and optimization of control algorithms.

System architecture
===================

.. image:: ./opendce_diagrams.png

API description
===============

The `OpenAI Gym <https://github.com/openai/gym>`_ API will server as a guideline to the API found in this project.

Creating a new environment
**************************

.. code-block:: python

    import opendce
    from opendce import error, spaces, utils
    from opendce.utils import seeding # seeding to make environments reproducible

    class FooEnv(opendce.Env):
        def __init__(self):
            ...
        def step(self, state, action):
            ...
        def reset(self):
            ...
        def render(self):
            ...
        def close(self):
            ...


Engineering infrastructure
==========================

Documentation
*************

After discovering reStructuredText, documentation will be generated with `Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`_ from reStructuredText documents. Each file will have a matching documentation page describing the file's objective and API in the file.

Code style guides
*****************

Code guidelines will follow Google's styleguides:

| `Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_
| `Shell Style Guide <https://google.github.io/styleguide/shellguide.html>`_

At the time of this writting Modelica style guide were not found, therefore one will be written gradually.


Version control guidelines
**************************

The ``Main`` branch will be workable tested code. New sprints will have a new working branch until tests are all passed and ready to merge into ``Main``.

For best practices refer to Chris Beams' Git commit `blog entry <https://chris.beams.io/posts/git-commit/>`_. For brevity, the *properly formated Git commit subject line* bit will be added here.

**A properly formed Git commit subject line should always be able to complete the following sentence:**


| If applied, this commit will your subject line here
| For example:
|
| If applied, this commit will ``refactor subsystem X for readability``
| If applied, this commit will ``update getting started documentation``
| If applied, this commit will ``remove deprecated methods``
| If applied, this commit will ``release version 1.0.0``
| If applied, this commit will ``merge pull request #123 from user/branch``
|
| Notice how this doesn’t work for the other non-imperative forms:
|
| If applied, this commit will ``fixed bug with Y``
| If applied, this commit will ``changing behavior of X``
| If applied, this commit will ``more fixes for broken stuff``
| If applied, this commit will ``sweet new API methods``
| Remember: Use of the imperative is important only in the subject line. You can relax this restriction when you’re writing the body.

    -- Chris Beams


Testing
*******
Testing is to be done with ``pytest``.

Schedule
========

This schedule is a **very** rough estimate of the effort needed per objective.
During the semester, each objective will be implemented via `Scrum <https://en.wikipedia.org/wiki/Scrum_(software_development)>`_. The *Objective* column represents the *Product Backlog*, the *Sprint Backlog* will be written in detail during the sprint planning, the *Sprint* will follow (5 days) and on the last day there will be a *Sprint Review*.

.. list-table::
   :widths: 15 100 50
   :header-rows: 1

   * - Week No.
     - Objective
     - Effort (hours)

   * - 42
     - Proposal
     - 12

   * - 43
     - Implement ``Server``, ``Local Fans`` and ``Server Rack`` in Modelica
     - 20

   * - 44
     - Wrap ``Server``, ``Local Fans`` and ``Server Rack`` with OMPython 
     - 10

   * - 45
     - | Calibrate and validate results with real data
       | Report progress
     - 20

   * - 46
     - Create base environment
     - 20

   * - 47
     - Implement learning algorithm
     - 20

   * - 48
     - MVP - Combine the environment with the learning algorithm
     - 20

   * - 49
     - | Implement ``Server Room``, ``Cooling Towers``, ``Air Handler Units``, ``Underfloor Plenum``
       | Report progress
     - 20

   * - 50
     - Train, test the learning algorithm with the new environment
     - 20

   * - 51
     - TBD
     - TBD



References
==========

List of external references for the information provided in the proposal.

| `OpenModelica <https://www.openmodelica.org/>`_
| `OMPython <https://github.com/OpenModelica/OMPython>`_
| `Scrum <https://en.wikipedia.org/wiki/Scrum_(software_development)>`_
| `OpenAI Gym <https://github.com/openai/gym>`_

Papers
******

.. _cite berezovskaya:

[1] *Y. Berezovskaya, C. Yang, A. Mousavi, V. Vyatkin and T. B. Minde,* **"Modular Model of a Data Centre as a Tool for Improving Its Energy Efficiency,"** in IEEE Access, vol. 8, pp. 46559-46573, 2020, DOI:`10.1109/ACCESS.2020.2978065 <https://doi.org/10.1109/ACCESS.2020.2978065>`_.

.. _cite yangfu01:

[2] *Yangyang Fu, Wangda Zuo, Michael Wetter, James W. VanGilder, Peilin Yang,* **"Equation-based object-oriented modeling and simulation of data center cooling systems,"** Energy and Buildings, volume 198, Pages 503-519, 2019, DOI:`10.1016/j.enbuild.2019.06.037 <https://doi.org/10.1016/j.enbuild.2019.06.037>`_ .

.. _cite yangfu02:

[3] *Yangyang Fu, Wangda Zuo, Michael Wetter, Jim W. VanGilder, Xu Han, David Plamondon,* **"Equation-based object-oriented modeling and simulation for data center cooling: A case study,"** Energy and Buildings, Volume 186, Pages 108-125, 2019, DOI:`10.1016/j.enbuild.2019.01.018 <https://doi.org/10.1016/j.enbuild.2019.01.018>`_

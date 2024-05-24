# Basic Model Interface Tutorial

## Overview

Welcome! This repo includes materials for a workshop called *Get your model ready for NextGen with BMI* at the 2024 [CIROH Training and Developers Conference](https://ciroh.ua.edu/devconference/). 

![image](https://github.com/SnowHydrology/bmi-tutorial/assets/32177682/f44fbb7d-1731-4413-a6c4-3c922c5d6078)

The Basic Model Interface (BMI) features a set of model interoperability and coupling functions that standardize model control across a variety of programming languages. We use BMI in the Next Generation Water Resources Modeling Framework (NextGen) to run and couple independently developed hydrologic models. In this workshop, we will gain the knowledge we need to implement BMI for enhanced model interoperability in NextGen.

The objectives for this learning module are to:

1) Detail the capabilities and key functions of the Basic Model Interface (BMI)
2) Demonstrate how to make a model BMI compliant and implement BMI functions for use in NextGen
3) Run an example model with and without BMI

## Repo Contents

We've broken this repo out into a couple directories to help you navigate the available resources and accomplish the learning objectives.

- [`examples`](examples/): Here you'll find the Jupyter Notebook and supporting data for learning BMI and running the example models. 
- [`presentation`](presentation/): This directory includes the presentation from a previous workshop called *BMI Basics for NextGen*. It has helpful information on each of the BMI functions.

## Dependencies

The `bmi-for-nextgen.ipynb` file in `examples` runs two simple temperature-index snow models developed in Python 3.9. They are:

- [`snowPy`](https://github.com/SnowHydrology/snowPy): A script-based Python model that demonstrates what **not** to do if you want to make a BMI-compliant, portable model that can be used in NextGen.
- [`snowBMI`](https://github.com/SnowHydrology/snowBMI): A modular Python model with an implementation of BMI that you can build as a package and run in NextGen. It demonstrates several of the best practices we discuss in the workshop.

In addition, you'll need:

- The [BMI Python bindings](https://github.com/csdms/bmi-python) from CSDMS
- A [Jupyter Notebook](https://jupyter.org/) installation
- `numpy`
- `yaml`
- `pandas`
- `Matplotlib`

## Installation

As noted above, you need Python (plus the noted packages) and Jupyter distributions to run the examples. Once you have those, you'll need to install the BMI Python bindings using the CSDMS instructions linked above. Next, build the `snowBMI` model according to its instructions. You're ready to go now!

## Acknowledgments

The Community Surface Dynamics Modeling System ([CSDMS](https://csdms.colorado.edu/)) group at CU Boulder created, develops, and maintains [BMI](https://csdms.colorado.edu/wiki/BMI). Some of the example code is based on their work and documentation.

NextGen is a joint effort between Lynker and the [NOAA-NWS Office of Water Prediction](https://water.noaa.gov/) (OWP), plus other federal water agencies, institutes, and contracting companies. OWP has funded NextGen development activities. 

[CIROH](https://ciroh.ua.edu/) is the Cooperative Institute for Research to Operations in Hydrology, a partnership between OWP and a consortium of universities, research institutes, and private sector companies. We thank CIROH for inviting us to deliver this workshop.






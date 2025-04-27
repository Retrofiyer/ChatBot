<div>
    <h1>ChatBot ISO14001</h1>
</div>

## About The Project

This project is an interactive chatbot built using Google's Gemini API and a simple web interface powered by Gradio. It allows users to have dynamic conversations with a state-of-the-art language model, with the added flexibility of assigning a custom role and adjusting the model's creativity via the temperature parameter.

## Table of Contents

<ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#running-the-service">Running the service</a></li>
      </ul>
    </li>
    <li>
      <a href="#contributing">Contributing</a>
    </li>
 </ol>

## Overview

The chatbot is implemented as a Python class that:
- Connects to the Gemini API using a secure API key stored in environment variables.
- Supports defining a role or person to guide the chatbot's behavior.
- Allows control over the model's creativity and variability using the temperature setting.
- Uses Gradio to provide a clean and interactive web interface where users can chat in real time.

## Features

<div>
  <ul>
      <li> <b>Custom Role Configuration:</b> Set a specific personality or context for the chatbot to follow.</li>
      <li> <b>Interactive Web UI:</b> Built with Gradio for ease of use—no frontend coding needed.</li>
  </ul>
</div>

## Built With

[![Python][python.com]][python-url]

<!-- GETTING STARTED -->
## Getting Started

## Prerequisites

Before you begin, make sure you have the following tools installed on your machine:

- **Python 3.9.5 or higher** - [Download Python](https://www.python.org/downloads/)

If you don't have any of these tools installed, follow the provided links to install them.


## Installation

1.- Clone the repository
   ```sh
   git clone https://github.com/Retrofiyer/ChatBot.git
   cd ChatBot
   ```
2.- Create a virtual environment and install dependencies
 ```sh
python -m venv .venv
.venv\Scripts\activate # On Linux, use `source .venv/bin/activate`
pip install -r requirements.txt
   ```

## Configuration

File .env:
```sh
GOOGLE_API_KEY=YOUR_API_KEY
   ```
Generate api_key on this web:

https://ai.google.dev/aistudio?hl=es-419

## Running the service

  ```sh
python run.py
   ```

## Contributing

I would like you to contribute to this project. Whether it's fixing a bug, adding a new feature or improving the documentation, your help is always welcome. Please email me at `sebitas5225@gmail.com` with all the details for improvement.

<!-- LINKS & IMAGES -->

[python.com]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/

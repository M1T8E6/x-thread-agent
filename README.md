# AI-Powered Twitter Thread Generator

This project leverages LangChain and ChatPerplexity to generate engaging, concise, and structured Twitter threads based on user input. The application utilizes a language model (```llama-3.1-sonar-small-128k-online```) and a custom prompt template to create threads ready for direct use on Twitter.

## Features
* Twitter-Specific Output: Generates numbered Twitter threads tailored for maximum engagement.
* Character Limit Compliance: Ensures each tweet is within Twitter’s 280-character limit and the entire thread stays under 25,000 characters.
* Customizable Prompt: The AI model is primed with a clear and specific system message for consistent and high-quality output.
* Seamless Integration: Built with the LangChain framework and ChatPerplexity for flexible configuration and scalability.

## Prerequisites

* Python 3.8 or above
* API key for ChatPerplexity (configured via Config.PPLX_API_KEY)

### Usage

1.	**Clone the repository:**
```bash
git clone git@github.com:M1T8E6/x-thread-agent.git
cd 
```

2.	**Download dependencies:**
```bash
pip install -r requirements.txt
```

## Customization

* Prompt Modification:
Update the system_message variable to tweak the instructions for thread generation.
* Model Configuration:
Change the model parameters (temperature, model, etc.) in the ChatPerplexity instantiation for different behavior.
* Input Integration:
Replace the static input string with a dynamic user input function for real-time interaction.

## Files

* ```notebooks/```: This folder contains Jupyter Notebook files with examples, demonstrations, or experiments related to the project. Use these notebooks to understand the implementation or test new ideas interactively.
* ```config.py```: This file defines the Config class, which is responsible for managing configuration settings for the project. Ensure your PPLX_API_KEY is correctly set here to enable interaction with the ChatPerplexity API.
* ```requirements.txt```: A list of all dependencies required to run the project. Install these using pip install -r requirements.txt to set up the environment seamlessly.

### Contribution

I welcome contributions! To contribute:
1. Fork the repository.
2.	Create a new branch for your feature or bug fix.
3.	Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

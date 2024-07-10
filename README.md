# Requirement AI SWE Generator

This is an implementation of a requirements generator AI sequence for software engineering projects. It aims in automating my 4 step process for the Analysis Phase in Software Development Lifecyle (SDLC). It analyzes inputs using NLP techniques to extract key information and organize requirements into functional and non-functional categories. The generated requirements specification document adheres to common software engineering best practices and standards.

## Table of Contents

- [Description](#description) - Detailed project overview
- [Installation](#installation) - Installation instructions
- [Usage](#usage) - Examples of usage
- [Contributing](#contributing) - How to contribute
- [License](#license) - Project license
- [Credits](#credits) - Attributions
- [Contact](#contact) - Contact info
- [Acknowledgements](#acknowledgements) - Appreciations

## Description

This AI assistant aims to automatically generate requirements for software engineering projects based on natural language project descriptions and other contextual inputs such as transcripts or documentation.

When the intial natural language project description or contextual inputs i.e. transcript of a customer's project needs are provided, it analyzes the inputs using NLP techniques to extract key entities, concepts, functional and non-functional requirements.

The steps are as follows:

1. Cleaning up contextual inputs using NLP techniques like tokenization, lemmatization, stopword removal etc.

2. Extracting key entities, concepts, functional and non-functional requirements using techniques like named entity recognition; Organizing extracted requirements into functional and non-functional categories

3. Plan the product by generating natural language requirements specification document based on extracted and organized requirements using common product planning i.e. Epics, Features, Scenarios

4. Generating natural language user stories and acceptance criteria based on extracted product planning specifications using Gherkin format i.e Given, When, Then syntax.

Key features:

- Automatic extraction of key requirements from contextual inputs
- Organization of requirements into functional and non-functional categories
- Generation of natural language requirements specification document adhering to common software engineering best practices and standards
- Automatic generation of user stories and acceptance criteria in Gherkin format from requirements specifications
- Generate user stories in the format:

```markdown
As a <user type>
I want to <goal/desire>
So that <benefit>

Acceptance Criteria:

Given <precondition>
When <action>
Then <outcome>
```

- Breakdown generated requirements into user stories using common practices like INVEST criteria, gheriken and several work items outlined in [project-models.md](docs/project-models.md)

# Endpoints

| Method | Endpoint                        | Description                                                                                                                                                                 |
| ------ | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POST   | /upload/request                 | User should be able to upload request with title and description, uploaded file, document(pdf,docx, excel, csv, markdown) for generation with other actions to be performed |
| POST   | /upload/:projectId/requirements | User should be able to upload requirements document or text, title, description document(pdf,docx, excel, csv, markdown) as starting point for generation                   |
| POST   | /upload/:projectId/featurelist  | User should be able to upload featurelist document(pdf,docx, excel, csv, markdown) or text, title, description as starting point for generation                             |
| POST   | /upload/:projectId/stories      | User should be able to upload user stories as a document(pdf,docx, excel, csv, markdown) or text, title, description as starting point for generation                       |
|        |                                 |                                                                                                                                                                             |

## Installation

Provide step-by-step instructions for setting up and running the project.

1. Clone the repository

```bash
git clone https://github.com/javaniecampbell/requirements-generator.git
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

OR conda

```bash
conda init && conda create -n <environment> -f environment.yml
```

3. Activate the virtual environment:

Linux/Unix

```bash
source venv/bin/activate
```

OR Windows

```bash
& venv/Scripts/Activate.ps1
```

4. Activate the virtual environment via conda:

```bash
conda init && conda activate <environmnt>
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Set environment key from [OpenAI API](https://platform.openai.com/api-keys)

```bash

export OPENAI_API_KEY="sk-yourkey"

```

OR create `.env` file and add:

```env
OPENAI_API_KEY="sk-yourkey"
```

7. For observability, run the following before running the main.py:

```bash
docker run -p 6006:6006 -i -t arizephoenix/phoenix:latest -d
```

8. Run the project

```bash
python main.py
```

## Usage

**_Show examples of project usage with code snippets, screenshots, examples, etc._**

See [requirements.md](requirements.md) for an example of what was generated.

## Contributing

Explain how others can contribute - issues, feature requests, pull requests etc. Provide guidelines.

## License

This project is licensed under the **TBA** License. I have yet to determine the appropriate license for this project. This project is currently my personal and intellectual property until further notice, and I welcome feedback on the appropriate open source license that allows for attribution to the contributors and prohibits commercial use without attribution.

Contact for permission to use this project commercially, within your own project or for any other inquiries can be made by submitting an issue

## Credits

List contributors, related projects, tutorials, inspirations etc will be listed here.

[![requirements-generator contributors](https://contrib.rocks/image?repo=javaniecampbell/requirements-generator)](https://github.com/javaniecampbell/requirements-generator/graphs/contributors)

## Contact

For questions, support, bug reports - github issues can be submitted.

## Acknowledgements

Recognize any projects or people who inspired or helped will be added to this list.

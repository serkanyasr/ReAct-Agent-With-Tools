<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>REACT-AGENT-WITH-TOOLS</h1>
<p align="left">
	<em>Empowering AI with Reason, Action, and Tools!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/serkanyasr/ReAct-Agent-With-Tools?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/serkanyasr/ReAct-Agent-With-Tools?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/serkanyasr/ReAct-Agent-With-Tools?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/serkanyasr/ReAct-Agent-With-Tools?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)


</details>
<hr>

## 📍 Overview

ReAct-Agent-With-Tools is an innovative open-source project designed to enhance language learning through interactive AI. It combines language learning models, search engines, and image production models in a user-friendly interface. The project offers unique features like image generation from text prompts and webpage content extraction, making it an invaluable tool for educators, students, and language enthusiasts. Its Dockerized environment ensures consistent operation across different platforms, making it accessible and easy to use for everyone.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>The project is structured around a Python-based environment.</li><li>The main entry point is `app/app.py` which orchestrates the interaction between different models and manages user input and AI responses.</li><li>The `app/tools.py` module serves as a utility hub, providing functions for image generation and webpage content extraction.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>The code is well-structured and modular, facilitating easy maintenance and scalability.</li><li>It leverages Python's capabilities for clear and concise code.</li><li>The use of Docker ensures consistent operation across different computing environments.</li></ul> |
| 📄 | **Documentation** | <ul><li>The primary language used is Python.</li><li>There are clear instructions for installing and using the project with `pip` and `docker`.</li><li>Testing commands are also provided.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>The project integrates with Docker for containerization.</li><li>It uses `pip` for package management.</li><li>It leverages OpenAI's DALL·E 3 and Stability AI's Stable Diffusion XL models for image generation.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The project is divided into separate modules for different functionalities.</li><li>`app/app.py` serves as the main entry point, while `app/tools.py` provides utility functions.</li></ul> ||
| ⚡️  | **Performance**   | <ul><li>The use of Docker ensures consistent performance across different environments.</li><li>Specific performance metrics or benchmarks are not mentioned in the provided context.</li></ul> |
| 🛡️ | **Security**      | <ul><li>The use of Docker provides isolation, enhancing security.</li><li>Specific security measures or practices are not mentioned in the provided context.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>The project depends on Docker and Python 3.12.</li><li>Dependencies are managed with `pip` and listed in `app/requirements.txt`.</li><li>It includes various language processing libraries and utilities for environment management, web scraping, and HTTP requests.</li></ul> |
| 🚀 | **Scalability**   | <ul><li>The modular structure of the code facilitates scalability.</li><li>The use of Docker allows for easy deployment and scaling.</li></ul> |

---

## 📁 Project Structure

```sh
└── ReAct-Agent-With-Tools/
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── app
    │   ├── app.py
    │   ├── requirements.txt
    │   └── tools.py
    └── img
        ├── ai_agent_banner.png
        └── generated_image_20250224_172205.png
```


### 📂 Project Index
<details open>
	<summary><b><code>REACT-AGENT-WITH-TOOLS/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- The Dockerfile sets up a Python-based environment, copies the application into the container, installs necessary dependencies from the requirements file, and runs the Streamlit application<br>- It ensures the application is containerized and isolated, facilitating consistent operation across different computing environments.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/master/app/app.py'>app.py</a></b></td>
				<td>- App/app.py serves as the main entry point for the LangChain application, orchestrating the interaction between different language learning models (LLMs), search engines, and image production models<br>- It configures and executes the ReAct (Reason-Action) Agent based on user selections, manages chat history, and handles user input and AI responses within a Streamlit interface.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/master/app/tools.py'>tools.py</a></b></td>
				<td>- The app/tools.py module in the project serves as a utility hub, providing functions for image generation and webpage content extraction<br>- It leverages OpenAI's DALL·E 3 and Stability AI's Stable Diffusion XL models to generate images based on text prompts<br>- Additionally, it offers a tool to fetch and analyze webpage content, returning plain text limited to 4000 characters.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/master/app/requirements.txt'>requirements.txt</a></b></td>
				<td>- App/requirements.txt outlines the necessary dependencies for the project<br>- It includes various language processing libraries like langchain, langchain-community, and langchain-openai, among others<br>- Additionally, it specifies utilities for environment management (python-dotenv), web scraping (beautifulsoup4), and HTTP requests (requests, httpx)<br>- The specific versions of httpx and anthropic are also defined to prevent potential conflicts.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with ReAct-Agent-With-Tools, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Installation

Install ReAct-Agent-With-Tools using one of the following methods:

**Build from source:**

1. Clone the ReAct-Agent-With-Tools repository:
```sh
❯ git clone https://github.com/serkanyasr/ReAct-Agent-With-Tools
```

2. Navigate to the project directory:
```sh
❯ cd ReAct-Agent-With-Tools
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r app/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t serkanyasr/ReAct-Agent-With-Tools .
```




### 🤖 Usage
Run ReAct-Agent-With-Tools using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```






## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/serkanyasr/ReAct-Agent-With-Tools/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/serkanyasr/ReAct-Agent-With-Tools/issues)**: Submit bugs found or log feature requests for the `ReAct-Agent-With-Tools` project.
- **💡 [Submit Pull Requests](https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/serkanyasr/ReAct-Agent-With-Tools
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/serkanyasr/ReAct-Agent-With-Tools/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=serkanyasr/ReAct-Agent-With-Tools">
   </a>
</p>
</details>

---

## 🎗 License


This project is licensed under the MIT License.For more details, refer to the [LICENSE](https://github.com/serkanyasr/ReAct-Agent-With-Tools/blob/main/LICENSE) file.

---

🛠️ What is GitHub Actions?
GitHub Actions is a tool that helps you automate tasks (like testing code, deploying apps, etc.) every time something happens in your GitHub repository.

💡 Example use cases:
Automatically run tests when you push code.
Build your project and deploy it when you merge to the main branch.
Schedule tasks (e.g., daily backups).
It works by using workflows, which are YAML files stored in .github/workflows/.

📝 What is YAML?
YAML (YAML Ain’t Markup Language) is a human-readable data format. It's used to configure many tools—GitHub Actions included.

✨ Key YAML Syntax Rules:
Indentation matters! Use spaces, not tabs.
Start with name:, on:, and jobs: in GitHub Actions.
Use - to create lists.


🧠 What Is a GitHub Actions Workflow?
It's a set of steps you write in a .yml file that GitHub runs automatically when something happens in your repo (like pushing code).
Think of it like setting up a robot: “When I do X, please do Y, Z, and A for me.”

✅ Full Breakdown of YAML Terms
Here’s the workflow you ran:

'''
name: Hello World Workflow

on: [push]

jobs:
  say_hello:
    runs-on: ubuntu-latest

    steps:
      - name: Say Hello
        run: echo "This is my first automation!"

      - name: Checkout code
        uses: actions/checkout@v3

      - name: Print Hello
        run: echo "Hello from GitHub Actions!"

      - name: Print Date
        run: date

      - name: List Files
        run: ls -la
        '''
        
Let’s explain each part:

🔷 name: Hello World Workflow
This is just the name of your workflow.
You’ll see this name in the Actions tab when it runs.

🔷 on: [push]
Tells GitHub: “Run this workflow when I push code to the repo.”
You can also use on: pull_request, on: schedule, etc.

🔷 jobs:
A job is a group of steps that run together.
You can have multiple jobs (e.g., build, test, deploy).

🔷 say_hello:
This is the name of your job. You can name it anything.
Everything inside this block is part of the job.

🔷 runs-on: ubuntu-latest
Tells GitHub which machine to use to run your steps.
GitHub gives you a free virtual computer called a runner.
ubuntu-latest is a Linux machine that runs your code.

🔷 steps:
A job has multiple steps.
Each step does one thing, like print a message, run code, or copy files.

🔷 - name: Say Hello
A human-friendly label for the step (you'll see this in the logs).
Helps you identify what each step is doing.

🔷 run: echo "..."
Tells GitHub to run a command in the terminal (like Linux shell).
echo just prints a message.
Other run: commands include python3, npm install, ls, etc.

🔷 uses: actions/checkout@v3
This is very important!
uses: means you are using someone else’s reusable code called an action.
actions/checkout@v3 is a pre-made action by GitHub.
It pulls (checks out) your code from the repo into the runner so later steps can access your files.
📌 Without this, your script wouldn’t be able to see example.txt or Example.py!

💡 So How Does This Automate Things?
When you push code:
GitHub sees the push
It finds your .github/workflows/hello-world.yml
It reads your steps one by one
It spins up a free Linux computer
It runs your commands for you automatically — like:
Printing messages
Running scripts
Building code
Running tests
Deploying apps
No need to do it manually every time!

✅ Summary: Key YAML Keywords
Term	Meaning
name:	Name of your workflow or step
on:	What triggers the workflow
jobs:	Group of tasks to be run
runs-on:	The machine (OS) your code runs on
steps:	A list of tasks inside a job
run:	Run a shell/terminal command
uses:	Use a pre-built action (like checkout)

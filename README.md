##  This is the python app 2

Github Actions -> CI/CD Pipeline :

GitHub Actions is a powerful automation tool built directly into GitHub, allowing developers to automate, customize, and run workflows directly from their repositories. It supports CI/CD, automates testing, deployment, and other development tasks, and integrates seamlessly with the GitHub ecosystem. With GitHub Actions, developers can create workflows triggered by events in their repositories, such as pushes, pull requests, or issues.

![image](https://github.com/user-attachments/assets/e4b7bdf6-6b0e-4fbb-8467-ca07cd130f86)

CI/CD Pipeline :

CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery). It's a set of practices and tools designed to improve the software development process by automating builds, testing, and deployment, enabling you to ship code changes faster and reliably.

Continuous integration (CI): Automatically builds, tests, and integrates code changes within a shared repository

Continuous delivery (CD): automatically delivers code changes to production-ready environments for approval

Continuous deployment (CD): automatically deploys code changes to customers directly.

![image](https://github.com/user-attachments/assets/6cfbc3fd-1480-42ff-acaa-d72e66906009)

WorkFlow :

A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
Workflows are defined in the (.github/workflows) directory in a repository. A repository can have multiple workflows, each of which can perform a different set of tasks such as:

-> Building and testing pull requests.

-> Deploying your application every time a release is created.

-> Adding a label whenever a new issue is opened.

Key Stages :

1. Coding -> IDE(VS code, Pycham, Jupiter Notebook) should contain Coding standards & best practise.
2. Version Control -> Git - (Manage the codebase, allow multiple developers to collaborate)
   Commit
   Branch
   Push
   Pull
   Resolve Conflict
3. Code Review ->

![image](https://github.com/user-attachments/assets/cd80d42b-e3bd-47ca-b359-252fbffd1ed9)


   |-------->|

   |<--------|

main  --------  new branch

5. Testing -> Automated testing
   -> Unit testing
   -> Integration testing
   -> End to end Test Cases

6. Continous Integration (CI) -> Buliding,Testing->Notified->Fixing the issues
7. Continous Deployment (CD) -> Deploy different server (QA,UAT)


Benefits of a Developer Workflow :

GitHub Actions workflows are automated processes that can help with software development tasks like building, testing, and deploying. Some benefits of GitHub Actions workflows include: 

1. Automation = You can automate tasks within your GitHub repository, such as: 
   -> Building and testing pull requests. 

   -> Deploying an application after a release. 

   -> Adding a label to an issue. 

   -> Running arbitrary code on a repository when an event occurs.
    
3. Reusable actions = You can use actions from the GitHub Marketplace or create your own actions. 
4. Compatibility = GitHub Actions is compatible with all programming languages and can run on public clouds and local servers. 
5. Workflows based on YAML files = You can define workflows in the .github/workflows directory in a repository. 
6. Triggering = You can trigger workflows manually, at a defined schedule, or when an event occurs in your repository. 
7. Hosted runners = GitHub Actions offers hosted runners for Linux, MacOS, Windows, ARM, and Containers.

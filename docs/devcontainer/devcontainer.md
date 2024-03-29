---
layout: default
title: Develop in Container
nav_order: 2
permalink: /docs/devcontainer
has_children: true
has_toc: false
---

# Develop in Container

Welcome to the world of development containers! Whether you're a seasoned statistician or just starting your journey, development containers through Docker provides a powerful and flexible solution for creating reproducible and isolated environments for your data analysis and statistical modeling projects. With development containers, you can effortlessly set up and manage pre-configured environments that contain all the necessary dependencies, libraries, and tools, ensuring consistent results across different systems whether on your local laptop or remote server.  The following tutorials provide instructions for development container setup, management, and customization.

{: .note }
It is enouraged to use dev containers through [remote servers such as Alta](/docs/computing/department-sources#alta).

----

## Setup 

### [PSTAT User Account Sign-up](/docs/devcontainer/new-accounts)
{: .d-inline-block }
New Users
{: .label .label-yellow }

New users or users attempting to add new machines, start here.

### [Basic Container Usage on Alta](/docs/devcontainer/basic-usage/)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers how to:
- connect to Alta
- set up your project files
- access Jupyterhub and RStudio
- install packages
- log into GitHub

<!-- ## Initial Setup

### 1. [SSH Setup](/docs/devcontainer/ssh-setup/)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers how to:
- set up SSH keys
- manage keys 
- connect to remote servers via terminal
- set up GitHub SSH keys for repository access

### 2. [VS Code Setup](/docs/devcontainer/vscode-setup/)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers:
- basic VS Code configuration 
- connecting to remote servers via VS Code 
- customizing languages, packages, and system through Dockerfile templates
- initial dev container setup

### 3. [Local Setup](/docs/devcontainer/local-setup/) 
{: .d-inline-block }
Optional
{: .label }
{: .d-inline-block }

This tutorial covers:
- local Docker installation
- Docker configuration -->

## Management

### [Containers Management](/docs/devcontainer/container-management/)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers:
- basic container commands
- starting/attaching/detaching/stopping containers

### [Files](/docs/devcontainer/file-management/)

This tutorial covers:
{: .mt-6}
- moving files around between remote and local instances
- GitHub repository cloning and basic management

### [Jobs](/docs/devcontainer/job-management/)

This tutorial covers:
{: .mt-6}
- background job management
- basic terminal multiplexer (`tmux`) usage for persistant terminal sessions
- running background jobs while disconnected from server and/or container

## Additional Features

### [Editing Dockerfile](/docs/devcontainer/editing-dockerfile/)

This tutorial covers:
{: .mt-6}
- advanced customization of Dockerfile

### [GitHub Codespaces](/docs/devcontainer/github-codespaces/)

This tutorial covers:
{: .mt-6}
- getting the GitHub Developer Pack
- running Codespaces
- using Codespaces with VS Code

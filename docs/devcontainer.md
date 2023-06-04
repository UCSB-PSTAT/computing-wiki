---
layout: default
title: Develop in Container
nav_order: 2
has_children: true
has_toc: false
---

# Develop in Container

Welcome to the world of development containers! Whether you're a seasoned statistician or just starting your journey, development containers through Docker provides a powerful and flexible solution for creating reproducible and isolated environments for your data analysis and statistical modeling projects. With development containers, you can effortlessly set up and manage pre-configured environments that contain all the necessary dependencies, libraries, and tools, ensuring consistent results across different systems whether on your local laptop or remote server.  The following tutorials provide instructions for development container setup, management, and customization.

----

## Initial Setup

### 1. [SSH Setup](./ssh-setup)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers how to:
- set up SSH keys
- manage keys 
- connect to remote servers via terminal
- set up GitHub SSH keys for repository access

### 2. [VS Code Setup](./dev-container-vscode)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers:
- basic VS Code configuration 
- connecting to remote servers via VS Code 
- initial dev container setup

### 3. [Local Setup](./devcontainer.html#3-local-setup) 
{: .d-inline-block }
Optional
{: .label }
{: .d-inline-block }
Coming soon
{: .label .label-yellow }

This tutorial covers:
- local Docker installation
- Docker configuration

## Management

### [Containers Usage](./dev-container-management)
{: .d-inline-block }
Essential
{: .label .label-green }

This tutorial covers:
- basic container commands
- starting/attaching/detaching/stopping containers

### [Files](./file-management)

This tutorial covers:
{: .mt-6}
- Moving files around between remote and local instances
- GitHub repository cloning and basic management

### [Jobs](./job-management)

This tutorial covers:
{: .mt-6}
- background job management
- basic terminal multiplexer (`tmux`) usage for persistant terminal sessions
- running background jobs while disconnected from server and/or container

## Customization

### [Editing Dockerfile](./devcontainer.html#6)
{: .d-inline-block }

Coming soon
{: .label .label-yellow }

This tutorial covers:
- customizing languages, packages, and system through Dockerfile templates
- advanced customization of Dockerfile

----
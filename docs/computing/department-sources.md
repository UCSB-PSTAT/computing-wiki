---
layout: default
title: Department Sources
nav_order: 1
permalink: /docs/computing/department-sources
parent: Computing Resources
has_toc: false
---

# Department Computing Resources

The following are servers available to the PSTAT department.

## Alta
{: .d-inline-block }
Recommended
{: .label .label-green }

Alta is the latest and greatest in PSTAT department's research computing offerings geared for usage with development containers and VS Code. It contains the following specs:
- 1x24 Intel Xeon @ 2.90GHz (24 total cores)
- 202 GB RAM

To access:
- Requires completion of the [department user sign-up process](https://computing.pstat.ucsb.edu/docs/devcontainer#setup).
- Connect command: `ssh <username>@alta.pstat.ucsb.edu`

## Sandbox

{: .highlight }
This system is for testing and available at request.

A GPU powered server with a Nvidia Tesla V100. Uses the same development container configuration as Alta.
- 1x16 Intel Xeon @ 2Ghz (16 total cores)
- Tesla V100-SXM2-32GB
- 64 GB RAM

To access:
- Connect command: `ssh <username>@sandbox.pstat.ucsb.edu`

## Roble

{: .highlight }
This system is for specific grant use only.

To access:
- Connect command: `ssh <username>@roble.pstat.ucsb.edu`

## SciFi

{: .highlight }
This system is for specific grant use only.

To access:
- Connect command: `ssh <username>@scifi.pstat.ucsb.edu`

## Denali

Denali is the previous iteration of the PSTAT department server with Alta serving as the replacement.  It contains the following specs:
- 2x10 Intel(R) Xeon(R) Platinum 8268 CPU @ 2.90GHz (20 total cores)
- 128 GB RAM

To access:
- Connect command: `ssh <username>@denali.pstat.ucsb.edu`
- Make sure you're connected to the [Campus VPN](https://www.ets.ucsb.edu/network-infrastructure-services/ivanti-secure-access-campus-vpn)
- Use your [department account login](/docs/department#department-server-accounts)
- Complete the [SSH Setup](/docs/devcontainer/ssh-setup) to generate and transfer your SSH keys

## Perelandra

{: .highlight }
Perelandra is no longer accepting new users and is only available to existing research groups.  Please use Denali for your computation needs.

PSTAT departments dedicated RStudio server.

To access:
- Connect command: `ssh <username>@perelandra.pstat.ucsb.edu`
- Available via [https://perelandra.pstat.ucsb.edu/rstudio](https://perelandra.pstat.ucsb.edu/rstudio)
- Make sure you're connected to the [Campus VPN](https://www.ets.ucsb.edu/network-infrastructure-services/ivanti-secure-access-campus-vpn)
- Complete the [SSH Setup](/docs/devcontainer/ssh-setup) to generate and transfer your SSH keys

{: .note }
Regarding RStudio Stuck Processes: To fix this, login into RStudio server using the terminal command above and issue the following commands: `rstudio-server active-sessions` and `pkill -u <username>`

## Wavelet

{: .important }
This system is offline for specific grant use only.

To access:
- Connect command: `ssh <username>@wavelet.pstat.ucsb.edu`

## RAS Cluster

{: .important }
As of Spring 2023, the RAS Cluster is being decomissioned and its resources are being redistributed towards other PSTAT systems.

Utilizing VMware, Windows server and [Parallels RAS](https://www.parallels.com/products/ras/remote-application-server/) software we've added a new research cluster. This cluster utilizes virtualized GUI statistical software like: R, Matlab and SAS to do research. All running jobs are load balanced over the entire cluster giving your jobs peak performance. You can easily start a job on your office computer then disconnect leave and at anytime reconnect to the existing running job from either another computer, laptop, tablet or even from your phone.  Running these applications requires specialized accounts on the cluster, to request one for yourself please click [HERE](https://regulation.pstat.ucsb.edu/ras/request_account.htm). To request access for a group please have each member of the group make an individual request and put in the project title field, your group project name.

Make sure to download the [RAS client software](https://www.parallels.com/products/ras/download/client/) for either Windows, Mac, Linux, iOS, Android, Chrome or Windows Phone. This is required to optimize your virtualized application performance.

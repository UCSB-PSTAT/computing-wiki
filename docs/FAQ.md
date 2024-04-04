---
layout: default
title: Frequently Asked Questions
nav_order: 5
permalink: /docs/faq
has_children: false
has_toc: false
---

# Frequently Asked Questions

## Development

### Q: Can I connect multiple VS Code windows to a single container?

Yes! With your two windows open do the following on each:

1. Connect both VS Code windows to the same host.
2. Using one of the windows, open your project.
3. Once your project is open, either build the container or reopen in the container.
4. (Optional) To verify the current container name, type `docker ps`.
4. Using your 2nd window, press the remote connections button (bottom left corner).
5. Select the option "Attach to Running Container..." and follow through the dialogues to select the container running in the other window (if necessary, check step 4.).

You now have 2 VS Code windows connected to the same container!

For more details, refer to [this step in the container management tutorial](/docs/devcontainer/container-management/#2).

### Q: How do I run a long running job in the background on a server?

This is assuming that you are using a dev container or an operating system with `tmux` installed.  Here are quick start steps:

1. In your terminal, type and run `tmux`.
2. Now run your long running job.
3. Run `tmux detach` to detach from the tmux session.
4. Feel free to disconnect from the server (but leave your devcontainer running!)
5. Reconnect to the server and reattach to the devcontainer.
6. Run `tmux attach`
7. Your job will either be there running or completed!

For more details, refer to [this step in the job management tutorial](/docs/devcontainer/job-management/#3).

### How do I enable parallel processing for R?

In order to have access to parallel computation for models that can take advantage of it, install the `doParallel` package. This will allow you to enable usage of multiple [CPU cores/threads](https://unix.stackexchange.com/a/88285) with only a couple commands.  

Use this command to detect the total number of cores/threads available on your system:

```
parallel::detectCores()
```

Then, use the following library to select a desired number of cores/threads (in this case 4):

```
library(doParallel)
registerDoParallel(cores=4)
```

{: .warning }
Please be conscious of the resources available on shared systems.  **Do not hog resources!**

Additional information about available parallel computing tools in R can be found on [CRAN](https://cran.r-project.org/web/views/HighPerformanceComputing.html).
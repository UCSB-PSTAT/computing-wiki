---
layout: default
title: Computing Resources
nav_order: 3
permalink: /docs/computing
has_children: true
has_toc: false
---

# Computing Resources

## Remote Computing Sources

There 3 different levels of remote supercomputing available to PSTAT faculty/staff/students:

#### [**Department**](/docs/computing/department-sources)
- Available to everyone with minor caveats

#### [**University**](/docs/computing/university-sources)
- Available through your research PI

#### [**External**](/docs/computing/external-sources)
- Available through simple application or external funding

## Parallel Processing Using R

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

---
layout: default
title: "New Device Access"
parent: "Develop in Container"
nav_order: 1
permalink: docs/devcontainer/new-devices/
---

## Introduction

In this tutorial, you will go through adding the SSH keys stored in your Google Drive to a new device in order to gain access to a server.

**If you run into any issues, please ask for help in the**[**PSTAT Research Computing Users**](https://chat.google.com/room/AAAAR6wMcN0?cls=7)**Google Group!**

### Prereqs

- Terminal access

### Useful Links

[Google Docs Version of Tutorial](https://docs.google.com/document/d/1thskdRPZvwvL-bhyiI3_VxCRAutCms1xQ_mwOis6pkQ)

![](img/2ba8463b328120da.png)
![](img/2ba8463b328120da.png)


## Adding SSH Keys - Windows

1. First, download your SSH keys from your Google Drive to your "Downloads" folder.
2. Press Start and search for "Windows Powershell". Click on it to open a new shell.
3. Next, run the following command to create a directory called `.ssh`:

```
new-item $HOME\.ssh -ItemType Directory
```

{: .warning }
**Note:** You may get an error saying "new-item : An item with the specified name ...\.ssh already exists.". If you do, you can proceed to the next step since the directory is already there!

4. Move your SSH keys from the "Downloads" folder to the ".ssh" folder using the following commands:

```
Move-Item -Path $HOME\Downloads\ed25519.pub -Destination $HOME\.ssh\ Move-Item -Path $HOME\Downloads\ed25519 -Destination $HOME\.ssh\
```

5. From here [follow steps 4-7 found at this link](/docs/devcontainer/new-accounts/#1) in order to *setup SSH agent*and *add your key to your SSH agent's keyring*. **You do not need to generate new SSH keys, skip the ssh-keygen steps!**


## Adding SSH Keys - macOS/Linux

1. First, download your SSH keys from your Google Drive to your "Downloads" folder.
2. Find your terminal application and open up a new shell:

- macOS: `⌘` + `space`, then search "terminal"
- Ubuntu: `ctrl` + `alt` + `t`

3. Run the following command to make sure that you create a directory called `.ssh`:

```
mkdir ~/.ssh
```

{: .warning }
**Note:** You may get an error saying that a directory file already exists. If you do, you can proceed to the next step since the directory is already there!

4. Move your SSH keys from the "Downloads" folder to the ".ssh" folder using the following commands:

```
mv ~/Download/ed25519.pub ~/.ssh/ mv ~/Download/ed25519 ~/.ssh/
```

5. In order for you to add these files to your keyring in the next step, run the following command to update the file permissions of the keys:

```
chmod 600 ~/.ssh/ed25519
```

6. From here [follow steps 3-4 found at this link](/docs/devcontainer/new-accounts/#2) in order to *enable SSH agent* and*add your key to your SSH agent's keyring*. **You do not need to generate new SSH keys, skip the ssh-keygen steps!**


## Conclusion

{: .note }
You are now ready to reconnect to your server(s)! Simply follow the [steps found here](/docs/devcontainer/basic-usage/#1) in order to reconnect to your server! If you have any connection issues, checkout the [troubleshooting steps here](/docs/devcontainer/troubleshooting).


**Next up:** continue on to [the related wiki page](/docs/devcontainer#setup).
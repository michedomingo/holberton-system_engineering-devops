# 0x0B. SSH

<details><summary>Project Requirements ☑️</summary>
...
</details>

<details><summary>Resources 💡</summary>

* [What is a (physical) server - text](https://intranet.hbtn.io/rltoken/PXE-o9DWronMp4ETwADOpg)
* [What is a (physical) server - video](https://intranet.hbtn.io/rltoken/IfLc3lxSs4w5xdsFlRDPWw)
* [SSH essentials](https://intranet.hbtn.io/rltoken/qKJi0RXLqaCLkHLCLhiYNA)
* [SSH Config File](https://intranet.hbtn.io/rltoken/DNiFD9w9Gx0mnQk5nXbtjg)
* [Public Key Authentication for SSH](https://intranet.hbtn.io/rltoken/ZBYjVLcJ-ck-CFjndgSDBw)
* [How Secure Shell Works](https://intranet.hbtn.io/rltoken/SW2m2e0KMA2K1dXk_0M0CA)
* [SSH Crash Course](https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg)
</details>

#### Learning Objectives 🤓

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  #!/usr/bin/env bash instead of /bin/bash 

---
## Tasks

### [0. Use a private key](./0-use_a_private_key)
<details><summary>...</summary><br>

* Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
```

```
</details>

### [1. Create an SSH key pair](./1-create_ssh_key_pair)
<details><summary>Write a Bash script that creates an RSA key pair.</summary><br>

* 
```

```
</details>

### [2. Client configuration file](./2-ssh_config)
<details><summary>Share your SSH client configuration in your answer file.</summary><br>

* Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password.
```

```
</details>

### [3. Let me in!](./4-puppet_ssh_config.pp)
<details><summary>Add the SSH public key below to your server so that we can connect using the ubuntu user.</summary><br>

* Now that you have successfully connected to your server, we would also like to join the party.
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```
</details>
---

## Author
[Michelle Domingo](https://github.com/michedomingo)

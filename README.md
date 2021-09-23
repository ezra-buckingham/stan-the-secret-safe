# Stan the Supervisor

<img height ="250" width="250" src="https://avatars.githubusercontent.com/u/15990069?s=280&v=4"/>
<img height ="250" width="250" src="https://logos-download.com/wp-content/uploads/2016/10/Ansible_logo-700x700.png"/>

A more robust Bitwarden integration for Ansible (Forked from https://github.com/c0sco/ansible-modules-bitwarden).

## Installation

The easiest way to install this lookup plugin is to use the
`ansible-galaxy` command

```
ansible-galaxy install git+https://github.com/ezra-buckingham/stan-the-supervisor
```

This will place the `stan-the-supervisor` role into
`$HOME/.ansible/roles`, where it will be available to all playbooks
you run on your system.

## Lookup plugin

To use this plugin, you will need to activate it by including the role
in your play.  For example:

```yaml
 - hosts: localhost
   roles:
   - stan-the-supervisor
```

Use Ansible's `lookup()` function with the `bitwarden` argument, 
followed by the `action` named argument and the action's required 
arguments. If you need to specify the path to the Bitwarden CLI
binary, use the `path` named argument. Additionally, if you want
to sync the vault before running the commands, add the `sync=True`
keyword argument.

## Actions

These are actions that have been built into `stan-the-supervisor` and if
you see an action you would like, make a pull request.

### create

Create an item as defined in the BitWarden CLI documentation.

Required Arguents:
- lorem

### get

Get an item as defined in the BitWarden CLI documentation.

Required Arguents:
- lorem

### delete

Delete an item as defined in the BitWarden CLI documentation.

Required Arguents:
- lorem

### generate

Generate an item as defined in the BitWarden CLI documentation.

Required Arguents:
- lorem


## Uninstallation

To uninstall run:

```
ansible-galaxy remove stan-the-supervisor
```

<h1 align="center">Welcome to Wekan-GUI-App for wekan tools 👋</h1>
<p></p>

## Prerequisites

<% projectPrerequisites.map(({ name, value }) => { -%>
- <%= name %> <%= value %>
<% }) -%>
<% } -%>
<% if (installCommand) { -%>

## Install

```sh
<%= installCommand %>
```
<% } -%>
<% if (usage) { -%>

## Usage

```sh
<%= usage
```

## Run tests

```sh
<%= testCommand %>
```


## Author

👤

* GitHub: https://github.com/heidet

* LinkedIn: https://linkedin.com/in/antoine-heidet/



## 📝 License

Copyright © https://github.com/heidet .<br />

This project is heidet licensed.

***
<%- include('footer.md'); -%>
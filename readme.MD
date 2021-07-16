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
<%= usage %>
```
<% } -%>
<% if (testCommand) { -%>

## Run tests

```sh
<%= testCommand %>
```
<% } -%>
<% if (authorName || authorTwitterUsername || authorGithubUsername) { -%>

## Author
<% if (authorName) { %>
👤 **<%= authorName %>**
<% } %>
<% if (authorGithubUsername) { -%>
* GitHub: [@<%= authorGithubUsername %>](https://github.com/heidet<%= authorGithubUsername %>)
<% } -%>
<% if (authorLinkedInUsername) { -%>
* LinkedIn: [@<%= authorLinkedInUsername %>](https://linkedin.com/in/antoine-heidet/<%= authorLinkedInUsername %>)
<% } -%>
<% } -%>
<% if (issuesUrl) { -%>


## 📝 License

<% if (authorName && authorGithubUsername) { -%>
Copyright © <%= currentYear %> [<%= authorName %>](https://github.com/heidet<%= authorGithubUsername %>).<br />
<% } -%>
This project is [<%= licenseName %>]heidet(<%= licenseUrl %>) licensed.
<% } -%>

***
<%- include('footer.md'); -%>
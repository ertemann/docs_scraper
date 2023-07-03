============
docs_scraper
============


    small python script that allows you replace any exact string or search for occurance of any exact string.


```python
# Execution example - Replace

old = "chat.scrt.network"
new = "scrt.network/discord"
docs_dir = "C:/projs/docs/"

replace_exact(docs_dir, old, new)

# Execution example - find

exact_str = "v1.9"
docs_dir = "C:/projs/docs/"

occurance_list = find_exact (docs_dir, exact_str)

```

Note
====

This project has been set up using PyScaffold 4.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.

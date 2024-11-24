# Paintings

A little Django app built around data from the Joy of Painting episodes. Includes a home dashboard, a paginated table for viewing all the episodes, and individual episode pages that include an embedded YouTube video for watching the episode.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Requires version 3.10 or greater for Python as well as pip for installing modules. Note pip generally comes pre-installed with Python.

- [Python](https://www.python.org/downloads/)

### Installing

After cloning the repository, it is recommended that you setup a virtual environment inside the root of the repository.

```sh
python -m venv .venv
```

Next you will want to activate your environment.

If using Linux/MacOs:

```sh
source .venv/bin/activate
```

If using Windows:

```sh
.venv\Scripts\activate
```

Now, install the requirements with pip:

```sh
pip install -r requirements.txt
```

Verify Django is installed by running:

```sh
python -m django --version
```

If Django is installed you should see the version of your installation.

Next, you will get your sqlite DB setup and seeded with data.

To setup your database, run:

```sh
python manage.py migrate
```

To seed your database run:

```sh
python manage.py loaddata data.json
```

Finally, you can run the application with:

```sh
python manage.py runserver
```

This will spin up a development server and make the app available locally through your web browser. You should get ouput telling you the address that the app is running at. Generally, you can find it at `localhost:8000`.

## Acknowledgments

- The data comes from TidyTuesday: `Data Science Learning Community (2024). Tidy Tuesday: A weekly social data project. https://tidytues.day`
  - [Data](https://github.com/rfordatascience/tidytuesday/tree/master/data/2023/2023-02-21)
- The CSS is based off of [simple.css](https://github.com/kevquirk/simple.css)
- Thanks to YouTube for providing the embedded player so that episodes can be watched.

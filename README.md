# Guze Sports

A web-stack portfolio project that uses beautifulSoup4 to webscrap (extract) data from the internet for sports which runs on the terminal (console API) and web (web API). This project solves issues related to access to real time data related to sports, granting access to multiple sport data without any limitations or fees that comes with this type of data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

#### Clone the Repository (if not already cloned)

If you haven't already cloned the repository, you can do so with the following commands:

```
$ git clone https://github.com/ZeusGolohor/folio.git
$ cd folio
```

#### Set Up Virtual Environment

create a virtual environment named venv (or any other name you prefer):

```
$ python3 -m venv venv
```

#### Activate Virtual Environment

- On Windows:

  ```
  $ venv\Scripts\activate
  ```

- On macOS/Linux:

  ```
  $ source venv/bin/activate
  ```

#### Install Dependencies

Ensure your virtual environment is activated, then install the required packages from requirements.txt:

```
$ pip install -r requirements.txt
```

This command will install the following packages (listed in your requirements.txt file):

- beautifulsoup4==4.12.3
- html5lib==1.1
- six==1.16.0
- soupsieve==2.5
- webencodings==0.5.1
- requests
- tabulate
- lxml
- bcrypt
- sqlalchemy

## Usage

### Terminal (Console API)

To use the terminal/console API, follow these steps:

- Ensure your virtual environment is activated.
- Run the appropriate Python script or command to initiate data extraction or interaction with the sports data.

- #### End points

1. football_today: This command is used to get all football games for the day.

   ```
   (Guze) football_today
   ```

2. football_live: This command is used to get live football games for the day.

   ```
   (Guze) football_live
   ```

3. hockey_live: This command is used to get hockey games for the day.

   ```
   (Guze) hockey_today
   ```

4. hockey_live: This command is used to get live hockey games for the day.

   ```
   (Guze) hockey_live
   ```

5. basketball_today: This command is used to get basketball games for the day.

   ```
   (Guze) basketball_today
   ```

6. basketball_live: This command is used to get live basketball games for the day.

   ```
   (Guze) basketball_live
   ```

7. tennis_today: This command is used to get tennis games for the day.

   ```
   (Guze) tennis_today
   ```

8. tennis_live: This command is used to get live tennis games for the day.

   ```
   (Guze) tennis_live
   ```

9. cricket_today: This command is used to get cricket games for the day.

   ```
   (Guze) cricket_today
   ```

10. cricket_live: This command is used to live cricket games for the day

    ```
    (Guze) cricket_live
    ```

11. list_of_sports: This command is used to get the list of all sports supported by the appication.

    ```
    (Guze) list_of_sports
    To select a sport use the command below
    Usage: select_sport <sport_number>
    +----------+------------+
    |   Number | Sport      |
    +==========+============+
    |        1 | Football   |
    +----------+------------+
    |        2 | Hockey     |
    +----------+------------+
    |        3 | Basketball |
    +----------+------------+
    |        4 | Tennis     |
    +----------+------------+
    |        5 | Cricket    |
    +----------+------------+
    (Guze)
    ```

12. select_sport: This command is used to select one of the available sport by it's number.

    ```
    (Guze) select_sport 1
    You have selected:
    +----------+----------+
    |   Number | Sport    |
    +==========+==========+
    |        1 | Football |
    +----------+----------+
    (Guze) select_sport 4
    You have selected:
    +----------+---------+
    |   Number | Sport   |
    +==========+=========+
    |        4 | Tennis  |
    +----------+---------+
    (Guze)
    ```

13. delete_monitored_sport: This command is used to delete a sport that has been selected before using the 'select_sport' command, by using the sport number.

    ```
    (Guze) delete_monitored_sport 4
    From monitored sports, you have deleted:
    +----------+---------+
    |   Number | Sport   |
    +==========+=========+
    |        4 | Tennis  |
    +----------+---------+
    (Guze)
    ```

14. delete_all_monitored_sports: This command is used to delete all selected sports.

    ```
    (Guze) delete_all_monitored_sports
    All monitored sports have been deleted
    (Guze)
    ```

15. all_monitored_sports: This command is used to list all sports selected using the 'select_sport' command.

    ```
    (Guze) all_monitored_sports
    List of all monitored sports:
    +----------+---------+
    |   Number | Sport   |
    +==========+=========+
    |        2 | Hockey  |
    +----------+---------+
    |        4 | Tennis  |
    +----------+---------+
    |        5 | Cricket |
    +----------+---------+
    (Guze)
    ```

16. all_lt: This command is used to get and list all live leagues and tournaments for all selected sports.

    ```
    (Guze) all_lt
    ```

### Web API

To use the web API, follow these steps:

- Ensure your virtual environment is activated.
- Run the web application using the specified command

  ```
  $ python3 -m api.v1.app
  ```

- Access the web API endpoints through your terminal, browser or a tool like Postman.

- #### End points

1. football_today:

   - Description: This endpoint gets information for football games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: football_today

   - Example:

     ```
     GET http://localhost:5000/api/v1/football_today
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "Argentina - Primera Division": {
               "date": "July 23",
               "live_lt": {
                   "1": {
                   "away": "Argentinos Juniors",
                   "away_score": "0",
                   "home": "Deportivo Riestra",
                   "home_score": "2",
                   "time": "FT"
                   },
                   "2": {
                   "away": "San Lorenzo de Almagro",
                   "away_score": "1",
                   "home": "Gimnasia LP",
                   "home_score": "0",
                   "time": "FT"
                   },
               }
               ...
               }
           }
       }
     ```

2. football_live:

   - Description: This endpoint gets information for football live games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: football_live

   - Example:

     ```
     GET http://localhost:5000/api/v1/football_live
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "Club Friendlies - Club Friendlies 2024": {
               "date": "July 22",
               "live_lt": {
                   "1": {
                   "away": "Adelaide United",
                   "away_score": "8",
                   "home": "Cumberland United",
                   "home_score": "1",
                   "time": "FT"
                   },
                   "2": {
                   "away": "Sporting CP",
                   "away_score": "",
                   "home": "Farense",
                   "home_score": "",
                   "time": "Canc."
                   },
               }
               ...
               }
           }
       }
     ```

3. basketball_today:

   - Description: This endpoint gets information for basketball games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: basketball_today

   - Example:

     ```
     GET http://localhost:5000/api/v1/basketball_today
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "EuroBasket U18 - Division C: Group A": {
                  "date": "July 25",
                  "live_lt": {
                    "1": {
                      "away": "San Marino U18",
                      "away_score": [],
                      "home": "Albania U18",
                      "home_score": [],
                      "time": "09:30"
                    },
                    "2": {
                      "away": "Luxembourg U18",
                      "away_score": [],
                      "home": "Gibraltar U18",
                      "home_score": [],
                      "time": "12:00"
                    }
                  },
                  "name": "EuroBasket U18 - Division C: Group A"
                },
            ...
           }
        }
     ```

4. basketball_live:

   - Description: This endpoint gets information for basketball live games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: basketball_live

   - Example:

     ```
     GET http://localhost:5000/api/v1/basketball_live
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "EuroBasket U18 - Division C: Group A": {
                  "date": "July 25",
                  "live_lt": {
                    "1": {
                      "away": "San Marino U18",
                      "away_score": [],
                      "home": "Albania U18",
                      "home_score": [],
                      "time": "09:30"
                    },
                    "2": {
                      "away": "Luxembourg U18",
                      "away_score": [],
                      "home": "Gibraltar U18",
                      "home_score": [],
                      "time": "12:00"
                    }
                  },
                  "name": "EuroBasket U18 - Division C: Group A"
                },
            ...
           }
        }
     ```

5. hockey_today:

   - Description: This endpoint gets information for hockey games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: hockey_today

   - Example:

     ```
     GET http://localhost:5000/api/v1/hockey_today
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
      {
        "data": {
          "International - Club Friendlies": {
            "date": "July 24",
            "live_lt": {
              "1": {
                "away": "Krylya Sovetov",
                "away_score": "()",
                "home": "SKA-Junior",
                "home_score": "()",
                "time": "03:00"
              },
              "2": {
                "away": "Chaika",
                "away_score": "()",
                "home": "MHC Dynamo",
                "home_score": "()",
                "time": "08:00"
              }
            },
            "name": "International - Club Friendlies"
          }
        }
      }
     ```

6. hockey_live:

   - Description: This endpoint gets information for hockey live games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: hockey_live

   - Example:

     ```
     GET http://localhost:5000/api/v1/hockey_live
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
      {
        "data": {
          "International - Club Friendlies": {
            "date": "July 24",
            "live_lt": {
              "1": {
                "away": "Krylya Sovetov",
                "away_score": "()",
                "home": "SKA-Junior",
                "home_score": "()",
                "time": "03:00"
              },
              "2": {
                "away": "Chaika",
                "away_score": "()",
                "home": "MHC Dynamo",
                "home_score": "()",
                "time": "08:00"
              }
            },
            "name": "International - Club Friendlies"
          }
        }
      }
     ```

7. tennis_today:

   - Description: This endpoint gets information for tennis games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: tennis_today

   - Example:

     ```
     GET http://localhost:5000/api/v1/tennis_today
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "ATP 250 - Atlanta Open": {
                "date": "July 24",
                "live_lt": {
                    "1": {
                    "away": "Jackson Withrow || Nathaniel Lammons",
                    "away_score": "",
                    "home": "Constant Lestienne || Juncheng Shang",
                    "home_score": "",
                    "time": "Canc."
                    },
                    "2": {
                    "away": "Jackson Withrow || Nathaniel Lammons",
                    "away_score": "",
                    "home": "Niki Kaliyanda Poonacha || Rithvik Bollipalli",
                    "home_score": "",
                    "time": "08:00"
                    },
               }
               ...
               }
           }
       }
     ```

8. tennis_live:

   - Description: This endpoint gets information for tennis live games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: tennis_live

   - Example:

     ```
     GET http://localhost:5000/api/v1/tennis_live
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
               "ATP 250 - Atlanta Open": {
                "date": "July 24",
                "live_lt": {
                    "1": {
                    "away": "Jackson Withrow || Nathaniel Lammons",
                    "away_score": "",
                    "home": "Constant Lestienne || Juncheng Shang",
                    "home_score": "",
                    "time": "Canc."
                    },
                    "2": {
                    "away": "Jackson Withrow || Nathaniel Lammons",
                    "away_score": "",
                    "home": "Niki Kaliyanda Poonacha || Rithvik Bollipalli",
                    "home_score": "",
                    "time": "08:00"
                    },
               }
               ...
               }
           }
       }
     ```

9. cricket_today:

   - Description: This endpoint gets information for cricket games for the day.
   - Endpoint URL:

     - Base URL: http://localhost:5000/api/v1/
     - Resource: cricket_today

   - Example:

     ```
     GET http://localhost:5000/api/v1/cricket_today
     ```

   - HTTP Methods

     - GET: This method retrieves data about a specific resource.

   - Request Parameter:

     - None

   - Authentication:

     - None

   - Response Format:
     The response will be formated in JSON format.

     - status code: 200 for success
     - Response Body: Describe the structure of the response data.

   - Example: (JSON Schema):

     ```
       {
           "data": {
                "Canada - Global T20 Canada": {
                  "date": "July 25",
                  "live_lt": {
                    "1": {
                      "away": "Toronto Nationals",
                      "away_score": "",
                      "home": "Vancouver Knights",
                      "home_score": "",
                      "time": "13:00"
                    }
                  },
                  "name": "Canada - Global T20 Canada"
                },
               ...
          }
      }
     ```

10. cricket_live:

- Description: This endpoint gets information for cricket live games for the day.
- Endpoint URL:

  - Base URL: http://localhost:5000/api/v1/
  - Resource: cricket_live

- Example:

  ```
  GET http://localhost:5000/api/v1/cricket_live
  ```

- HTTP Methods

  - GET: This method retrieves data about a specific resource.

- Request Parameter:

  - None

- Authentication:

  - None

- Response Format:
  The response will be formated in JSON format.

  - status code: 200 for success
  - Response Body: Describe the structure of the response data.

- Example: (JSON Schema):

  ```
       {
           "data": {
                "Canada - Global T20 Canada": {
                  "date": "July 25",
                  "live_lt": {
                    "1": {
                      "away": "Toronto Nationals",
                      "away_score": "",
                      "home": "Vancouver Knights",
                      "home_score": "",
                      "time": "13:00"
                    }
                  },
                  "name": "Canada - Global T20 Canada"
                },
               ...
          }
      }
  ```

11. users:

- Description: This create a new user.
- Endpoint URL:

  - Base URL: http://localhost:5000/api/v1/
  - Resource: users

- Example:

  ```
  POST https://localhost:5000/api/v1/users -d 'email=zeusgolohor@gmail.com' -d 'password=password' -v
  ```

- HTTP Methods

  - POST: This method creates data about a specific resource.

- Request Parameter:

  - email: new user email
  - password: new user password

- Authentication:

  - None

- Response Format:
  The response will be formated in JSON format.

  - status code: 200 for success, 400 for email already registered
  - Response Body: Describe the structure of the response data.

- Example: (JSON Schema):

  ```
    {
        "email": "zeus@gmail.com",
        "message": "user created"
    }
  ```

12. sessions:

- Description: This create a user session and also log the user into the application.
- Endpoint URL:

  - Base URL: http://localhost:5000/api/v1/
  - Resource: sessions

- Example:

  ```
  POST http://localhost:5000/api/v1/sessions -d 'email=zeus@gmail.com' -d 'password=password' -v
  ```

- HTTP Methods

  - POST: This method creates data about a specific resource.

- Request Parameter:

  - email: new user email
  - password: new user password

- Authentication:

  - None

- Response Format:
  The response will be formated in JSON format.

  - status code: 200 for success, 401 for bad user login details
  - Response Body: Describe the structure of the response data.

- Example: (JSON Schema):

  ```
    {
        "email": "zeus@gmail.com",
        "message": "logged in"
    }
  ```

13. profile:

- Description: This gets a user profile deteils via a user session id.
- Endpoint URL:

  - Base URL: http://localhost:5000/api/v1/
  - Resource: profile

- Example:

  ```
  GET http://localhost:5000/api/v1/profile -b "session_id=ID"
  ```

- HTTP Methods

  - GET: This method retrieves data about a specific resource.

- Request Parameter:

  - session_id: a logged in user sessions id

- Authentication:

  - None

- Response Format:
  The response will be formated in JSON format.

  - status code: 200 for success, 403 for bad user session details
  - Response Body: Describe the structure of the response data.

- Example: (JSON Schema):

  ```
    {
        "email": "zeus@gmail.com"
    }
  ```

14. session:

- Description: This log a user out of the application.
- Endpoint URL:

  - Base URL: http://localhost:5000/api/v1/
  - Resource: sessions

- Example:

  ```
    DELETE http://localhost:5000/api/v1/sessions -d "session_id=id"
  ```

- HTTP Methods

  - DELETE: This method removes data about a specific resource.

- Request Parameter:

  - session_id: a logged in user sessions id

- Authentication:

  - True

- Response Format:
  The response will be formated in JSON format.

  - status code: 200 for success, 401 for bad user login details
  - Response Body: Describe the structure of the response data.

- Example: (JSON Schema):

  ```
    {
        "message": "User logged out"
    }
  ```

## Contributing

Since this project is developed and maintained by a single individual, external contributions in the form of pull requests are not expected at this time. However, you can still contribute by:

- Testing and providing feedback.
- Reporting bugs or suggesting new features through [GitHub Issues](https://github.com/ZeusGolohor/folio/issues).
- Sharing the project with others who might find it useful.
- Providing constructive feedback or suggestions for improvement.

If you have any questions, ideas, or feedback, feel free to reach out via [email](mailto:zeusgolohor@gmail.com).

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

This is a human-readable summary of (and not a substitute for) the [license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

**You are free to:**

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

The licensor cannot revoke these freedoms as long as you follow the license terms.

**Under the following terms:**

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

**No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

## Contact

Feel free to reach out with any questions, feedback, or suggestions:

Email: [zeusgolohor@gmail.com](mailto:zeusgolohor@gmail.com)

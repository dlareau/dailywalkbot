# DailyWalkBot

A [Twitter bot](https://twitter.com/DailyWalkBot) that takes long, random walks
through the world in real-time.

## Installation

Dependencies are managed with [`pip`](https://pip.pypa.io/en/latest/installing.html).
Install the necessary modules with:

    pip install --user -r requirements.txt

## Configuration

Copy the API keys template file to `api_keys.py` and insert your Twitter and
Google API keys:

    cp api_keys{_template,}.py
    $EDITOR api_keys.py
    # Insert API keys.

Several constants are defined at the top of `daily_walk.py`.
In particular, set `TWEET_ON = False` to print to the console instead of tweeting to Twitter,
and set `SLEEP_ON = False` to remove the "real-time" delays for testing purposes.

## Invocation

Run the script with `python daily_walk.py`.

To run at regular intervals, append a line to your `crontab`.
For example, to begin a walk at 10:00 daily,

    (crontab -l ; echo "0 10 * * * python /full/path/to/daily_walk.py") | crontab -

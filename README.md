# lightnovel
Just a random little collection of scripts that scrapes titles from [Novel Updates](https://www.novelupdates.com/) and creates randomly-generated titles using the power of Markov chains. I originally wanted to make a neural network but I don't have the time / resources to do that yet.

All of these scripts run on the terminal and can be cancelled any time by pressing `Ctrl-C`. The scripts that fetch new novel titles save all the titles onto a Python pickle file, and you can pick up from where you left off once you run the script again.

## Scripts

`scrape.py`: Fetches the titles of the most recently updated novels. Goes through all 1000 pages of the front page.

`random_novel.py`: Simulates pressing the "Random Novel" link a bunch of times and adding the novel title to the pickle file.

`markov.py`: A sort of quiz game that prints either a real or fake title. You have to determine whether it's real or fake.

## Notes

Because of the nature of Markov chains, a lot of the randomly-generated titles can be nonsense or grammatically incorrect, making them obvious when distinguishing from real to fake. It might take a while before it generates a believable fake. Maybe a neural network would work better.
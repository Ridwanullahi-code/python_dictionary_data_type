playlist = {
	"title": "patagonia",
	"autor": "colt steele",
	"song": [
	{"title":"song1", "artist":["blue"], "duration":25},
	{"title":"song2", "artist":["kitty","djcat"], "duration":5.25},
	{"title":"meowmeo", "artist":["garfield"], "duration":2.0},
	]
}
total_length = 0
for song in playlist["song"]:
	total_length += song["duration"]
print(total_length)
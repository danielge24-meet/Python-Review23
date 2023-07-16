def create_youtube_video (title, description):
	youtube_video={"title":title, "description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtube_video

def like(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"] += 1
	return youtubevideo	

def dislike(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"] += 1
	return youtubevideo

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

youtube_video=create_youtube_video(input("what would you like the title to be"), input("what would you like the description to be"))
for i in range(495):
	like(youtube_video)
dislike (youtube_video)

video = add_comment(youtube_video,input("what ifis your username"),input("what comment would you like to leave"))
print(video)
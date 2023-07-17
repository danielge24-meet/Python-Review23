def create_youtube_video (title, description):
	hashtags =set()
	for i in range(5):
		hashtags.add(input("hashtags: "))
	youtube_video={"title":title, "description":description,"likes":0,"dislikes":0,"comments":{},"hashtags":hashtags}
	return youtube_video

def like(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"] += 1
	return youtubevideo	

def dislike(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"] += 1
	return youtubevideo

def similarity_to_video(vid1,vid2):
	s_vid1=vid1["hashtags"]	
	s_vid2=vid2["hashtags"]
	similiar_set=s_vid1.intersection(s_vid2)
	float_percentage=(len(similiar_set)/max(len(s_vid1),len(s_vid2)))*100
	return float_percentage

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

youtube_video=create_youtube_video(input("what would you like the title to be"), input("what would you like the description to be"))
for i in range(495):
	like(youtube_video)
dislike (youtube_video)

video = add_comment(youtube_video,input("what is your username"),input("what comment would you like to leave"))
print(video)

youtube_video2=create_youtube_video(input("what would you like the title to be"), input("what would you like the description to be"))
video2= add_comment(youtube_video2,input("what is your username"),input("what comment would you like to leave"))
pe=similarity_to_video(video,video2)


print("the percentage of similirity is: "+str(pe)+"%")
from firebase_admin import auth
from kite.services.firebase import store

def rankUsers(claim,me):
    score_input_p = store.collection('users1').where('user_id', '==', claim).get()[0].to_dict()
    score_input = store.collection('posts1').where('public_profile_id', '==', score_input_p.get("publicProfileId")).get()
    follows = len(score_input_p.get("followers"))
    follows += 10 if me in score_input_p.get("followers") else 0
    activity = len(score_input)
    likes = 0
    comments = 0
    for scorei in score_input:
        score = scorei.to_dict()
        # if instance code will be deleted when we reset the posts
        likes += score.get("likes") if isinstance(score.get("likes"), int) else len(score.get("likes"))
        likes += 5 if claim in score.get("likes") else 0
        comments += len(score.get("comments"))
        comments += 5 if claim in score.get("comments") else 0
    return [{'activity':activity,'follows':follows,'likes':likes,'comments':comments},activity + follows + likes + comments]
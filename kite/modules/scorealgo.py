from firebase_admin import auth
from kite.services.firebase import store

def scorify(claim):
    score_input_p = store.collection('users1').where(
        'user_id', '==', claim).get()[0].to_dict()
    score_input = store.collection('posts1').where(
        'user_id', '==', claim).get()

    follows = len(score_input_p.get("followers"))
    activity = len(score_input)
    likes = 0
    comments = 0
    for scorei in score_input:
        score = scorei.to_dict()
        likes += score.get("likes") if isinstance(score.get("likes"), int) else len(score.get("likes"))
        comments += len(score.get("comments"))
    return {'activity':activity,'follows':follows,'likes':likes,'comments':comments,'total':activity + follows + likes + comments}
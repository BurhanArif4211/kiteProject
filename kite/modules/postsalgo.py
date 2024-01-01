from kite.services.firebase import store
import random

def post_fetching_algo(limit=10):
    char_set = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    char = random.choice(char_set)
    print(f"algorithm char is selected to be {char}")
    # Query to filter posts with a specific character in the "postid" field
    posts_ref = store.collection("posts1").where("post_id", ">=", char).limit(limit).stream()

    """
    TODO: i will also add a step to check if the user has interacted with the post and if interacted remove from array by tossing!!!
    """

    # Fetch 10 posts that contain the specified character in their post ID
    posts = []
    for post in posts_ref:
        post_data = post.to_dict()
    
        # Replace problematic characters with their Unicode escape sequences
        sanitized_data = {key: value.encode('utf-8', 'replace').decode('utf-8') if isinstance(value, str) else value for key, value in post_data.items()}
        
        posts.append(sanitized_data)
    random.shuffle(posts)
    return posts

def fetch_documents_noalgo(limit=50):
    collection_ref = store.collection('posts1')

    documents = collection_ref.limit(limit).stream()

    data_list = []
    for doc in documents:
        data = doc.to_dict()
        data_list.append(data)

    random.shuffle(data_list)
    return data_list
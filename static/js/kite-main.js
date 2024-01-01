
function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

                break;
            }
        }
    }

    return cookieValue;
}


    function openTab(evt, tabname) {
        // Declare all variables
        var i, tabcontent, tablinks;

        // Get all elements with class="tabcontent" and hide them
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Get all elements with class="tablinks" and remove the class "active"
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        // Show the current tab, and add an "active" class to the button that opened the tab
        document.getElementById(tabname).style.display = "block";
     //   evt.currentTarget.className += " active";
    }
    openTab(event, 'Posts')

    // Fetch and load the post grid component asynchronously
    fetch('/api/loaduserposts', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
        .then(response => response.text())
        .then(html => {
            document.getElementById('post-grid-container').innerHTML = html;
        });


    // Function to fetch and load the modal content asynchronously
    function loadUploadModalContent() {
        fetch('/uploadpost',
            {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
            })
            .then(response => response.text())
            .then(html => {
                // Set the modal content
                document.getElementById('modal-container').innerHTML = html;
                // Show the modal
                $('#uploadPostModal').modal('show');
            });
    }
      

    
    
    document.getElementById('pp-input').addEventListener('change', function () {
        var input = this;
        var data = new FormData();
        data.append('profilePicture', input.files[0]);
        const csrftoken = getCookie('csrftoken');
        fetch('/api/uploaduserpic', {
            method: 'POST',
            body: data,
            headers: {
             'X-CSRFToken': csrftoken
              },
        })
        .then(response => {

            console.log(response);

            document.getElementById('profilePicture').src =response.url

        })
        .catch(error => console.error('There has been a problem with your fetch operation: ', error));
    });




    function commentToggle(a) {
        console.log(a.closest(".card").getElementsByClassName('comment-box')[0].toggleAttribute("hidden"))
    }



    function conditionPop(x){
        alert(x) //Change with a good looking modal
    }
    function posterror(){
        conditionPop("Post or user not found, it commonly happens when the owner deletes the post")
    }
    function redirect(){
        location.href = "./login"
    }
    function unliked(x){
        x.classList.add("btn-info")
        x.classList.remove("btn-outline-info")
        x.innerHTML = x.innerHTML.replace("Downvote",'Upvote')
        x.innerHTML = x.innerHTML.replace("-down",'-up')
        count = parseInt(x.innerHTML.match(/[0-9]+/g)[0])
        x.innerHTML = x.innerHTML.replace(count,count-1)
    }
    function liked(x){
        x.classList.add("btn-outline-info")
        x.classList.remove("btn-info")
        x.innerHTML = x.innerHTML.replace("Upvote",'Downvote')
        x.innerHTML = x.innerHTML.replace("-up",'-down')
        count = parseInt(x.innerHTML.match(/[0-9]+/g)[0])
        x.innerHTML = x.innerHTML.replace(count,count+1)
    }
    function toggleLike(a){
        fetch(`/api/like/${a.getAttribute("post-id")}`).then(response => response.text()).then(data => {
            eval(`${data}(a)`)
        })
    }
//aynchronously load servies
function loadService(){
    fetch("/components/api/services/{{ profile_info.publicProfileId }}/")
    .then(res => res.text())
    .then(data => {
        document.getElementById("Services").innerHTML = data;
    })
}